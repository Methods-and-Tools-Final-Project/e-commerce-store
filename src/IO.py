#this class holds all the methods that will perform reading and writing to/from the data files in 
# the data directory, seriallizing the data into objects is also done here, changing data should be performed outside
# of this class and then the method to write the objects to the files should be invoked from this class

from os.path import exists
from objs.cart import Cart
from objs.item import Item
from objs.purchase import Purchase
from objs.user import User

def getCarts():
    fileExists = exists("src/data/carts.csv")

    if (fileExists):
        retList = []

        lines = tuple(open("src/data/carts.csv", 'r'))

        for line in lines:
            parts = str(line).split(",")

            if (len(parts) != 3):
                raise Exception("Given line cannot be serialized to a cart object: ", line)
            else:
                retList.append(Cart(parts[0], parts[1], parts[2]))
        
        return retList

    else:
        raise Exception("Carts.csv file does not exist")

def getItems():
    fileExists = exists("src/data/items.csv")

    if (fileExists):
        retList = []

        lines = tuple(open("src/data/items.csv", 'r'))

        for line in lines:
            parts = str(line).split(",")

            if (len(parts) != 5):
                raise Exception("Given line cannot be serialized to an item object: ", line)
            else:
                retList.append(Item(parts[0], parts[1], parts[2], parts[3], parts[4]))
        
        return retList

    else:
        raise Exception("Items.csv file does not exist")

def getPurchases():
    fileExists = exists("src/data/purchases.csv")

    if (fileExists):
        retList = []

        lines = tuple(open("src/data/purchases.csv", 'r'))

        for line in lines:
            parts = str(line).split(",")

            if (len(parts) != 4):
                raise Exception("Given line cannot be serialized to a purchase object: ", line)
            else:
                retList.append(Purchase(parts[0], parts[1], parts[2], parts[3]))
        
        return retList

    else:
        raise Exception("Purchases.csv file does not exist")

def getUsers():
    fileExists = exists("src/data/users.csv")

    if (fileExists):
        retList = []

        lines = tuple(open("src/data/users.csv", 'r'))

        for line in lines:
            parts = str(line).split(",")

            if (len(parts) != 5):
                raise Exception("Given line cannot be serialized to a user object: ", line)
            else:
                retList.append(User(parts[0], parts[1], parts[2], parts[3], parts[4]))
        
        return retList

    else:
        raise Exception("Users.csv file does not exist")

def writeCarts(cartList):
    print("Writing passed list containing ", len(cartList), " carts to carts.csv")
    
    fileExists = exists("src/data/carts.csv")

    if (fileExists):
        lines = []

        for cart in cartList:
            lines.append(cart.toString())

        with open('src/data/carts.csv', 'w') as f:
            f.writelines(lines)
            
    else:
        raise Exception("Carts.csv file does not exist")

def writeItems(itemList):
    print("Writing passed list containing ", len(itemList), " items to items.csv")
    
    fileExists = exists("src/data/items.csv")

    if (fileExists):
        lines = []

        for item in itemList:
            lines.append(item.toString())

        with open('src/data/items.csv', 'w') as f:
            f.writelines(lines)
            
    else:
        raise Exception("Items.csv file does not exist")


def writePurchases(purchaseList):
    print("Writing passed list containing ", len(purchaseList), " purchases to purchases.csv")
    
    fileExists = exists("src/data/purchases.csv")

    if (fileExists):
        lines = []

        for purchase in purchaseList:
            lines.append(purchase.toString())

        with open('src/data/purchases.csv', 'w') as f:
            f.writelines(lines)
            
    else:
        raise Exception("Purchases.csv file does not exist")

def writeUsers(userList):
    print("Writing passed list containing ", len(userList), " users to users.csv")
    
    fileExists = exists("src/data/users.csv")

    if (fileExists):
        lines = []

        for user in userList:
            lines.append(user.toString())

        with open('src/data/users.csv', 'w') as f:
            f.writelines(lines)
            
    else:
        raise Exception("Users.csv file does not exist")