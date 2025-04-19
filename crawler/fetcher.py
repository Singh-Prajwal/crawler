import aiohttp
import asyncio
from aiohttp import ClientTimeout

async def fetch(session, url, retries=3):
    try:
        for attempt in range(retries):
            try:
                async with session.get(url, timeout=ClientTimeout(total=10)) as response:
                    if response.status == 200 and 'text/html' in response.headers.get('Content-Type', ''):
                        return await response.text()
            except Exception as e:
                if attempt < retries - 1:
                    await asyncio.sleep(1)
                else:
                    print(f"\033[91m[ERROR]\033[0m Failed to fetch {url}: {e}")
        return None
    except Exception as e:
        print(f"\033[91m[ERROR]\033[0m Exception in fetch(): {e}")
        return None
