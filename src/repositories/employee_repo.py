from db import get_db_connection
from models import *
from common import map_object

def get_employee_records():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            ep.user_id,
            ep.full_name AS name,
            ep.username,
            ep.email,
            ep.department,
            ep.device_id,
            ep.join_date,
            rs.risk_score,
            rs.risk_reason,
            ep.status
        FROM employees_profile ep
        LEFT JOIN risk_scoring rs ON ep.user_id = rs.user_id
        ORDER BY ep.join_date DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return [map_object(row, Employee) for row in rows]