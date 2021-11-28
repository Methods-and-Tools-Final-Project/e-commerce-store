class Purchase:
    _userid: int
    _itemid: int
    _quantity: int
    _time: str

    #constructor needs all information to instantiate object
    def __init__(self, userid, itemid, quantity, time):
        self.userid = userid
        self.itemid = itemid
        self.quantity = quantity
        self.time = time;
    
    #to string method
    def toString(self):
        return (f'{self.userid},{self.itemid},{self.quantity},{self.time}')

    #getters
    def getUserID(self):
        return self.userid
    def getItemID(self):
        return self.itemid
    def getQuantity(self):
        return self.quantity
    def getTime(self):
        return self.time

    #setters
    def setUserID(self, userid_):
        self.userid = userid_
    def setItemID(self, itemid_):
        self.itemid = itemid_
    def setQuantity(self, quantity_):
        self.quantity = quantity_
    def setTime(self, time_):
        self.time = time_