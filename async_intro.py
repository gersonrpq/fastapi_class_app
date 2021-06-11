import time
from typing import Callable  

import requests

import asyncio
import aiohttp

async def get_page_asynchronously(url: str) -> int:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            status_code = response.status
    print(url, status_code)
    

async def get_pages_list_asynchornously(pages: list) -> None:
    await asyncio.gather(*[get_page_asynchronously(page) for page in pages])
    

def get_page_synchronously(url: str) -> int:
    status_code = requests.get(url).status_code
    print(url, status_code)

def get_pages_list_synchronously(pages: list) -> None:
    for page in pages:
        get_page_synchronously(page)


pages_list =['https://www.google.com','https://www.facebook.com/','https://twitter.com',
             'https://platzi.com/','https://www.wikipedia.org/']

def time_function(func: Callable) -> None:
    start_time = time.perf_counter()
    func()
    elapsed_time = time.perf_counter() - start_time
    print(f"Function time was {elapsed_time}")
# Synch time
print("sync test")
time_function(lambda: get_pages_list_synchronously(pages_list))

# Async time
print("async test")
time_function(lambda: asyncio.run(get_pages_list_asynchornously(pages_list)))