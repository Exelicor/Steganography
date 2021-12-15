# Ref:
# https://sr.ht/~cedric/stegano/
# https://pythonrepo.com/repo/Damgaard-PyImgur-python-third-party-apis-wrappers
# https://github.com/cedricbonhomme/Stegano
# https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/

import base64
import json
import requests
from stegano import lsb
import pyimgur

msg = input('Input Message to Encode : ')
msg_bytes = msg.encode("ascii")
b64_bytes = base64.b64encode(msg_bytes)
b64_string = b64_bytes.decode("ascii")
print(f"Encoded string to Base64: {b64_string}")

img_steg = lsb.hide("9gag.png", b64_string)
img_steg.save("9gag_enc.png")
img_dcd = lsb.reveal("9gag_enc.png")
print(img_dcd)
print("Message inserted successfully ")

CLIENT_ID = "f3204c36c8223a3"
PATH = "9gag_enc.png"

image = pyimgur.Imgur(CLIENT_ID)
uploaded_image = image.upload_image(PATH, title="Steg")
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.type)