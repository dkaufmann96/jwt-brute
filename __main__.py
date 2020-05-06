from string import letters, digits, punctuation
from bruteforce import check

# use all letters, digits, and special characters for brute forcing
characters = letters + digits + punctuation

token = str(raw_input("Insert token: "))

maxlength = int(raw_input("Max length of secret: "))

secret = check(token, characters, maxlength) or ""

print "The secret used to generate the token is \""+ secret +"\"."