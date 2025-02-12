import time
import pyqrcode
import png
from pyqrcode import QRCode

PASSWORD = "1234"
QR_SECRET = "COLLEAGUE-ACCESS-2024"  # Secret code inside the QR
colleague_access_granted = False  

# Generate the QR Code
qr = pyqrcode.create(QR_SECRET)
qr.png("colleague_qr.png", scale=6)  # Save QR as an image

print("📲 Scan this QR code to request access:")
qr.show()  # Show QR code

while True:
    user_input = input("\nEnter access password OR scan the QR code: ")
    
    if user_input == PASSWORD or user_input == QR_SECRET:
        print("✅ Temporary access granted! Auto-lock disabled for 2 minutes.")
        colleague_access_granted = True
        time.sleep(120)  # Disable auto-lock for 2 minutes
        print("🔒 Temporary access expired. Auto-lock re-enabled.")
        break  
    else:
        print("❌ Access denied! Try again.")
