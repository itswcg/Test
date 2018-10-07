# 抨击线程的往往是系统程序员, 所以我要学会抨击线程

# 下载
# 单线程
# 循环+requests


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)


# concurrent.futures #  多线程
from concurrent import futures


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))

# 多进程


def download_many(cc_list):
    with futures.ProcessPoolExecutor() as executor:
        pass


# cpython解释器本身就不是线程安全的, 因此需要全局解释器锁,GIL
