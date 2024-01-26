#!/usr/bin/env python3

import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

from AEScipher import AESCipher

import sys
import base64
saifer = AESCipher("blacksand")


iv = saifer.__dict__.insecureIV()
print ("iv: ", iv)
print ("ivBinary: ", "".join(["{:08b}".format(x) for x in iv]) )

print ("message: ", sys.argv[1])
msg = saifer.encrypt(sys.argv[1])
print ("ciphertext: ", msg)

dmsg = saifer.decrypt(msg)
print ("decrypted: ", dmsg)
