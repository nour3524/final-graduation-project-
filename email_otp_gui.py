import random
import smtplib
import pyodbc
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import sys

current_otp = None  # Temporary storage for OTP

# ✅ Send a 6-digit OTP to the user's email
def send_otp(user_name):
    global current_otp
    current_otp = str(random.randint(100000, 999999))  # Generate random code

    # Connect to the database
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
           "SERVER=DESKTOP-6P94OPL;"  
             "DATABASE=FaceRecognitionDB;"
             "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM Users WHERE name = ?", (user_name,))
    result = cursor.fetchone()
    conn.close()

    if not result or not result[0]:
        print(f"❌ No email found for user: {user_name}")
        return False

    recipient = result[0]

    # Email settings
    sender = "faceunlockbot@outlook.com"
    password = "Graduation_25"

    msg = MIMEText(f"""
    Hello {user_name},

    Your FaceUnlock login verification code is:

        {current_otp}

    Please enter this code within 2 minutes to complete your login.

    Regards,
    FaceUnlock Security Bot
    """)
    msg["Subject"] = "Your FaceUnlock OTP Code"
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        print(f"✅ OTP sent to {recipient}")
        return True
    except Exception as e:
        print("❌ Failed to send OTP email:", e)
        return False

# 🖥️ Show GUI to enter and verify the OTP
def verify_otp_gui():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Two-Factor Authentication")

    layout = QVBoxLayout()
    layout.addWidget(QLabel("Enter the 6-digit code sent to your email:"))

    input_box = QLineEdit()
    input_box.setMaxLength(6)
    input_box.setPlaceholderText("e.g. 123456")
    layout.addWidget(input_box)

    submit_btn = QPushButton("Verify")
    layout.addWidget(submit_btn)

    def verify():
        if input_box.text().strip() == current_otp:
            QMessageBox.information(window, "Access Granted", "✅ OTP Verified! Access granted.")
            window.close()
            app.quit()
        else:
            QMessageBox.critical(window, "Access Denied", "❌ Invalid OTP. Please try again.")

    submit_btn.clicked.connect(verify)
    window.setLayout(layout)
    window.show()
    app.exec_()

# 🔁 Combo function to use in face recognition flow
def run_email_otp_verification(user_name):
    if send_otp(user_name):
        verify_otp_gui()
