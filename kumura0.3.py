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
    new_item = input("Enter a New Item: ").title()
    # Checks item against catalog
    item = find_item(new_item)
    # If item already in catalog re direct to menu
    if item["Item"] != None:
        print("This is not a new item")
    else:
        # Asks for price
        price = float(input("Enter Price: "))
        # Asks for amount to stock
        new_stock = int(input("Enter amount of Stock: "))
        # Checks amount is under Max stock number
        stock = check_stock(new_stock, None, None)
        # Adds dictionary of item to catalog
        catalog.append({"Item":new_item, "Price":price, "Stock":stock})

    # Return an updated catalog
    return catalog
    


def check_stock(new_stock, stock, function):
    """
Ensures final stock count must not exceed 50
"""
    MAX_STOCK = 50
    MIN_STOCK= 0
    while new_stock > MAX_STOCK or new_stock < MIN_STOCK:
        if function == "+":
            print("You cannot have a stock over {}".format(MAX_STOCK))
            new_stock = add_stock(stock)
        elif function == "-":
            print("You cannot have a stock less than {}".format(MIN_STOCK))
            new_stock = sell_stock(stock)
        else:
            print("You cannot have a stock"+
                  "over {} or less than {}".format(MAX_STOCK,MIN_STOCK))
            try:
                new_stock = int(input("Enter New Stock: "))
            except:
                print("That was not a valid input")

    # Returns Corrected amount
    return new_stock
        

    
def restock(catalog):
    """
Allows user to restock an item
"""
    ADD = "+"
    # User inputs an item to restock
    restock_item = input("Enter Item to restock: ").title()
    # Finds item dictionary in catalog
    item = find_item(restock_item)
    print(item)
    if item["Item"] == restock_item:
        # Prints current stock
        print("{} currently has {} in stock".format(item["Item"], item["Stock"]))
        # adds to stock
        stock = add_stock(item["Stock"])
        # Ensures stock is under 50
        final_stock = check_stock(stock, item["Stock"], ADD)
        # Updates catalog
        for items in catalog:
            if items == item:
                items.update({"Stock":final_stock})
        print(item)

    # catches any items not already in catalog
    else:
        print("This item is not in catalog")
    # Returns updated Catalog

def sell_stock(stock):
    """
takes away from an items stock if selling
minus_stock = amount - (amount * 2)
"""
    sell_stock = int(input("Enter sale amount: "))
    stock -= sell_stock
    return stock

def add_stock(stock):
    """
adds stock to an item
    """
    add_stock = int(input("Enter add stock amount: "))
    stock += add_stock
    print(stock)
    return stock


def sell(catalog):
    """
Lets the user sell a number of a product
takes away from stock
prints gst price

"""
    MINUS = "-"
    # User inputs an item to restock
    sale_item = input("Enter sale item: ").title()
    # Finds item dictionary in catalog
    item = find_item(sale_item)
    print(item)
    if item["Item"] == sale_item:
        # Finds GST inclusive price
        gst_price = gst(item["Price"])
        # Prints price
        print("The GST inclusive price"+
              "of {} is {}".format(item["Item"], gst_price))
        # Approves sale with price
        choice = input("Would you like to continue with sale(y/n): ")
        if choice == "y":
            # takes away from stock
            stock = sell_stock(item["Stock"])
            # Ensures stock is within specifications
            final_stock = check_stock(stock, item["Stock"], MINUS)
            # Updates catalog
            for items in catalog:
                if items == item:
                    items.update({"Stock":final_stock})
                    print(items)
        else:
            quit
        
    else:
        print("This item is not in catalog")
        


def find_item(item):
    """
Finds a specified item key and returns it
"""
   #checks if nothing in catalog
    if not len(catalog):
        return {"Item":None}
    else:
        # Compares each cataloged title to the title asked for
        for items in catalog:
            if items["Item"] == item:
                # Returns item if found
                return items
    
    return {"Item":None}
        


def gst(price):
    """
Calculates the gst included price of an item
"""
    GST = 0.15
    price += GST * price
    return price

def print_all(catalog):
    """
Prints every item, price and stock
"""
    for items in catalog:
        for key, value in items:
            print(key, ":", value)
    

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
