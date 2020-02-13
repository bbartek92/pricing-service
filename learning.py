import re
import requests
from bs4 import BeautifulSoup


def load_prince(url, tag_name, query) -> float:
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find(tag_name, query)
    # print(element)
    string_price = element.get_text().strip()
    print(string_price)
    pattern = re.compile(r"(\d+,?\d*\.\d\d)")
    match = pattern.search(string_price)
    print(match)
    found_price = match.group()
    without_commas = found_price.replace(",", "")
    price = float(without_commas)
    return price

url_ = "https://www.johnlewis.com/2019-apple-ipod-touch-32gb/space-grey/p4185402"
tag_name_ = "p"
query_= {"class": "price price--large"}

my_price = load_prince(url_, tag_name_, query_)
print(my_price)
