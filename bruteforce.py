from itertools import product
from signature_validation import validate

def checkSecret(token, secret, n):
    print "N="+ str(n) + " - tried secret: \"" + ''.join(secret) + "\""
    if validate(token, ''.join(secret)):
        return ''.join(secret)

def check(token, characters, maxlength):
    for n in xrange(0, maxlength):
        generator=product(characters, repeat = n)
        for secret in generator:
            successful = checkSecret(token, secret, n)
            if(successful or successful == ""):
                return successful
    