#!/usr/bin/env python3

import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import base64
import time

from quantumAES import AESCipher
from braket_bridge import *

print ('Enter a message to encrypt:')

txt = input()

braket_bits = run_circuit()

#braket_bits = ''
#for x in range(4):
#    braket_bits+=run_circuit()

time.sleep(12)
print("Quantum Initialization Vector:")
print (braket_bits)

time.sleep(7)
saifer = AESCipher("blacksand", braket_bits)
print (list(saifer.insecureIV))

time.sleep(7)
iv = saifer.insecureIV
print (iv)
print ()

time.sleep(4)

print("Encrypting the string \"" + txt + "\"")

time.sleep(8)

msg = saifer.encrypt(txt)
print ("Ciphertext: " + msg)

dmsg = saifer.decrypt(msg)
print ("Plaintext: " + dmsg)

