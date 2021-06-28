# kumura_store.py
# Rhiannon MacCreadie
# 22.06.2021
# This program will add, sell, and restock items at Hemis' kumura farm

def test():
    """
    test for something i need later
    """
    i = 50 - (50 * 2)
    print(i)

def add(catalog):
    """
Adds items to catalog with price and stock
returns updated catalog
"""
   
  
    # Asks user for item
    new_item = input("Enter a New Item: ").title()
    # Checks if item in catalog
    item = find_item(catalog, new_item)
    # Ensure only new items are added to catalog
    if item == new_item:
        # If already cataloged tell the user and go back to menu
        print("This item already in catalog")
    else:
        # If New Item ask for price
        price = input("Enter price of {}: ".format(new_item))
        # ask for stock (how much)
        stock = int(input("Enter stock amount: "))
        # check if stock under 50
        checked_stock = check_stock(stock)
        # update catalog
        catalog.append({"Item" : new_item , "Price" : price, "Stock" : checked_stock })

    # return updated catalog
    return catalog
            
            
    
        


def check_stock(stock):
    """
Lets user input how much of an item they are adding or minusing
Final stock count must not exceed 50
"""
    MAX = 50
    while stock > MAX:
        print("stock no more then 50 of an item")
        stock = int(input("Enter stock amount: "))

    return stock
        
        
        
    


def find_price():
    """
Lets the user access a certain items price
"""


def sell():
    """
Lets the user sell a number of a product
takes away from stock
prints gst price

"""


def restock():
    """
Allow user to restock a previously added item
"""


def find_item(catalog, new_item):
    """
finds a specified item
"""
    if not len(catalog):
        return None
    else:
        for items in catalog:
            if items["Item"] == new_item:
                print(items)
                return items["Item"]



def gst():
    """
Calculates the gst included price of an item
"""


def print_all():
    """
Prints every item, price and stock
"""


def menu(catalog):
    """
Redirects the user to chosen function
"""
    print(" Welcome to Hemi's Kumura store ")
    while True:
        print(""" (a)dd
    (s)ell
    (r)estock
    (p)rint
    (q)uit""")
        choice = input("Please enter an option: ").lower()
        # Redirect user
        if choice == "a":
            catalog = add(catalog)
        elif choice == "s":
            catalog = sell(catalog)
        elif choice == "r":
            catalog = restock(catalog)
        elif choice == "p":
            print_stock()
        elif choice == "q":
            break
        # Error catch if user doesnt input a letter correlation
        else:
            print("This is not a valid input :(")
            print("Try inputing a letter in bracket")

# Main
if __name__ == "__main__":
    catalog = []
    menu(catalog)
