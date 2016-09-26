import asyncio
import operator


async def addition(num):
    print('add coroutine')
    return operator.add(num, 5)

async def multiply(num):
    print('mul coroutine')
    return operator.mul(num, 5)


async def arthimetic_coroutine(num):
    print('main coroutine')
    result_sum = await addition(num)
    result_mul = await multiply(num)
    return (result_sum, result_mul)


event_loop = asyncio.get_event_loop()

try:
    print('entering event loop')
    # _func = arthimetic_coroutine(12)
    # print(dir(_func))
    # print(_func.cr_running)
    return_val = event_loop.run_until_complete(arthimetic_coroutine(3))
    print('coroutine returned {0}'.format(return_val))
finally:
    print('closing event loop')
    event_loop.close()
