import base64
import hmac
import hashlib
import json

def validate(token, secret):
    # read parts from token
    parts = token.split(".", 3)
    header = parts[0]
    payload = parts[1]
    signature = parts[2]

    # parse stringified json
    headerDecoded = json.loads(base64.decodestring(header))

    # read algorithm from header part - not used yet
    algorithm = headerDecoded["alg"]

    # hash header.payload using provided secret
    headerPayloadHash = hmac.new(secret, header+"."+payload, hashlib.sha256).digest()

    # convert to base64url
    headerPayloadBase64 = base64.b64encode(headerPayloadHash)
    headerPayloadBase64 = headerPayloadBase64.replace("+", "-")
    headerPayloadBase64 = headerPayloadBase64.replace("/", "_")
    headerPayloadBase64 = headerPayloadBase64.replace("=", "")

    # check if the generated base64-encoded string matches the initial signature
    # this proves whether the token was generated using the provided key
    return headerPayloadBase64==signature
