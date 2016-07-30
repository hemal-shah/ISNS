__author__ = "Hemal Shah"

# Simple Data Encryption Standard

KEY = '0010010111' #Change the key here!
FIXED_P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
FIXED_P8 = (6, 3, 7, 4, 8, 5, 10, 9)
FIXED_IO_P8 = (2, 6, 3, 1, 4, 8, 5, 7)
FIXED_IP_INVERSE = (4, 1, 3, 5, 7, 2, 8, 6)
FIXED_EP = (4, 1, 2, 3, 2, 3, 4, 1)
FIXED_P4 = (2, 4, 3, 1)

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

def permute(bits, order):
    """
        This function performs permutations based on
        the order specified.
        bits : The bits to be re-ordered based on the
        variable order.
        order : A tuple specifying the order of permutation.
    """

    print "Now, permuting the {} in the order: ".format(bits)
    print " ".join(str(i) for i in order)
    return ''.join(bits[i-1] for i in order)


def getKey1(key_10_bit):
    # This function generates the key 1 for the SDES.

    key_10_bit = permute(key_10_bit, FIXED_P10)
    print "The key after IP is {}".format(key_10_bit)
    left_part = leftShift(getLeftPart(key_10_bit))
    right_part = leftShift(getRightPart(key_10_bit))
    print "Left Part = ", left_part
    print "Right Part = ", right_part
    key1 = permute((left_part + right_part), FIXED_P8)
    print "Key 1 formed is ===== ", key1
    return key1

def getKey2(key_10_bit):
    # This function generates the key 2 for the SDES.
    
    key_10_bit = permute(key_10_bit, FIXED_P10)
    print "The key after IP is {}.".format(key_10_bit)
    left = leftShift(getLeftPart(key_10_bit), times = 3)
    right = leftShift(getRightPart(key_10_bit), times = 3)
    print "Left Part = ",left
    print "Right Part = ", right
    key2 = permute((left + right), FIXED_P8)
    print "Key 2 formed is ===== ", key2
    return key2 

def getRightPart(bits):
    print "Seperating right part from {}.".format(bits)
    return bits[(len(bits)/2):]

def getLeftPart(bits):
    print "Seperating left part from {}.".format(bits)
    return bits[:(len(bits)/2)]

def leftShift(original, times = 1):
    # Performs 'times' times shift left operation on the original
    # bits data
    for i in range(0, times):
        print "Left Shifting %s, %d time."%(original, (i+1))
        original = original[1:] + original[0]
    return original

KEY1 = getKey1(KEY) #generated key1
KEY2 = getKey2(KEY) #generated key2


def xor(bits1, bits2):
    """
        Simple function to perform bitwise X-OR
        operation between two input values
        and return it in form of string.
    """
    if(len(bits1) != len(bits2)):
        return "Length should be same for both!"

    print "Performing X-OR between %s and %s."%(bits1, bits2)
    return ''.join(str((int(bits1[i]) ^ int(bits2[i]))) for i in range(0, len(bits2)))


def lookup_in_sbox(bits):
    # the length of bits should be 8!
    # sbox can either be S0 or S1.
    left = getLeftPart(bits)
    right = getRightPart(bits)
    row = int(left[0] + left[3], 2)
    col = int(left[1] + left[2], 2)
    row1 = int(right[0] + right[3], 2)
    col1 = int(right[1] + right[2], 2)

    print "The value at row %d and column %d in S0 is %d."%(row, col, S0[row][col])
    print "The value at row %d and column %d in S1 is %d."%(row1, col1, S1[row1][col1])

    intermediate = '{0:02b}'.format(S0[row][col])
    intermediate += '{0:02b}'.format(S1[row1][col1])
    return permute(intermediate, FIXED_P4)

def func(r, key):
    r = permute(r, FIXED_EP)
    return xor(r, key)

def func1(l, r, key):
    # This should return (l xor func(r, key), r)
    # return the format l, r
    return xor(l, lookup_in_sbox(func(r, key))), r

def encrypt(text):
    print "Performing Encryption on {}".format(text)
    text = permute(text, FIXED_IO_P8)
    l, r = func1(getLeftPart(text), getRightPart(text), KEY1)
    print "The left and right side after supplying key1 is :"
    print "Left = ", l
    print "Right = ", r
    l, r = r, l #Switching!
    print "The left and right side after switching. :"
    print "Left = ", l
    print "Right = ", r
    l, r = func1(l, r, KEY2)
    print "The left and right side after supplying key2 is :"
    print "Left = ", l
    print "Right = ", r
    encrypted = permute((l + r), FIXED_IP_INVERSE)
    print "Encrypted Cipher Text is {}".format(encrypted)
    return encrypted

def decrypt(ct):
    print "The Cipher text to decrypt is : {}".format(ct)
    ct = permute(ct, FIXED_IO_P8)
    l, r = func1(getLeftPart(ct), getRightPart(ct), KEY2)
    print "The left and right side after supplying key2 is :"
    print "Left = ", l
    print "Right = ", r
    l, r = r, l #Switching!
    print "The left and right side after switching. :"
    print "Left = ", l
    print "Right = ", r
    l, r = func1(l, r, KEY1)

    print "The left and right side after supplying key1 is :"
    print "Left = ", l
    print "Right = ", r
    decrypted = permute((l + r), FIXED_IP_INVERSE)
    print "Decrypted Plain Text is {}".format(decrypted)

decrypt(encrypt('10100101'))