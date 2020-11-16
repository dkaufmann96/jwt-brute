from bruteforce import check
from string import ascii_letters, digits, punctuation
import time
import tracemalloc

token = str(input("Insert token: "))

maxlength = int(input("Max length of secret: "))

# use all letters, digits, and special characters for brute forcing
characters = ascii_letters + digits + punctuation

start = time.time()
check(token, characters, maxlength+1)
end = time.time()
print("Elapsed time: " + str(end - start) + "s")