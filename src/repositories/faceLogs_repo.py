from db import get_db_connection
from models import *
from common import map_object

def get_face_activity_logs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT log_id, event_time, pc_name, full_name, event_type, description FROM face_activity_logs ORDER BY event_time DESC")
    rows = cursor.fetchall()
    conn.close()
    return [map_object(row, FaceActivityLog) for row in rows]