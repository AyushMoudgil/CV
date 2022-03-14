import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJFDW/ref=sr_1_6?pf_rd_i=1388921031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=e1b534f1-3276-56a6-91b1-814616b41341&pf_rd_r=FY0ANF7FV6ANTHA9MVZR&pf_rd_s=merchandised-search-11&pf_rd_t=101&qid=1562742381&refinements=p_n_feature_browse-bin%3A6631672031%7C6631673031&rw_html_to_wsrp=1&s=electronics&sr=1-6'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[2:7].replace(',',''))
    if (converted_price<1499):
        send_mail()
    print(converted_price)
    print(title.strip())

    if(converted_price>1399):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('abhiakashona@gmail.com', 'derdacvzufwkbpsu')
    
    subject = 'Price Fell Down!'
    body = 'Check the Amazon link https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJFDW/ref=sr_1_6?pf_rd_i=1388921031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=e1b534f1-3276-56a6-91b1-814616b41341&pf_rd_r=FY0ANF7FV6ANTHA9MVZR&pf_rd_s=merchandised-search-11&pf_rd_t=101&qid=1562742381&refinements=p_n_feature_browse-bin%3A6631672031%7C6631673031&rw_html_to_wsrp=1&s=electronics&sr=1-6'

    msg = f"Subject: {subject} \n{body}"

    server.sendmail(
        'ayushrules37@gmail.com',
        'ayushrules37@gmail.com',
        msg)
    print("Hey email has been sent!!")

    server.quit()
         

check_price()



