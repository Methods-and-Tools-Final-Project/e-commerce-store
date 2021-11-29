#this class holds all the methods that will perform reading and writing to/from the data files in 
# the data directory, seriallizing the data into objects is also done here, changing data should be performed outside
# of this class and then the method to write the objects to the files should be invoked from this class

import os
from os.path import exists
from objs.cart import Cart
from objs.item import Item
from objs.purchase import Purchase
from objs.user import User

#get full contents of tables
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

            if (len(parts) != 6):
                raise Exception("Given line cannot be serialized to a user object: ", line)
            else:
                retList.append(User(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]))
        
        return retList

    else:
        raise Exception("Users.csv file does not exist")

#set full contents of tables
def writeCarts(cartList):
    fileExists = exists("src/data/carts.csv")

    if (fileExists):
        lines = []

        for cart in cartList:
            lines.append(cart.toString())

        print(len(lines))

        f = open('src/data/carts.csv', 'w')
        for line in lines:
            if len(line) != 0:
                f.write(line)
        f.write("\n")
            
    else:
        raise Exception("Carts.csv file does not exist")

def writeItems(itemList):
    fileExists = exists("src/data/items.csv")

    if (fileExists):
        lines = []

        for item in itemList:
            lines.append(item.toString())

        print(len(lines))

        f = open('src/data/items.csv', 'w')
        for line in lines:
            if len(line) != 0:
                f.write(line)
        f.write("\n")
            
    else:
        raise Exception("Items.csv file does not exist")


def writePurchases(purchaseList):
    fileExists = exists("src/data/purchases.csv")

    if (fileExists):
        lines = []

        for purchase in purchaseList:
            lines.append(purchase.toString())

        print(len(lines))

        f = open('src/data/purchases.csv', 'w')
        for line in lines:
            if len(line) != 0:
                f.write(line)
        f.write("\n")
            
    else:
        raise Exception("Purchases.csv file does not exist")


def writeUsers(userList):
    fileExists = exists("src/data/users.csv")

    if (fileExists):
        lines = []

        for user in userList:
            lines.append(user.toString())

        print(len(lines))

        f = open('src/data/users.csv', 'w')
        for line in lines:
            if len(line) != 0:
                f.write(line)
        f.write("\n")
            
    else:
        raise Exception("Useres.csv file does not exist")

#add entries to tables object methods
def addCartEntryByObj(cart):
    carts = getCarts()
    carts.append(cart)
    writeCarts(carts)

def addItemEntryByObj(item):
    items = getItems()
    items.append(item)
    writeItems(items)

def addPurchaseEntryByObj(purchase):
    purchases = getPurchases()
    purchases.append(purchase)
    writePurchases(purchases)

def addUserEntryByObj(user):
    users = getUsers()
    users.append(user)
    writeUsers(users)

#remove entries from tables by key
def removeCartEntry(userid, itemid):
    carts = getCarts()

    for cart in carts:
        if (int(cart.getUserID()) == int(userid) 
            and int(cart.getItemID()) == int(itemid)):
            carts.remove(cart)
            break;

    writeCarts(carts)

def removeItemEntry(itemid):
    items = getItems()

    for item in items:
        if (int(item.getItemID()) == int(itemid)):
            items.remove(item)
            break;

    writeCarts(items)

def removePurchaseEntry(userid, itemid):
    purchases = getPurchases()

    for purchase in purchases:
        if (int(purchase.getUserID) == int(userid) and int(purchase.getItemID) == int(itemid)):
            purchases.remove(purchase)
            break;

    writePurchases(purchases)

def removeUserEntry(id):
    users = getUsers()

    for user in users:
        if (int(user.getID()) == int(id)):
            users.remove(user)
            break;

    writeUsers(users)