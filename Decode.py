# Ref :
# https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
# https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/

import base64
import urllib.request
from stegano import lsb

urllib.request.urlretrieve("https://i.imgur.com/qnGXyMm.png", "9gag_dec.png")

img_dcd = lsb.reveal("9gag_dec.png")
print('Message in decoded :' + img_dcd)

msg_bytes = img_dcd.encode("ascii")
b64_bytes = base64.b64decode(msg_bytes)
b64_string = b64_bytes.decode("ascii")
print(f"Decode Base64 to String: {b64_string}")