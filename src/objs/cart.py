class Cart:
    _userid: int
    _itemid: int
    _quantity: int

    #constructor needs all information to instantiate object
    def __init__(self, userid, itemid, quantity):
        self.userid = userid
        self.itemid = itemid
        self.quantity = quantity
    
    #to string method
    def toString(self):
        return (f'{self.userid},{self.itemid},{self.quantity}')

    #getters
    def getUserID(self):
        return self.userid
    def getItemID(self):
        return self.itemid
    def getQuantity(self):
        return self.quantity

    #setters
    def setUserID(self, userid_):
        self.userid = userid_
    def setItemID(self, itemid_):
        self.itemid = itemid_
    def setQuantity(self, quantity_):
        self.quantity = quantity_