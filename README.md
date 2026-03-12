# Image Scraper

A Python web scraper that extracts image URLs from any webpage.

## Features
- Tries multiple CSS selectors to find images
- Handles `srcset` attributes for responsive images
- Filters out icons, logos, and tracking pixels
- Skips images below a minimum width threshold
- Error handling for failed requests

## Requirements
- Python 3.x
- Install dependencies:
```bash
pip install requests beautifulsoup4 lxml
```

## Usage
```bash
python image_scraper.py
```
Enter a URL when prompted. The script will print all image URLs found.

## Example Output
```
Enter URL to scrape: https://example.com
Using: img[src*='.jpg']
https://example.com/images/photo1.jpg
https://example.com/images/photo2.jpg
```

## Disclaimer
Only scrape websites that permit it. Check a site's `robots.txt` 
and terms of service before scraping.
