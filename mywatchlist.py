# James Bebarski
# December 13, 2022
# CS 5003: Recitation for CS 5001
# Final Project
# mywatchlist.py


from Storage import Storage
from Scrape import Scrape
import os

# When adding a new item, this function assembles user_inputs into a dictionary, which gets stored in myitems.txt. 
def dictAssembly(item_name, neweggurl, microcenterurl, bestbuyurl):
   item_dictionary = {str(item_name): [str(neweggurl), str(microcenterurl), str(bestbuyurl)]}
   return item_dictionary

   
def main(): 
   # Initializes instance of Storage class, loads storage file. 
   my_storage = Storage('my-items.txt') # NOTE Please ensure that all your program files are in the same directory.
   
   # Displays current version of program. 
   print("MyWatchlist v1.0.")
   
   main_menu = True
   while main_menu == True: 
      
      # MAIN MENU INSTRUCTIONS
      prompt = "\nMAIN MENU\nEnter 1 to get an item price.\nEnter 2 to enter a new item.\nEnter 3 to remove an item.\nEnter 4 to quit."
      print(prompt)
      
      # MAIN MENU INPUT
      response = int(input("\n>>> "))
      while not str(response).isnumeric():
         response = int(input("Please enter a valid menu item\n>>> "))
      
      # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
      
      # 1) GET ITEM PRICE
      if response == 1:
         
         # Prompts user to enter the item they want to parse prices for. User can also enter 1 to display all items that exist for price parsing.
         sub_menu1 = True
         while sub_menu1 == True:
            item = str(input("\nEnter the name of the item you want to search.\nNOTE: Please be as specific as possible!\nPress 1 to display saved items.\n>>> "))
            
            # Displays all stored items when the user inputs "1". Then prompts user to input the item they want to parse prices for. 
            while item == "1":
               print("\nYour saved items:\n")
               my_storage.displayItems()
               item = str(input("\nEnter the name of the item you want to search.\nPress 1 to display saved items.\n>>> "))
            
            # Inputs the requested item into the Scrape class and creates an instance of the Scrape class. Program then calls displayAllPrices method to display prices for the user.
            my_scrape = Scrape(item)
            print("\nparsing prices....\n")
            my_scrape.displayAllPrices()
            
            # Checks if the user wants to display the links for the item they just parsed.
            display_links = True 
            while display_links == True:
               display_urls = str(input("\nPress 1 to display the links, press any other key to go back to the previous menu.\n>>> "))
               
               # Displays the links and goes back to previous menu.
               if display_urls == "1":
                  my_storage.displayLinks(item)
                  display_links = False
               
               # Goes back to previous menu.
               else:
                  display_links = False
                  
            # Asks the user if they want to parse prices for another item or go back to the main menu.
            goagain = False
            while goagain == False:
               response = str(input("\nPress 1 to parse another item.\nPress any other key to go back to the Main Menu.\n>>> "))
               
               # Goes back to the start of this submenu, and user can make another parse request.
               if response == "1":
                  goagain = True
                  sub_menu1 = True
               
               # Goes back to Main Menu and clears terminal. 
               else:
                  goagain = True
                  sub_menu1 = False
                  os.system('cls')
      
      # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
      
      # 2) ADD NEW ITEM
      elif response == 2:
         
         sub_menu2 = True
         while sub_menu2 == True:
            
            # Some instructions regarding errors.
            print("\nNOTE: If you make a mistake while inputting a new item, just exit the program.")
            
            # Enter item name.
            new_item = str(input("\nEnter the name of the item you want to save.\n>>> "))
            while not isinstance(new_item, str):
               new_item = str(input("\nPlease enter a valid item name.\n>>> "))
            
            # Enter newegg link.
            newegginput = str(input("\nEnter the item link from Newegg.\n>>> "))
            while not newegginput.startswith("https://www.newegg.com/"):
               newegginput = str(input("\nPlease enter an item link from Newegg.\n>>> "))
            
            # Enter microcenter link.
            microcenterinput = str(input("\nEnter the item link from Microcenter.\n>>> "))
            while not microcenterinput.startswith("https://www.microcenter.com/"):
               microcenterinput = str(input("\nPlease enter an item link Microcenter.\n>>> "))
            
            # Enter bestbuy link.
            bestbuyinput = str(input("\nEnter the item link from Bestbuy.\n>>> "))
            while not bestbuyinput.startswith("https://www.bestbuy.com/"):
               bestbuyinput = str(input("\nPlease enter an item link from Bestbuy.\n>>> "))
            
            # Assembles the item and links into a dictionary. Plugs it into the Storage method addItem and writes new information into file.
            item_dictionary = dictAssembly(item_name=new_item, neweggurl=newegginput, microcenterurl=microcenterinput, bestbuyurl=bestbuyinput)
            my_storage.addItem(item_dictionary)
            
            # Prompt user to enter a new item or go back to main menu.
            more_items = str(input("\nEnter 1 to enter another item, or any other key to go back to the main menu.\n>>> "))
            
            # Goes back to start of this menu to enter a new item.
            if more_items == "1":
               sub_menu2 = True
            
            # Goes back to main menu.
            else:
               sub_menu2 = False
               os.system('cls')

      # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

      # 3) REMOVE ITEM
      elif response == 3:
         
         print("\nIn the remove item menu please be as specific as possible.\n")
         
         sub_menu3 = True
         while sub_menu3 == True:
            
            # Asks user to input the item that they want to remove.If they press one it displays all items currently in the file.
            item_to_remove = str(input("\nEnter the name of the item you want to remove.\nPress 1 to display all stored items.\n>>> "))
            
            while item_to_remove == "1":
               print("\nYour saved items:\n")
               my_storage.displayItems()
               item_to_remove = str(input("\nEnter the name of the item you want to remove.\nPress 1 to display saved items.\n>>> "))
            
            # Calls removeItem and removes the inputted item.
            my_storage.removeItem(item_to_remove)
            print("\nItem was successfully removed.\n")
            
            #  Prompts user to enter 1 to enter another item or any other key to go back to the main menu. 
            more_items = str(input("\nEnter 1 to enter another item or any other key to go back to the main menu.\n>>>"))
            if more_items == "1":
               sub_menu3 = True
            else:
               sub_menu3 = False
               os.system('cls')
      
      # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
      
      # 4) EXIT PROGRAM/QUIT
      elif response == 4:
         main_menu = False
         
      # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
   
      # RESPONSE TO INVALID MAIN MENU INPUT
      else:
         print("\nPlease enter a valid response.\n")
    
if __name__ == "__main__":
    main()
    
   