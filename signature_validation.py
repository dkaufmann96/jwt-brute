import base64
import hmac
import hashlib
import json

def validate(token, secret):
    # read parts from token
    token = token.decode()
    parts = token.split(".", 3)
    headerWithPayload = (parts[0]+"."+parts[1]).encode()
    header = parts[0]
    payload = parts[1]
    signature = parts[2]

    # parse stringified json
    headerDecoded = json.loads(base64.b64decode(header))

    # read algorithm from header part - not used yet
    algorithm = headerDecoded["alg"]

    # hash header.payload using provided secret
    headerPayloadHash = hmac.digest(secret.encode(), headerWithPayload, hashlib.sha256)

    # convert to base64url
    headerPayloadBase64 = base64.b64encode(headerPayloadHash).decode()
    headerPayloadBase64 = headerPayloadBase64.replace("+", "-")
    headerPayloadBase64 = headerPayloadBase64.replace("/", "_")
    headerPayloadBase64 = headerPayloadBase64.replace("=", "")

    # check if the generated base64-encoded string matches the initial signature
    # this proves whether the token was generated using the provided key
    return headerPayloadBase64==signature
