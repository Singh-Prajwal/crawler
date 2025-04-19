# E-Commerce Product URL Crawler 🛒

This is a fast, scalable, and reliable asynchronous web crawler designed to extract product page URLs from multiple e-commerce websites. It supports different domain structures and handles edge cases to ensure high performance and accuracy.

---

## 📦 Features

- ✅ Discovers product URLs using domain-specific patterns
- ⚙️ Handles asynchronous crawling with controlled concurrency
- 🧠 Smart internal link following (avoids external links)
- 🚀 Designed for large websites with deep navigation
- 📀 Outputs clean JSON with all product and visited URLs
- ♻️ Retry logic for failed requests
- 🧱 Handles broken HTML, timeouts, and inconsistent structures

---

## 📁 Project Structure

```
crawler/
├── config.py         # URL patterns per domain
├── fetcher.py        # Handles HTTP requests with retries
├── parser.py         # Extracts internal links from HTML
├── main.py           # Core crawler logic
└── output/
    ├── product_urls.json   # Collected product links
    └── visited_urls.json   # All visited URLs
```

---

## 🚀 How to Run

1. **Clone the repo**

```bash
git clone https://github.com/Singh-Prajwal/crawler.git
cd ecom-crawler
```

2. **(Optional) Add your domains**

By default, `main.py` includes 4 example domains. You can edit them in the `domains` list.

```python
domains = [
    "https://www.virgio.com/",
    "https://www.tatacliq.com/",
    "https://www.nykaafashion.com/",
    "https://www.westside.com/"
]
```

3. **Install requirements**

```bash
pip install -r requirements.txt
```

4. **Run the crawler**

```bash
python crawler/main.py
```

---

## 📤 Output

- `product_urls.json`: All discovered product URLs grouped by domain and visited by the crawler.

---

## 🛠️ Customizing

You can update `config.py` to add domain-specific URL matching patterns:

```python
DOMAIN_PATTERNS = {
    "example.com": [r"/product/.*", r"/item/.*"]
}
```

These patterns help the crawler know which URLs are likely to be product pages.

---

## 📌 Notes

- The crawler respects internal links only (it won't crawl external sites).
- It uses a depth limit (`MAX_DEPTH`) to avoid infinite loops or unnecessary crawling.
- Error handling and retry logic are built in to make it resilient against flaky pages or failed requests.

---

## 👤 Author

Built with care by Prajwal Singh.  