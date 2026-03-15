import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return "data"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())

import asyncio

async def fetch_data(id):
    await asyncio.sleep(2)
    return f"data {id}"

async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    
    print(results)

asyncio.run(main())