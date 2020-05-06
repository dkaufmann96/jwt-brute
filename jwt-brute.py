import base64
import hmac
import hashlib
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.5mhBHqs5_DTLdINd9p5m7ZJ6XD0Xc55kIaCRY5r6HRA"
secret = "test"

parts = token.split(".", 3)
header = parts[0]
payload = parts[1]
signature = parts[2]

headerDecoded = json.loads(base64.decodestring(header))
algorithm = headerDecoded["alg"]

print "header: " + header
print "payload: " + payload
print "signature: " + signature

headerPayloadHash = hmac.new(secret, header+"."+payload, hashlib.sha256).digest()

headerPayloadBase64 = base64.b64encode(headerPayloadHash)
headerPayloadBase64 = headerPayloadBase64.replace("+", "-")
headerPayloadBase64 = headerPayloadBase64.replace("/", "_")
headerPayloadBase64 = headerPayloadBase64.replace("=", "")

print "\n"

print "hashed header.payload using algorithm \""+algorithm+"\" and secret \"" + secret + "\""

print "header.payload base64url encoded: " + headerPayloadBase64

print "original signature: " + signature

if headerPayloadBase64==signature:
    print "they match"
