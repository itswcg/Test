import time
from tqdm import tqdm

for i in tqdm(range(1000)):
    time.sleep(.01)


# 对于CPU密集工作, 启动多个进程,
# 最简单futures.ProcessPoolExecutor, 然后mutiprocess
# 线程 futures.ThreadPoolExecutor, 然后threading
