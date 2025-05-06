# database connection

import pyodbc
from dotenv import load_dotenv
import os
# Load the .env file
load_dotenv()

DATABASE_CONFIG = {
    "driver": os.getenv("DATABASE_DRIVER"),
    "server": os.getenv("DATABASE_SERVER"),
    "database": os.getenv("DATABASE_NAME"),
}

def get_db_connection():
    conn = pyodbc.connect(
        f"DRIVER={DATABASE_CONFIG['driver']};"
          f"SERVER={DATABASE_CONFIG['server']};"  
          f"DATABASE={DATABASE_CONFIG['database']};"
          "Trusted_Connection=yes;"
        
    )
    return conn