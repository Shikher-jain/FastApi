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
    # await asyncio.sleep(2)
    return f"data {id}"

async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    
    print(results)

async def main():
    print(await fetch_data(1))
    print(await fetch_data(2))
    print(await fetch_data(3))
    print(await fetch_data(4))
    print(await fetch_data(5))
    print(await fetch_data(6))

    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
        fetch_data(4),
        fetch_data(5),
        fetch_data(6)
    )
    print(results)
        
    
    # print(results)
# for _ in range(6):
    # asyncio.run(main())
asyncio.run(main())