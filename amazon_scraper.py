import requests
from bs4 import BeautifulSoup

def search_amazon(product_name):
    search_url = f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find("span", {"class": "a-size-medium"})
    price = soup.find("span", {"class": "a-price-whole"})

    if product and price:
        return {
            "platform": "Amazon",
            "name": product.text.strip(),
            "price": float(price.text.replace(",", ""))
        }
    return {"error": "Product not found"}
