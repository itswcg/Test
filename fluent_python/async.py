import asyncio
import threading


async def hello():
    print(f'hello world {threading.currentThread()}')
    await asyncio.sleep(1)
    print(f'hello again {threading.currentThread()}')


loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
