import itertools
from multiprocessing import Pool, Event, cpu_count
from multiprocessing.sharedctypes import Value, Array
from ctypes import c_char_p
from signature_validation import validate
from functools import partial
import sys
import time

sharedToken = None
sharedN = None
sharedC = None
event = None

def checkSecret(secret):
    global sharedToken
    global sharedN
    global sharedC

    if(event.is_set()):
        return
    with sharedC.get_lock():
            sharedC.value += 1
    secret = "".join(secret)
    print("N="+ str(sharedN.value) + " - tried secret: \"" + secret + "\"", end='\r')
    if validate(sharedToken.value, secret):
        event.set()
        outputSecret(secret)

def check(token, characters, maxlength):
    global sharedToken
    global sharedN
    global sharedC
    global event

    sharedToken = Value(c_char_p, token.encode())
    sharedN = Value('i', 0)
    sharedC = Value('i', 0)
    event = Event()

    cores = cpu_count()

    pool = Pool(cores)

    print("Number of cores in use: " + str(cores))
    
    for n in range(0, maxlength):
        with sharedN.get_lock():
            sharedN.value = n
        generator = itertools.product(characters, repeat = n)
        pool.imap_unordered(checkSecret, generator, 5000)
    pool.close()
    pool.join()
    outputSecret(None)
def outputSecret(secret):
    global sharedC
    if(secret):
        
        print("The secret used to generate the token is \""+ secret +"\".")
    else:
        print("Tries: " + str(sharedC.value))
        print("The secret could not be determined. Try increasing the maximum length.")