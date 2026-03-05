import time
import os
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from database import insert_product
from config import SEARCH_QUERY, PAGES_TO_SCRAPE


def run_scraper():

    os.makedirs("images", exist_ok=True)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.amazon.in")

    time.sleep(3)

    search = driver.find_element(By.ID,"twotabsearchtextbox")
    search.send_keys(SEARCH_QUERY)
    search.submit()

    time.sleep(4)

    for page in range(PAGES_TO_SCRAPE):

        print("Scraping Page:", page+1)

        products = driver.find_elements(By.XPATH,"//div[@data-component-type='s-search-result']")

        for product in products:

            try:
                name = product.find_element(By.XPATH,".//h2").text
            except:
                name = "N/A"

            try:
                price = product.find_element(By.XPATH,".//span[@class='a-price-whole']").text
                price = int(price.replace(",",""))
            except:
                price = 0

            try:
                rating = product.find_element(By.XPATH,".//span[@class='a-icon-alt']").text
            except:
                rating = "No rating"

            try:
                link = product.find_element(By.XPATH,".//h2/a").get_attribute("href")
            except:
                link = ""

            try:
                image_url = product.find_element(By.XPATH,".//img").get_attribute("src")

                img_data = requests.get(image_url).content

                safe_name = name.replace("/","").replace("\\","")

                file_name = f"images/{safe_name[:25]}.jpg"

                with open(file_name,"wb") as f:
                    f.write(img_data)

            except:
                file_name = ""

            insert_product(name,price,rating,link,file_name)

        try:
            next_btn = driver.find_element(By.XPATH,"//a[contains(@class,'s-pagination-next')]")
            next_btn.click()
            time.sleep(4)
        except:
            break

    driver.quit()