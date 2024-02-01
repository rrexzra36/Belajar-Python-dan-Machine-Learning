import os
import pyqrcode 
from pyqrcode import QRCode 
  
#input username instagram
username = str(input("Username IG\t: ")).lower()
print(f"username saya {username}")

#charater detect on username
userfix = username.replace(".", "_")

# String which represent the QR code 
s = (f"https://www.instagram.com/{username}/")
  
# Generate QR code 
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png" 
url.svg(f"{userfix}.svg", scale = 8)