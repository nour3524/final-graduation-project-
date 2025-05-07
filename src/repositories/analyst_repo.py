from db import get_db_connection
from models.entities import Analyst
from common import map_object

def get_analyst_records():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            admin_id,
            username,
            contact_number,
            email,
            last_login
        FROM system_admins
        WHERE role = 'SOC Analyst'
    """)
    rows = cursor.fetchall()
    conn.close()
    return [map_object(row, Analyst) for row in rows]