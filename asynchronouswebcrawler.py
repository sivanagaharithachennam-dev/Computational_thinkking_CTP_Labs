import asyncio
import aiohttp
import time


urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]


async def fetch(session, url):
    for attempt in range(3):
        try:
            async with session.get(url) as response:
                return response.status

        except Exception:
            if attempt == 2:
                return "Failed"

            await asyncio.sleep(1)


async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    end = time.time()

    print("Status:", results)
    print("Async Time:", round(end - start, 2), "seconds")


asyncio.run(main())