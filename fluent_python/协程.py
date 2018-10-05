# yield 视作控制流程的方式

from functools import wraps


def coraoutine(func):
    """装饰器, 预激func"""
    def primer(*args, **kw):
        gen = func(*args, **kw)
        next(gen)
        return gen
    return primer


class DemoException(Exception):
    pass


@coraoutine
def demo_exc_handing():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('')
        else:
            print('')
    raise RuntimeError('')

# yield from 简化for循环中的yield表达式


def gen():
    for c in 'AB':
        yield c


def gen():
    yield from 'AB'

# throw() 抛出异常, close() 关闭

# 离散事件仿真
# 离散 -> 回合制游戏 -> 协程
# 连续仿真 -> 实时游戏 -> 多线程
