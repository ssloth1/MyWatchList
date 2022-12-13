# James Bebarski
# December 13, 2022
# CS 5003: Recitation for CS 5001
# Final Project
# testStorage.py

from Storage import Storage
from mywatchlist import dictAssembly


def main():
    
    # Instructions:
    # Use the myitemstes.txt file as a playground for testing Storage. 
    # If you need some of my provided items and associated links use "example-items.txt"
    # Additionally, for complete files feel free to copy as needed from "my-items-testing-backup.txt"
    # Feel free to try your own items and links from Newegg, Microcenter, and Bestbuy.
    
    # Final note, when you exit the text document make sure your cursor is on a new row, 
    # otherwise if you try to add an item it will add it to the same row as another dictionary.
    # If you want to check if your test had an effect feel free to just check the text document directly.
    # You may also use Storage's methods to check the dictionary's, keys, and values.
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Keep the below line uncommented for all tests. 
    test_object = Storage('my-items-testing-file.txt')
    
    
    # TEST addItem
    
    '''
    # See files before adding.
    print("\n")
    test_object.displayItems()
    print("\n")
    
    key1 = str(input("Enter your test item.\n>>>"))
    newegglink1 = str(input("Enter the newegg link.\n>>> "))
    microcenterlink1 = str(input("Enter the microcenter link.\n>>> "))
    bestbuylink1 = str(input("Enter the BestBuy link.\n>>> "))
    test_dict1 = dictAssembly(key1, newegglink1, microcenterlink1, bestbuylink1)
    test_object.addItem(test_dict1)
    
    # See dictionaries after filing.
    print("\n")
    test_object.displayItems()
    print("\n")
 
    # For Good Tests Follow the prompts and elements when requested.
    
    # For Bad Tests:
    # - Try adding an incorrect item name or no name at all.
    # - Try adding an incorrect url in the wrong place or no url at all. 
    #   - Most of these issues are rectified in the main file by requiring that the beginning of the input begins with the correct site.
    
    '''
    
    # TEST removeItem
    
    '''
    # See files before removing .
    print("\n")
    test_object.displayItems()
    print("\n")
    
    # TEST removeItem
    key2 = str(input("Enter your test item for removal.\n>>>"))
    test_object.removeItem(key2)
    
    # See dictionaries after filing.
    print("\n")
    test_object.displayItems()
    print("\n")
 
    # For Good Tests - make sure you are as specific as possible with your inputs. 
    
    # For Bad Tests:
    # - ENTERING NOTHING OR UNNECESSARY SPACES REMOVES ALL CONTENT FROM THE FILE. 
    # - If you are not specific enough, you may delete unintended items. 
    #   - For example, if you enter >>> Corsair, it will delete all items that have the name Corsair.
    #   - Additionally, adding and removals are case-sensitive. So if you initially stored an item as >>> AMD Ryzen 7 5700X
    #   - If try to remove the item by entering >> amd ryzen 5700X, it won't work. 
    
    '''
    
    # TEST displayItems
    
    '''
    
    print("\n")
    test_object.displayItems()
    print("\n")
    
    # Good Tests - Either with addItem or removeItem function, or manually editing the save file, change the file
    #              verify changes made using this function.
    # Bad Tests - You may try running the code without a test file altogether. 
    
    '''
    
    # TEST getLinks
    
    '''
    # This function returns a value associated with an entered item(key), the value is a list of links.
    # This function provides links to the Scraper constructor. 
    
    key3 = str(input("Enter your test item to return links list.\n>>>"))
    print(test_object.getLinks(key3))
    
    # For Good Tests - make sure you are as specific as possible with your inputs. 
    
    # For Bad Tests: 
    # - If you are not specific enough, you may return unintended links from items. 
    #   - For example, if you enter >>> Corsair, it will return all links associated with keys that have Corsair in their name.
    #   - Inputs should be case-sensitive. So if you initially stored an item as >>> AMD Ryzen 7 5700X
    #   - If try to pull the item by entering >> amd ryzen 5700X, it won't return any links. 
    #   - Empty input returns all links associated with keys.
    
    '''
    
    # TEST displayLinks
    
    '''
    # When a user calls displayLinks it returns all links associated with an item(key).
    
    key4 = str(input("Enter your test item to print links associated with an item.\n>>>"))
    test_object.displayLinks(key4)
    
    # For Good Tests - make sure you are as specific as possible with your inputs. 
    
    # For Bad Tests: 
    # - If you are not specific enough, you may return unintended links from items. 
    #   - For example, if you enter >>> Corsair, it will return all links associated with keys that have Corsair in their name.
    #   - Inputs should be case-sensitive. So if you initially stored an item as >>> AMD Ryzen 7 5700X
    #   - If try to pull the item by entering >>> amd ryzen 5700X, it won't return any links. 
    #   - Empty input returns all links associated with keys.
    '''
    
    
if __name__ == '__main__':
    main()