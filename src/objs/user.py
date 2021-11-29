class User:
    _id: int
    _name: str
    _password: str
    _address: str
    _email: str
    _phoneNum: str

    #constructor needs all information to instantiate object
    def __init__(self, id, name, password, address, email, phoneNum):
        self.id = id
        self.name = name
        self.password = password
        self.address = address
        self.email = email
        self.phoneNum = phoneNum
    
    #to string method
    def toString(self):
        return (f'{self.id},{self.name},{self.password},{self.address},{self.email},{self.phoneNum}')

    #getters
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getPassword(self):
        return self.password
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
    def setPassword(self, password_):
        self.password = password_
    def setAddress(self, address_):
        self.address = address_
    def setEmail(self, email_):
        self.email = email_
    def setPhoneNum(self, phoneNum_):
        self.phoneNum = phoneNum_