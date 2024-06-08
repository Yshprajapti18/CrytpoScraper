from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

class CoinMarketCap:
    BASE_URL = "https://coinmarketcap.com/currencies/"
    
    def __init__(self,coin_name) -> None:
        options = Options()
        options.binary_location = r"/usr/bin/google-chrome"
        options.add_argument("user_agent=mike")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)

        self.coin_name = coin_name

    def __del__(self):
        self.driver.quit()
    
    def get_coin_page(self):
        COIN_URL = self.BASE_URL + self.coin_name.lower() 
        self.driver.get(COIN_URL)
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        self.driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
        time.sleep(1)
        content = self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        return content

    def parse_coin_page(self,content):
        soup = BeautifulSoup(content, features="lxml")
        data = {
            "price": self.extract_price(soup),
            "price_change": self.extract_price_change(soup),
            "market_cap": self.extract_market_cap(soup),
            "market_cap_rank": self.extract_market_cap_rank(soup),
            # "volume": self.extract_volume(soup),
            # "volume_rank": self.extract_volume_rank(soup),
            # "volume_change": self.extract_volume_change(soup),
            # "circulating_supply": self.extract_circulating_supply(soup),
            # "total_supply": self.extract_total_supply(soup),
            # "diluted_market_cap": self.extract_diluted_market_cap(soup),
            # "contracts": self.extract_contracts(soup),
            # "official_links": self.extract_official_links(soup),
            # "socials": self.extract_socials(soup),
        }
        return data

    def extract_price(self,soup):
        return (soup.find("span",class_="sc-d1ede7e3-0 fsQm base-text").text.strip('$').replace(',',''))

    def extract_price_change(self,soup):
        return (soup.find("p",class_="sc-71024e3e-0 sc-58c82cf9-1 ihXFUo iPawMI").text.strip('%')) 

    def extract_market_cap(self,soup):
        return (soup.find("dd",class_="sc-d1ede7e3-0 hPHvUM base-text").text.strip('$').replace(',','')) 
    
    def extract_market_cap_rank(self,soup):
        return (soup.find("span",class_="text slider-value rank-value").text.strip('#'))

    # def extract_volume(self,soup):
    #     return (soup.find("span",class_="sc-d1ede7e3-0 hPHvUM base-text").text.strip('$').replace(',',''))

    # def extract_volume_rank(self,soup):
    #     return int(soup.find("span",class_="text slider-value rank-value").text.strip('#'))
    
    def scrape(self):
        content = self.get_coin_page()
        data = self.parse_coin_page(content)
        return data


















































