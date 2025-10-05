import requests as req
from bs4 import BeautifulSoup

class MobileFromFlipkart:
    def __init__(self,budget,rating,brand):
        self.budget = budget
        self.rating = rating
        self.brand = brand

        self.url = f"https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.rating%255B%255D%3D{rating}%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D{budget}&p%5B%5D=facets.brand%255B%255D%3D{brand}" if brand else f"https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.rating%255B%255D%3D{rating}%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D{budget}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/140.0.0.0 Safari/537.36"}

        self.response = req.get(url = self.url , headers=self.headers).text
        self.soup = BeautifulSoup(self.response , "lxml")

    def display(self):
        print(self.url)
        print()

        all_details = self.soup.find_all("div" , {"class" : "yKfJKb row"})
        for i in all_details:
            print( i.find("div" , {"class" : "KzDlHZ" }).text , end=" -- " )
            print( i.find("div" , {"class" : "XQDdHH"}).text , end= " price -- " )
            print( i.find("div" , {"class" : "Nx9bqj _4b5DiR"}).text)
            print()

budget_i = input("Enter Budget : " ).strip()
rating_i = input("Enter ratings out of 5 : ").strip()
brand_i = input("Enter brand : ").strip().upper()

obj = MobileFromFlipkart(budget_i,rating_i,brand_i)
obj.display()
