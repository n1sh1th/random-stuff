import hmac
import base64
import hashlib
import sys

## Download and Open public.pem file
with open('public_key.pem','r') as f:
    key = f.read()

## Get the updated token
final_token = input("Enter base64 updated header + payload for signing: ")

## Sign the token
signature = base64.urlsafe_b64encode(hmac.new(bytes(key,encoding='utf8'),final_token.encode('utf-8'),hashlib.sha256).digest()).decode('UTF-8').rstrip("=")

final_token = final_token+"."+signature
print("Updated token is: " + final_token)
