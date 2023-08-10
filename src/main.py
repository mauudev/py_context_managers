import asyncio

from src.resource_managers import (
    AsyncAPIClient,
    CustomLogger,
    SyncAPIClient,
    TempDirectory,
    Timer,
    db_session,
    timer,
)

# my custom logger
with CustomLogger() as logger:
    logger.write_log(
        "The shade is a tool, a device, a savior\nSee, I try and look up to the sky\nBut my eyes burn .."
    )

# timer
with Timer():
    for i in range(1000000):
        ...

with timer():
    for _ in range(1000000):
        ...


# temp dirs
with TempDirectory() as temp_dir:
    # inside this block, temp_dir is a path to a temporary directory
    print(f"Doing work in {temp_dir}")
    # you can create files and directories inside temp_dir, and they will be cleaned up automatically

# db transactions
with db_session() as db_transaction:
    # realizar queries, mutations etc
    ...

# sync api client
with SyncAPIClient("https://dummyjson.com") as client:
    data = client.make_request("comments")
    print(data)


# async api client
async def main():
    async with AsyncAPIClient("https://dummyjson.com") as client:
        users = await client.make_request("users")
        print(users)

        products = await client.make_request("products")
        print(products)

        posts = await client.make_request("posts")
        print(posts)


asyncio.run(main())
