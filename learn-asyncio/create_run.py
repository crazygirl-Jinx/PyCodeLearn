import asyncio
from datetime import datetime as dt





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




if __name__ == '__main__':
    # asyncio.run(coro())
    # asyncio.run(display_date())
    asyncio.run(main())
    