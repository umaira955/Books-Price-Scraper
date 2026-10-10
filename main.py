import csv
import requests
from bs4 import BeautifulSoup
# print(soup.prettify())

with open("Book.csv" , "w" , newline="", encoding="utf-8") as B:
    writer = csv.writer(B)
    writer.writerow(["Title" , "Price" , "Availability" , "Links" , "rating"])
    for page_num in range(1, 51):
        if page_num == 1:
            url = "https://books.toscrape.com/"
        else:
            url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content , "html.parser")
            for book in soup.find_all("article", class_="product_pod"):
                title = book.find("h3").find("a").get("title")
                price = book.find("p" , class_ = "price_color").get_text()
                availability = book.find("p" , class_ = "instock availability").get_text(strip=True)
                link = book.find("h3").find("a").get("href")
                rating = book.find("p", class_="star-rating").get("class")[1]
                writer.writerow([title , price , availability , link , rating])
        else:
            print("Request failed!!")
print("CSV created successfully!!!")
        