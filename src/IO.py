#this class holds all the methods that will perform reading and writing to/from the data files in 
# the data directory, seriallizing the data into objects is also done here, changing data should be performed outside
# of this class and then the method to write the objects to the files should be invoked from this class

from os.path import exists
from objs.cart import Cart
from objs.item import Item
from objs.purchase import Purchase
from objs.user import User

def getCarts():
    fileExists = exists("data/carts.csv")

    if (fileExists):
        retList = []

        lines = tuple(open("data/carts.csv", 'r'))

        for line in lines:
            parts = str(line).split(",")

            if (len(parts) is not 3):
                raise Exception("Given line cannot be serialized to a cart object: ", line)
            else:
                retList.append(Cart(parts[0], parts[1], parts[2]))
        
        return retList

    else:
        raise Exception("Carts.csv file does not exist")

def getItems():
    fileExists = exists("data/items.csv")

    if (fileExists):
        retList = []

        lines = tuple(open("data/items.csv", 'r'))

        for line in lines:
            parts = str(line).split(",")

            if (len(parts) is not 5):
                raise Exception("Given line cannot be serialized to an item object: ", line)
            else:
                retList.append(Item(parts[0], parts[1], parts[2], parts[3], parts[4]))
        
        return retList

    else:
        raise Exception("Items.csv file does not exist")

def getPurchases():
    fileExists = exists("data/purchases.csv")

    if (fileExists):
        retList = []

        lines = tuple(open("data/purchases.csv", 'r'))

        for line in lines:
            parts = str(line).split(",")

            if (len(parts) is not 4):
                raise Exception("Given line cannot be serialized to a purchase object: ", line)
            else:
                retList.append(Purchase(parts[0], parts[1], parts[2], parts[3]))
        
        return retList

    else:
        raise Exception("Purchases.csv file does not exist")

def getUsers():
    fileExists = exists("data/users.csv")

    if (fileExists):
        retList = []

        lines = tuple(open("data/users.csv", 'r'))

        for line in lines:
            parts = str(line).split(",")

            if (len(parts) is not 5):
                raise Exception("Given line cannot be serialized to a user object: ", line)
            else:
                retList.append(User(parts[0], parts[1], parts[2], parts[3], parts[4]))
        
        return retList

    else:
        raise Exception("Users.csv file does not exist")

def writeCarts(cartList):
    print("Writing passed list containing ", len(cartList), " carts to carts.csv")
    #todo

def writeItems(itemList):
    print("Writing passed list containing ", len(itemList), " items to items.csv")
    #todo

def writePurchases(purchaseList):
    print("Writing passed list containing ", len(purchaseList), " purchases to purchases.csv")
    #todo

def writeUsers(userList):
    print("Writing passed list containing ", len(userList), " users to users.csv")
    #todo
