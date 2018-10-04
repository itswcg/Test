# for/else while/else try/else

# 仅当for循坏运行完毕,才运行else
for item in my_list:
    if item.flavor == 'banana':
        break
else:
    raise ValueError('No banana flavor found!')

# while同理

# 仅当try没有没有异常抛出才执行
try:
    dangerous_call()
    after_call()
except OSError:
    log('OSError...')

# 优化
try:
    dangerous_call()
except OSError:
    log('OSError...')
else:
    after_call()
