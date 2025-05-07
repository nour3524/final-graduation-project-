from db import get_db_connection
from models import *
from common import map_object

def get_malicious_logs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            id, 
            timestamp, 
            log_type, 
            details, 
            classification 
        FROM malicious_logs 
        ORDER BY timestamp DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return [map_object(row, MaliciousLog) for row in rows]


