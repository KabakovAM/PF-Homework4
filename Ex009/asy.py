import asyncio
import aiohttp
import time

start = time.time()

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            filename = str(url.split('/')[-1:]).replace("['",'').replace("']",'')
            filepath = 'Homework4/Download/' + str(url.split('/')[-1:]).replace("['",'').replace("']",'')
            with open (filepath,'wb') as f:
                f.write(content)
            print(f'{time.time()-start:.2f} секунд - {filename}')


async def main(urls):
    tasks = []
    for i in range(len(urls)):
        a = asyncio.ensure_future(download(urls[i]))
        tasks.append(a)
    await asyncio.gather(*tasks)

def run(urls):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
    print(f'{time.time()-start:.2f} секунд - общее время')