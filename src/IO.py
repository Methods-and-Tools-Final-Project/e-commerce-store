#this class holds all the methods that will perform reading and writing to/from the data files in 
# the data directory, seriallizing the data into objects is also done here, changing data should be performed outside
# of this class and then the method to write the objects to the files should be invoked from this class

from os.path import exists
from objs.cart import Cart

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
    return ""

def getPurchases():
    return ""

def getUsers():
    return ""

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
