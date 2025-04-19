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
ecom-crawler/
│
├── crawler/
│   ├── main.py           # Main crawler logic
│   ├── fetcher.py        # Handles async HTTP requests with retry logic
│   ├── parser.py         # Extracts and filters links
│   └── config.py         # Contains domain-specific product URL patterns
│
├── output/
│   └──  product_urls.json # Final collected product URLs and all visited URLs
│   
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Requirements

- Python 3.8+
- Internet connection

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ecom-crawler.git
cd ecom-crawler
```

### 2. Create and Activate Virtual Environment

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🕷️ Run the Crawler

### Run with default domains:

```bash
python crawler/main.py
```

### Optional: Run with a custom domain list

Add your domains to a file named `domains.txt`, one per line, then run:

```bash
python crawler/main.py --file domains.txt
```

---

## 📤 Output

The crawler will generate two files under `output/`:

- `product_urls.json`: All discovered product URLs grouped by domain and visited by the crawler.

Example:
```json
{
  "https://www.example.com": [
    "https://www.example.com/product/abc123",
    ...
  ]
}
```

You’ll also get console logs for successful crawls, discovered products, and errors.

---

## 🛠️ Customizing

You can update `config.py` to add domain-specific product URL patterns:

```python
DOMAIN_PATTERNS = {
    "example.com": [r"/product/.*", r"/item/.*"]
}
```

These regex patterns help the crawler identify product pages more accurately.

---

## 📌 Notes

- The crawler respects internal links only.
- Uses a depth limit (`MAX_DEPTH`) to prevent infinite loops.
- Includes structured error handling and retry logic.

---

## 👤 Author

Built with care by Prajwal Singh.  