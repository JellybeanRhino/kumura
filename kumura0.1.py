# kumura_store.py
# Rhiannon MacCreadie
# 22.06.2021
# 28.06.2021
# This program will add, sell, and restock items at Hemis' kumura farm

def add(catalog):
    """
Adds items to catalog with price and stock
returns updated catalog
"""
    # Asks user for a new item
    new_item = input("Enter a New Item: ")
    # Checks item against catalog
    item = find_item(new_item)
    # If item already in catalog re direct to menu
    if item == new_item:
        print("This is not a new item")
    else:
        # Asks for price
        price = float(input("Enter Price: "))
        # Asks for amount to stock
        new_stock = int(input("Enter amount of Stock: "))
        # Checks amount is under Max stock number
        stock = check_stock(new_stock)
        # Adds dictionary of item to catalog
        catalog.append({"Item":new_item, "Price":price, "Stock":stock})

    # Return an updated catalog
    return catalog
    


def check_stock(new_stock):
    """
Ensures final stock count must not exceed 50
"""
    MAX_STOCK = 50
    while new_stock > MAX_STOCK:
        print("You cannot have a stock over {}".format(MAX_STOCK))
        new_stock = int(input("Enter New Stock: "))

    # Returns Corrected amount
    return new_stock
        

    
def restock():
    """
Allows user to restock an item
"""
    # User inputs an item to restock
    restock_item = input("Enter Item to restock: ")
    # Finds item in catalog
    item = find_item(restock_item)
    if item == restock_item:
        # Uses item to find previous stock
        stock = find_stock(item)
        # Prints current stock
        print(stock)
        # Asks user for restock value
        new_stock = input("Enter new stock amount: ")
        stock = check_stock(new_stock)
        # Updates catalog
        catalog.update
    else:
        print("This item is not in catalog")
    # Returns updated Catalog

def sell_stock():
    """
takes away from an items stock if selling
minus_stock = amount - (amount * 2)
"""

def find_stock():
    """
finds the stock of a specified item
"""

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



def find_item(item):
    """
Finds a specified item key and returns it
"""
    # Roll through each dictionary
    # Compares each cataloged title to the title asked for
    for items in catalog:
        # Returns item if already in catalog
        if item == items["title"]:
            return item
        else:
            # Returns Nothing if not in catalog
            item = None
            return item
            


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
    # Make a loop
    while True:
        print("""(a)dd
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
            quit
        # Error catch if user doesnt input a letter correlation
        else:
            print("This is not a valid input :(")
            print("Try inputing a letter in bracket")

# Main
if __name__ == "__main__":
    catalog = []
    menu(catalog)
