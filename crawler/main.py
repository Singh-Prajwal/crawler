import asyncio
import aiohttp
import os
import re
import json
from urllib.parse import urlparse, urlunparse
from fetcher import fetch
from parser import extract_links
from config import DOMAIN_PATTERNS

MAX_DEPTH = 3
CONCURRENT_REQUESTS = 10
semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)

visited = set()
product_links = {}
lock = asyncio.Lock()
all_visited_urls = set()

def log_success(message):
    print(f"\033[92m[SUCCESS]\033[0m {message}")

def log_info(message):
    print(f"\033[94m[INFO]\033[0m {message}")

def log_error(message):
    print(f"\033[91m[ERROR]\033[0m {message}")

def log_product(message):
    print(f"\033[93m[PRODUCT FOUND]\033[0m {message}")

def normalize_url(url):
    try:
        parsed = urlparse(url)
        return urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip('/'), '', '', ''))
    except Exception as e:
        log_error(f"Failed to normalize URL {url}: {e}")
        return url

async def   crawl(session, domain, url, depth):
    try:
        url = normalize_url(url)
        if depth > MAX_DEPTH:
            return

        async with lock:
            if url in visited:
                return
            visited.add(url)
            all_visited_urls.add(url) 
        async with semaphore:
            html = await fetch(session, url)
            if not html:
                return

            log_success(f"Crawled: {url} (depth={depth})")
            links = extract_links(domain, html)
            domain_netloc = urlparse(domain).netloc
            patterns = DOMAIN_PATTERNS.get(domain_netloc, [])

            for link in links:
                normalized = normalize_url(link)
                for pattern in patterns:
                    if re.search(pattern, normalized):
                        async with lock:
                            if normalized not in product_links.get(domain, set()):
                                product_links.setdefault(domain, set()).add(normalized)
                                log_product(normalized)
                await crawl(session, domain, normalized, depth + 1)
    except Exception as e:
        log_error(f"Error in crawl() for {url}: {e}")

async def run_crawler(domains):
    try:
        async with aiohttp.ClientSession() as session:
            tasks = [crawl(session, domain, domain, 0) for domain in domains]
            await asyncio.gather(*tasks)
    except Exception as e:
        log_error(f"Session error: {e}")
    finally:
        try:
            os.makedirs("output", exist_ok=True)
            final_output = {k: sorted(list(v)) for k, v in product_links.items()}
            with open("output/product_urls.json", "w") as f:
                json.dump(final_output, f, indent=2)
            log_success("✅ Crawling completed. Product URLs saved to output/product_urls.json")

            for domain, urls in final_output.items():
                log_info(f"{domain} → {len(urls)} product URLs")

            with open("output/product_urls.json", "w") as f:
                json.dump(sorted(list(all_visited_urls)), f, indent=2)
            log_success("✅ Visited URLs saved to output/product_urls.json")

        except Exception as e:
            log_error(f"Failed to write output files: {e}")


def load_domains_from_file(file_path="domains.txt"):
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except Exception as e:
        log_error(f"Failed to load domains from {file_path}: {e}")
        return []

if __name__ == "__main__":
    try:
        log_info("Starting the e-commerce crawler...")
        domains =  [
            "https://www.virgio.com/",
            "https://www.tatacliq.com/",
            "https://www.nykaafashion.com/",
            "https://www.westside.com/"
        ]
        asyncio.run(run_crawler(domains))
        log_info(" Crawler finished.")
    except Exception as e:
        log_error(f"Unhandled exception in main: {e}")
