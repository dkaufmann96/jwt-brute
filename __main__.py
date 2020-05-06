from string import letters, digits, punctuation
from bruteforce import check
import time

# use all letters, digits, and special characters for brute forcing
characters = letters + digits + punctuation

token = str(raw_input("Insert token: "))

maxlength = int(raw_input("Max length of secret: "))

start = time.time()
secret = check(token, characters, maxlength+1)
end = time.time()
print "Elapsed time: " + str(end - start) + "s"

print "The secret used to generate the token is \""+ secret +"\"."