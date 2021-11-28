class User:
    _id: int
    _name: str
    _address: str
    _email: str
    _phoneNum: str

    #constructor needs all information to instantiate object
    def __init__(self, id, name, address, email, phoneNum):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.phoneNum = phoneNum
    
    #to string method
    def toString(self):
        return (f'{self.id},{self.name},{self.address},{self.email},{self.phoneNum}')

    #getters
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getPhoneNum(self):
        return self.phoneNum

    #setters
    def setID(self, id_):
        self.id = id_
    def setName(self, name_):
        self.name = name_
    def setAddress(self, address_):
        self.address = address_
    def setEmail(self, email_):
        self.email = email_
    def setPhoneNum(self, phoneNum_):
        self.phoneNum = phoneNum_