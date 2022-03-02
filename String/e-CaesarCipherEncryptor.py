
# string = "xyz"
# key = 2
# output: "zab"

def encryptor(string, key):
    ret = []
    key %= 26
    
    for val in string:
        nextVal = findNext(val, key)
        ret.append(nextVal)
    return "".join(ret)

def findNext(ch, key):
    newCode =  ord(ch) + key 

    if newCode <= 122:
        return chr(newCode)
    else:
        return chr(96 + newCode % 122)

string = "xyz"
key = 2 

print(encryptor(string, 2))