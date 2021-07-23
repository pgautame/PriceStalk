import requests
from bs4 import BeautifulSoup
import smtplib

# URL = input("Enter URL : ")
# budget = float(input("Enter ALert Budget : "))
# toemail = input("Enter your email ID : ")
headers = {
    "User-Agent":
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.16 Safari/537.36 Edg/80.0.361.9'
}


def check_price_flip(URL,budget,toemail):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("span", {"class": "B_NuCI"}).get_text()
    price = soup.find("div", {"class": "_30jeq3 _16Jk6d"}).get_text()

    new_price = price[1:]
    array_price = new_price.split(',')
    converted_price = float((price[1:]).replace(",", ""))
   # converted_price = float(array_price[0] + array_price[1]+array_price[2])
    if (converted_price < budget):
        send_mail(toemail,URL)
    print(converted_price)
    print(title)
    return converted_price


def send_mail(toemail,URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('scraperamazonflipkart@gmail.com', 'hdbuscxtxxsqyuvh')
    subject = 'Price fell down! DO NOT REPLY.This is a System-generated mail'
    body = 'Check the Flipkart Link ' + URL

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail('scraperamazonflipkart@gmail.com', toemail, msg)
    print("Email has been sent")
    server.quit()


# check_price()
