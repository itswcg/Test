# 并发是指一次处理多见事, 并行是指一次做多件事


# 线程
def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


# 协程
@asyncio.coroutine
def supervisor():
    spinner = asncio.asyn(spin('thinking!'))
    result = yield from slow_function()
    spinner.cancel()
    return result
