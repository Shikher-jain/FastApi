from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker

host = "localhost"
user = "postgres"
password = quote_plus("sh!kherj@!n786")
database = "practice"
port = 5432

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
      