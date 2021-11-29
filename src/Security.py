import IO
import hashlib

def validateUser(username, password):
    ret = False

    #for all the users in the database
    for user in IO.getUsers():
        #if the name and password match something in the database
        if (user.getName().lower().equals(username.lower()) and user.getPassword().equals(hash(password))):
            ret = True
            break;

    return ret

#hashes the given string using sha256
def hash(password):
    return hashlib.sha256(password).hexdigest()