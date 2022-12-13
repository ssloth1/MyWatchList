-MyWatchlist- 

I. Description:
A personalized way to store items of interest, and parse prices from saved links to the associated item. 

II. Important Tips:

   i. Get an item price. 
      a. When requesting an item to parse, be as specific as possible. For example, if you have multiple items with the name 
         "Ryzen" and you type in only "Ryzen it will parse the first item with those exact characters it sees in your save file. 

   ii. Add New Item. 
      a. Again be as specific as possible. Ensure that you always follow the prompts.
         Enter the item name first, link to the item on Newegg second, Micro Center third, and then Best Buy.

   iii. Remove Item.
      a. Take very special care when removing an item, and again be very specific about what item you want to remove. 
         Stored items are case sensitive so if you want to remove "Intel i9" entering intel i9 will not remove the item. 
      b. DO NOT ENTER SINGLE CHARACTER or EMPTY SPACES, this will delete the entire save file!!!!

II. Required Modules: 
This project was written in a conda environment.
To limit any errors it's recommended to run the code in a conda environment.

ast (Abstract Syntax Trees)
 - Built-in Python Language Service

Beautiful Soup 4.11.1 (supports Python 3.6+)
- Recommended to import directly from Anaconda package, in a conda environment. 
- For pip install run the following command: 
  pip install beautifulsoup4 

Requests 2.28.1 (supports Python 3.7+)
- Recommended to import directly from Anaconda package, in a conda environment.
- For pip install run the following command: 
  pip install requests 

Browser Support: 
Works best with Chrome or Firefox, and an ad-blocker extension. 

III. Files

i. Main Files
   
   a. mywatchlist.py
      The main file for the project. Run the program from this file. 

   b. Scrape.py
      Contains the Scrape class and associated methods for scraping prices from Newegg, Micro Center, and Best Buy.

   c. Storage.py
      Contains the Storage class and associated methods for manipulating the program save file. 

   d. my-items.txt
      The main save file for the project. This is the file that contains rows of dictionaries in the following format:
      {example_item_A : [link_to_item_on_Newegg, link_to_item_on_MicroCenter, link_to_item_on_BestBuy]}
      This file should come preloaded with some dictionaries. 
      
      Ensure that within the Storage Constructor:
      self.my_storage = Storage('my-items.txt')

      Additionally within mywatchlist.py make sure that:
      my_storage = Storage('my-items.txt') is always the first line within the main() function.

      To change the save file to a different .txt file, you insert the new .txt file into those above two locations.

ii. Test Files

   a. testScrape.py
      test cases for the Scrape class and associated methods.

   b. testStorage.py
      test cases for the Storage class and associated methods. 

   c. my-items-testing-file.txt 
      main save file for testing of the testScrape and testStorage files. 

   d. my-items-testing-backup.txt
      backup of the testing file, exists for copying and pasting test cases to the my-items-testing-file.txt

iii. Misc Files

    a. my-items.backup.txt 
       A copy of my main save file, this does not back up on its own. 

    b. example_item.txt
       A list of all the items in the main save file and test files, but not in the form of a dictionary. 

IV. Credits

    Special thanks to Dr. Lindsay Jamieson and Northeastern University






