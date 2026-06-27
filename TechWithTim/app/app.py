from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostCreate, PostResponse
from app.db import Post, get_async_session, create_db_and_tables
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select

from app.images import imagekit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions 

import os ,shutil, uuid, tempfile 

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "API is running "}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(...),
    session: AsyncSession = Depends(get_async_session)
):
    temp_file_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False,suffix=os.path.splitext(file.filename)[1]) as temp_file:
            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

        upload_result = imagekit.upload_file(
            file=open(temp_file_path, "rb"),
            file_name=file.filename,
            options=UploadFileRequestOptions(
                use_unique_file_name=True,
                tags=["backend-upload"],
                )
            )
        
        if upload_result.response_metadata.http_status_code == 200:
            post = Post(
                caption=caption,
                url=upload_result.url,
                file_type=file.content_type,
                file_name=upload_result.name
            )
            
            session.add(post)
            await session.commit()
            await session.refresh(post)
            return post
     
    except Exception as e:
        import traceback
        traceback.print_exc()  # logs full stack trace in terminal
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
        file.file.close()

@app.get("/feed/")
async def get_feed(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts =  [row[0] for row in result.all()]  # Return a list of Post objects
    posts_data = []
    for post in posts:
        posts_data.append({
            "id":str(post.id),
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat() 
        })
    return { "posts": posts_data }
