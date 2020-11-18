import itertools
from multiprocessing import Pool, cpu_count
from multiprocessing.sharedctypes import Value, Array
from ctypes import c_char_p
from signature_validation import validate
from functools import partial
import sys
import time

sharedToken = None
sharedN = None
sharedC = None

def checkSecret(secret):
    global sharedToken
    global sharedN
    global sharedC
    
    secret = "".join(secret)
    print("N="+ str(sharedN.value) + " - tried secret: \"" + secret + "\"", end='\r')
    with sharedC.get_lock():
            sharedC.value += 1
    if validate(sharedToken.value, secret):
        return secret
    

def check(token, characters, maxlength):
    global sharedToken
    global sharedN
    global sharedC

    sharedToken = Value(c_char_p, token.encode())
    sharedN = Value('i', 0)
    sharedC = Value('i', 0)

    cores = cpu_count()

    pool = Pool(cores)

    secretFound = False

    print("Number of cores in use: " + str(cores))
    
    for n in range(0, maxlength):
        with sharedN.get_lock():
            sharedN.value = n
        generator = itertools.product(characters, repeat = n)
        for secret in pool.imap_unordered(checkSecret, generator, 5000):
            if secret or secret == "":
                shutDownPool(pool)
                secretFound = True
                outputSecret(secret)
                return secret

    if(secretFound == False):
        shutDownPool(pool)
        outputSecret(secret)
def outputSecret(secret):
    global sharedC
    if(secret or secret == ""):
        print("The secret used to generate the token is \""+ secret +"\".")
    else:
        print("Tries: " + str(sharedC.value))
        print("The secret could not be determined. Try increasing the maximum length.")

def shutDownPool(pool: Pool):
    pool.terminate()
    pool.join()