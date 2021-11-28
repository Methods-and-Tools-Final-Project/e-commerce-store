class Item:
    _id: int
    _name: str
    _price: float
    _category: str
    _quantity: int


    #constructor needs all information to instantiate object
    def __init__(self, id, name, price, cateogry, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.cateogry = cateogry
        self.quantity = quantity
    
    #to string method
    def toString(self):
        return (f'{self.id},{self.name},{self.price},{self.cateogry},{self.quantity}')

    #getters
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getCategory(self):
        return self.cateogry
    def getQuantity(self):
        return self.quantity

    #setters
    def setID(self, id_):
        self.id = id_
    def setName(self, name_):
        self.name = name_
    def setAddress(self, price_):
        self.price = price_
    def setEmail(self, category_):
        self.category = category_
    def setPhoneNum(self, quantity_):
        self.quantity = quantity_