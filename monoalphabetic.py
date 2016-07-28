import random
alpha = "abcdefghijklmnopqrstuvwxyz"

l = list(alpha)
random.shuffle(l)
key = "".join(l)

print "Key is : " + key

def encrypt(text):
    text = text.lower()
    e = []
    for char in text:
        e.append(key[alpha.index(char)])
        
    print "Encrypted message = "
    string = "".join(e)
    print "".join(e)
    decrypt(string)
    
    
    
def decrypt(encrypted):
    encrypted = encrypted.lower()
    d = []
    for char in encrypted:
        d.append(alpha[key.index(char)])
    
    print "".join(d)
encrypt("Hemal")