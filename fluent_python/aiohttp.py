import asyncio
import aiohttp


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)


# 使用asyncio包时, 相当于架起了管道, 让asyncio事件循环驱动执行底层异步I/O操作的库函数

# 回调地狱 每一次操作依赖之前操作的结果

@asyncio.coroutine
def three_stages(request1):
    respones1 = yield from api_call1(request1)
    request2 = step1(respones1)
    response2 = yield from api_call2(request2)
    request3 = step2(response2)
    respones3 = yield from api_call3(request3)
    step3(respones3)


loop.create_task(three_stages(request1))
