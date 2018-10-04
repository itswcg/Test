# with是简化try/finally模式, 保证一段代码运行完毕后执行某项操作
# 上下文管理器协议包含__enter__, __exit__


import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reserse_write(txt):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'WCG' # 在yield之前__enter__, 之后__exit__
    sys.stdout.write = original_write
