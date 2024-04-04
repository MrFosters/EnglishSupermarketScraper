import bs4
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# page links
name_list = []
price_list = []
category_list = []

links = ["https://bevasarlas.tesco.hu/groceries/hu-HU/shop/friss-grill-termekek/all?page=02",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/zoldseg-gyumolcs/all?page=06",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/tejtermekek-tojas/all?page=15",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/pekaru/all?page=05",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/hus-hal-felvagott/all?page=13",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/alapveto-elelmiszerek/all?page=54",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/specialis-es-egeszseges-taplalkozas/all?page=18",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/fagyasztott-elelmiszerek/all?page=10",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/italok/all?page=22",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/alkohol/all?page=20",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/haztartas/all?page=25",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/szepsegapolas/all?page=50",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/babaapolas/all?page=11",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/kisallat/all?page=10",
         "https://bevasarlas.tesco.hu/groceries/hu-HU/shop/otthon-hobbi/all?page=23"]


links2 = ["https://bevasarlas.tesco.hu/groceries/hu-HU/shop/friss-grill-termekek/all?page=01"]


# site looping
category_pages = []

for i in links:
    page = i[-2:]
    link = i[:-2]
    item_count = "&count=48"

    for element in range(int(page), 0, -1):
        combined_link = link + str(element) + item_count
        category_pages.append(combined_link)

    # print(category_pages)

# print(len(category_pages))
input_link = "https://bevasarlas.tesco.hu/groceries/en-GB/shop/bbq/all?include-children=true&page=01&count=48"


def anti_bot_scraping(current_link):

    driver_path = "C:/chromedriver.exe"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    options = Options()
    options.binary_location = brave_path
    options.headless = False
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get(current_link)

    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#tile-2004010090073 > div.product-details--wrapper > div.styles__StyledProductDetailsContent-dvv1wj-5.ddRSrq > div:nth-child(1) > a > span.styled__Text-sc-1xbujuz-1.fyDIEo.beans-link__text > span")))

    source = driver.page_source
    driver.quit()

    html_text = source
    parsed_html = bs4.BeautifulSoup(html_text, "lxml").find_all("li", {"class": "product-list--list-item"})

    items = BeautifulSoup(str(parsed_html), "lxml").find_all("span", {"styled__Text-sc-1xbujuz-1 ldbwMG beans-link__text"})

    prices = BeautifulSoup(str(parsed_html), "lxml").find_all("p", {"styled__StyledHeading-sc-119w3hf-2 jWPEtj styled__Text-sc-8qlq5b-1 lnaeiZ beans-price__text"})

    for k in items:
        a = k.getText(strip=True)
        name_list.append(a)
        print(a)

    for o in prices:
        u = o.getText(strip=True)
        price_list.append(u)
        print(u)

    # for c in item_category_name:
    #     t = c.getText(strip=False)
    #     category_list.append(t)
    #     print(item_category_name)


    # print(parsed_html.find_all("p", "styled__StyledHeading-sc-119w3hf-2 jWPEtj styled__Text-sc-8qlq5b-1 lnaeiZ beans-price__text"))

    # print(fine_price)


for i in category_pages:
    anti_bot_scraping(i)

with open('Tesco_Scrape_19_12_22.csv', 'w', encoding="utf-8 ", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(zip(name_list, price_list))
