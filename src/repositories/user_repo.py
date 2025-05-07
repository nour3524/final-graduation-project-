from db import get_db_connection
from models import *
from common import map_object

def get_user(email: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT admin_id, username, email, password_hash, role, last_login FROM system_admins WHERE email = ?",
        (email)
    )
    row = cursor.fetchone()
    conn.close()
    return map_object(row, SystemAdmin)

def add_user(user: AddUserDTO):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO system_admins (username, email, password_hash, role) VALUES (?, ?, ?, ?)",
        (user.Username, user.Email, user.PasswordHash, user.Role)
    )
    conn.commit()
    conn.close()