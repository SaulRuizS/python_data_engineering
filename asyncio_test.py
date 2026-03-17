import asyncio

async def asyncFunction():
    print('Test...')
    await asyncio.sleep(5)
    print('...ing')

asyncio.run(asyncFunction())