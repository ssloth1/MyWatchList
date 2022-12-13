# James Bebarski
# December 13, 2022
# CS 5003: Recitation for CS 5001
# Final Project
# Scrape.py

import requests
from bs4 import BeautifulSoup
from Storage import Storage

class Scrape:
    
    def __init__(self, item):
        '''
        PARAMETERS:
            - self
            - item - the item to be scraped (str).
        
        ATTRIBUTES: 
            - my.storage - the storage object (instance of Storage Class within Scrape)
            - self.my_links - the list of links of an item to be scraped.
            - self.newegglink - the Newegg link.
            - self.microcenterlink - the Microcenter link.
            - self.bestbuylink - the BestBuy link.
        '''
       
        if not isinstance(item, str):
            raise TypeError("Invalid type, please input a .txt file to scrape from.")
        
        self.my_storage = Storage('my-items.txt') # Instance of Storage class, allows me to to use the getLinks method to return a list of requested links.
        
        try:
            self.my_links = self.my_storage.getLinks(str(item)) # Returns a list of links.
            self.newegglink = str(self.my_links[0]) # First list element is Newegg link.
            self.microcenterlink = str(self.my_links[1]) # Second list element is Microcenter link.
            self.bestbuylink = str(self.my_links[2]) # Third list element is BestBuy link.
        
        except IndexError as error:
            print(error,": That item does not exist, parsing tool could not pull a link.")
            

            
    # __str__ method for Scrape class.
    def __str__(self):
        '''
        class Scrape
            - __str__ method 
        '''
        print(self.my_storage)
        print(self.my_links)
        print(self.newegglink)
        print(self.microcenterlink)
        print(self.bestbuylink)

    # Scraping method for Newegg links.
    def scrapeNewegg(self):
        '''
        class Scrape
            Description: 
            - Scrapes newegg links. 
        
        '''
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        page = requests.get(self.newegglink, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        mysoup = soup.find_all(text="$")
        parent = mysoup[0].parent 
        strong_tag = (parent.find("strong"))
        sup_tag = (parent.find("sup"))
        price = strong_tag.string + sup_tag.string
        if "," in price:
            price = price.replace(",", "")
        return price

    # Scraping method for Microcenter links
    def scrapeMicrocenter(self):
        '''
        class Scrape
            Description:
            - Scrapes Microcenter link for item price.
        '''
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        page = requests.get(self.microcenterlink, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        parseprice = soup.find("span", id="pricing")
        rawprice = "".join(i for i in str(parseprice) if i.isdigit())
        price_list = list(rawprice)
        price_list.insert(-2, ".")
        price = "".join(price_list)
        return price

    # Scraping method for BestBuy links.
    def scrapeBestBuy(self):
        '''
        class Scrape
            Description:
            - Scrapes BestBuy link for item price. 
        '''
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        page = requests.get(self.bestbuylink, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        parseprice = soup.find("span", {'class': "sr-only"})
        rawprice = "".join(i for i in str(parseprice) if i.isdigit())
        price_list = list(rawprice)
        price_list.insert(-2, ".")
        price = "".join(price_list)
        return price
    
    # Scrapes all links associated with an item, and prints results to the terminal. 
    def displayAllPrices(self):
        '''
        class Scrape
            Description: 
            - Displays all requested prices for an item.
        '''
        print("Price on Newegg: $", self.scrapeNewegg())
        print("Price on Microcenter: $", self.scrapeMicrocenter())
        print("Price on BestBuy: $", self.scrapeBestBuy())






