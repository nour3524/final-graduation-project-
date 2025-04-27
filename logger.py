import pyodbc
import socket
from datetime import datetime

# 🔹 Automatically get the current PC name
PC_NAME = socket.gethostname()

# 🔹 Log Face Activity to SQL
def log_event(event_type, full_name, description):
    try:
        conn = pyodbc.connect(
          "DRIVER={ODBC Driver 17 for SQL Server};"
          "SERVER=DESKTOP-6P94OPL;"  
          "DATABASE=UEBA_Analytics;"
          "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dbo.face_activity_logs (pc_name, full_name, event_type, description)
            VALUES (?, ?, ?, ?)
        """, (PC_NAME, full_name, event_type, description))
        conn.commit()
        conn.close()
        print(f"📝 Log saved: {event_type} - {full_name}")
    except Exception as e:
        print(f"❌ Failed to log event: {e}")
