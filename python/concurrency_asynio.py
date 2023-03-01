import aiohttp
import asyncio
import time

from variable import variable

async def call_api():
    async with aiohttp.ClientSession() as session:
        async with session.get(variable.URL.value, timeout=5) as resp:
            response = await resp.text()
            print(response)

async def main():
    task_list = []

    for _ in range(variable.LOOP_COUNT.value):
        task = asyncio.create_task(call_api())
        task_list.append(task)
    for task in task_list:
        await task
        #await asyncio.gather(*task_list)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f'It costs {str(end_time - start_time)} s')