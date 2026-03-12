import requests
import bs4

headers = {'User-Agent': 'ImageScraperBot/1.0'}

def find_image(soup, min_width=50):
    selectors_to_try = [
        "img[src*='.jpg']",
        "img[src*='.png']",
        "img[src*='.webp']",
        ".gallery img",
        ".image img",
        ".photo img",
        "figure img",
        "article img",
        "main img",
        "img"
    ]
      
    for selector in selectors_to_try:
        pic = soup.select(selector)
        real_image = []

        if not pic:
            continue

        for img in pic:
            src_options = img.get("srcset")
            if src_options:
                 src = src_options.split(",")[-1].strip().split(" ")[0]
            else:
                src = img.get("src") or img.get("data-src") or img.get("")
            width = img.get("width")

            if not src or any(x in src.lower() for x in ["icon","logo","pixel","tracker"]):
                continue

            if width and width.isdigit():
                if int(width) <= min_width:
                    continue
                if src.startswith(("//")):
                    src = "https" + src
                    
                if src.startswith(("https")):    
                    real_image.append(src)
        if list(set(real_image)):
            print(f"Using: {selector}")
            return real_image 
    return []
            

url = input("Enter URL to scrape: ").strip()

try:
    res = requests.get(url, headers=headers)
    res.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching URL: {e}")
    exit(1)

soup = bs4.BeautifulSoup(res.text, "lxml")

images = find_image(soup, 50)
if not images:
    print("No images found.")
else:
    for image_url in images:
        print(image_url)
     
