import asyncio


def func_later():
    print('later')


def func_soon():
    print('soon')


def stopper(loop):
    print('stopper invoked')
    loop.stop()


event_loop = asyncio.get_event_loop()
try:
    event_loop.call_later(30, func_later)
    event_loop.call_soon(func_soon)
    event_loop.call_later(40, stopper, event_loop)
    print('entering event loop')
    event_loop.run_forever()
finally:
    event_loop.close()
