import requests
from bs4 import BeautifulSoup

def search_myntra(product_name):
    search_url = f"https://www.myntra.com/{product_name.replace(' ', '-')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find("h3", {"class": "product-brand"})
    price = soup.find("span", {"class": "product-discountedPrice"})

    if product and price:
        return {
            "platform": "Myntra",
            "name": product.text.strip(),
            "price": float(price.text.replace("₹", "").replace(",", ""))
        }
    return {"error": "Product not found"}
