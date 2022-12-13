# James Bebarski
# December 13, 2022
# CS 5003: Recitation for CS 5001
# Final Project
# testScrape.py

from Scrape import Scrape 

# PLEASE DO NOT RUN MORE THAN ONE TEST AT A TIME. 
# BE COURTEOUS TO THE SITES AND DO NOT SEND UNNESSARY SCRAPE REQUESTS.

def main():
    # GOOD TESTS
    
    # Good Test1 - Scrape Intel Core i9-13900K:
    '''
    goodtest1 = Scrape("Intel Core i9-13900K")
    
    print("Testing individual scrape methods...")
    print("scrapeNewegg- ", goodtest1.scrapeNewegg())
    print("scrapeMicrocenter- ", goodtest1.scrapeMicrocenter())
    print("scrapeBestBuy- ", goodtest1.scrapeBestBuy())
    
    print("\nTesting displayAllPrices...")
    goodtest1.displayAllPrices()
    
    print("\nAs of 12/11/2022, actual prices should be:")
    print("Newegg Price: $629.99")
    print("Microcenter Price: $599.99")
    print("BestBuy Price: $649.99")
    
    print("\nAt time of testing if there is a mismatch, check to page and see if the price has changed.")
    print("It might be best to refer to pasted links on example-items.txt")
   
    '''
    
    # Good Test2 - Scrape Corsair Vengence RGB Pro 32 GB RAM (2x16GB):
    '''
    goodtest2 = Scrape("Corsair Vengence RGB Pro 32 GB RAM (2x16GB)")
    
    print("Testing individual scrape methods...")
    print("scrapeNewegg- ", goodtest2.scrapeNewegg())
    print("scrapeMicrocenter- ", goodtest2.scrapeMicrocenter())
    print("scrapeBestBuy- ", goodtest2.scrapeBestBuy())
    
    print("\nTesting displayAllPrices...")
    goodtest2.displayAllPrices()
    
    print("\nAs of 12/11/2022, actual prices should be:")
    print("Newegg Price: $115.99")
    print("Microcenter Price: $104.99")
    print("BestBuy Price: $117.99")
    
    print("\nAt time of testing if there is a mismatch, check to page and see if the price has changed.")
    print("It might be best to refer to pasted links on example-items.txt")
    '''
    
    # Good Test 3 - Partial name input. 
    # Notes: Entered Ryzen 9, instead of full name - AMD Ryzen 9 5900X
    '''
    goodtest3 = Scrape("Ryzen 9")
    
    print("Testing individual scrape methods...")
    print("scrapeNewegg- ", goodtest3.scrapeNewegg())
    print("scrapeMicrocenter- ", goodtest3.scrapeMicrocenter())
    print("scrapeBestBuy- ", goodtest3.scrapeBestBuy())
    
    print("\nTesting displayAllPrices...")
    goodtest3.displayAllPrices()
    
    print("\nAs of 12/11/2022, actual prices should be:")
    print("Newegg Price: $349.99")
    print("Microcenter Price: $329.99")
    print("BestBuy Price: $349.00")
    
    print("\nAt time of testing if there is a mismatch, check to page and see if the price has changed.")
    '''
    
    # BAD TESTS
    
    # Bad Test 1 - Input not specific enough. 
    
    '''
    badtest1 = Scrape("Ryzen") # Note, user actually wants to search for Ryzen 9 prices.
    
    print("Testing individual scrape methods...")
    print("scrapeNewegg- ", badtest1.scrapeNewegg())
    print("scrapeMicrocenter- ", badtest1.scrapeMicrocenter())
    print("scrapeBestBuy- ", badtest1.scrapeBestBuy())
    
    print("\nTesting displayAllPrices...")
    badtest1.displayAllPrices()
    
    print("\nAs of 12/11/2022, actual prices should be:")
    print("Newegg Price: $349.99")
    print("Microcenter Price: $329.99")
    print("BestBuy Price: $349.00")
    
   # Note: If user is not specific enough, the program will pull the first dictionary that contains the string "Ryzen" as a key.
   # In this test case, in the given myitems.txt file Ryzen 7 is the first row that would be detected with "Ryzen" in it's key.
   # If you were to enter the full name of the Ryzen 9 or even a partial that distinguishes the two keys, the correct item will get parsed.
   
   '''
   
   # Bad Test 2 - No input, just pressed enter for input.
   
    '''
    badtest2 = Scrape("")
    
    print("Testing individual scrape methods...")
    print("scrapeNewegg- ", badtest2.scrapeNewegg())
    print("scrapeMicrocenter- ", badtest2.scrapeMicrocenter())
    print("scrapeBestBuy- ", badtest2.scrapeBestBuy())
    
    print("\nTesting displayAllPrices...")
    badtest2.displayAllPrices()
    
    print("\nAs of 12/9/2022, actual prices should be:")
    print("Newegg Price: ???")
    print("Microcenter Price: ???")
    print("BestBuy Price: ???")
    
    # Notes: The program will just search for the first dictionary with "", meaning it will probably just return the first dictionary in "myitems.txt". 
   
    '''
    
    # Bad Test 3 - Whole item or a link does not exist in dictionary.
    
    '''
    badtest3 = Scrape("thing")
    
    print("Testing individual scrape methods...")
    print("scrapeNewegg- ", badtest3.scrapeNewegg())
    print("scrapeMicrocenter- ", badtest3.scrapeMicrocenter())
    print("scrapeBestBuy- ", badtest3.scrapeBestBuy())
    
    print("\nTesting displayAllPrices...")
    badtest3.displayAllPrices()
    
    print("\nAs of 12/9/2022, actual prices should be:")
    print("Newegg Price: ???")
    print("Microcenter Price: ???")
    print("BestBuy Price: ???")
    
    # Notes: Will return a Attribute Error".
    '''
    
    
if __name__ == '__main__':
    main()

