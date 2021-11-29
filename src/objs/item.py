class Item:
    _id: int
    _name: str
    _price: float
    _category: str
    _quantity: int


    #constructor needs all information to instantiate object
    def __init__(self, id, name, price, category, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
    
    #to string method
    def toString(self):
        return (f'{self.id},{self.name},{self.price},{self.category},{self.quantity}')

    #getters
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getCategory(self):
        return self.category
    def getQuantity(self):
        return self.quantity

    #setters
    def setID(self, id_):
        self.id = id_
    def setName(self, name_):
        self.name = name_
    def setPrice(self, price_):
        self.price = price_
    def setCategory(self, category_):
        self.category = category_
    def setQuantity(self, quantity_):
        self.quantity = quantity_