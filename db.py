import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-6P94OPL;"  
    "DATABASE=FaceRecognitionDB;"
      "Trusted_Connection=yes;"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()

print("✅ Users in Database:")
for user in users:
    print(user)

conn.close()

