import IO
import hashlib

userID = 0

def getUserID():
    return userID

def validateUser(username, password):
    ret = False

    #for all the users in the database
    for user in IO.getUsers():
        #if the name and password match something in the database
        if (user.getName().lower()==(username.lower()) and user.getPassword()==(hash(password))):
            global userID
            userID = user.getID()
            ret = True
            break;

    return ret

#hashes the given string using sha256
def hash(password):
    return hashlib.sha256(bytes(password,"UTF-8")).hexdigest()