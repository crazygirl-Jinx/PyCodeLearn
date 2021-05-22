import asyncio
from datetime import datetime as dt
import time




async def coro():
    await asyncio.sleep(2);
    print("sleep",dt.now());


async def  main():
    task = asyncio.create_task(coro())
    print("The task is a : ",type(task))
    await task






# 睡眠五秒 每秒一个时间
async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(dt.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)



async def factorial(name:str, number:int) -> int:
    f = 1;
    for i in range(2, number+1):
        print(f"Task {name}: Compute factorial({number}), currnetly i={i}...");
        await asyncio.sleep(1);
        f *= i;
    print(f"Task {name} : factorial({number}) = {f}");
    return f;

async def main():
    L = await asyncio.gather(
        factorial("A",2),
        factorial("B",3),
        factorial("C",4),
    );
    print(L);


# wait_for 超时
async def eternity():
    await asyncio.sleep(3600);
    print("yeah!");

async def main():
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError as e:
        print("timeout: ", e);
# wait 等待
# asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
"""
FIRST_COMPLETED: 函数将在任意可等待对象结束或取消时返回。

FIRST_EXCEPTION: 函数将在任意可等待对象因引发异常而结束时返回。当没有引发任何异常时它就相当于 ALL_COMPLETED。

ALL_COMPLETED: 函数将在所有可等待对象结束或取消时返回。
"""

async def foo():
    return 0;

async def main():
    task = asyncio.create_task(foo());
    # done, pending = await asyncio.wait(foo())  该方式已被弃用
    done, pending = await asyncio.wait([task]);

    print("done is :", done, "pending is :", pending);




# 通过线程异步 to_thread(function, *args, **kwargs)
# 在不同的线程线程运行function  不定长参数会传给function

def blocking_io():
    print(f"start blocking_io at {time.strftime(' %X')}");
    time.sleep(1);
    print(f"blocking_io complete at {time.strftime('%X')}");
    
async def main():
    print(f"starte main at {time.strftime(' %X')}");

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1)
    );
    
    print(f"finished main at {time.strftime(' %X')}");


async def main():
    # Create a coroutine
    coro = asyncio.sleep(1, result=3)
    loop = asyncio.new_event_loop()
    # Submit the coroutine to a given loop
    future = asyncio.run_coroutine_threadsafe(coro, loop)

    # Wait for the result with an optional timeout argument
    assert future.result() == 3


if __name__ == '__main__':
    # asyncio.run(coro())
    # asyncio.run(display_date())
    # asyncio.run(main())
    print('sdas ')
