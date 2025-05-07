from typing import List

class SystemAdmin():
    def __init__(self, admin_id: int, username: str, email: str, password_hash: str, role: str, last_login):
        self.AdminID = admin_id
        self.Username = username
        self.Email = email
        self.PasswordHash = password_hash
        self.Role = role
        self.LastLogin = last_login
        
        
class MaliciousLog():
    def __init__(self, log_id: int, timestamp, log_type: str, details: str, classification: str):
        self.LogID = log_id
        self.Timestamp = timestamp
        self.LogType = log_type
        self.Details = details
        self.Classification = classification
        
class FaceActivityLog:
    def __init__(self, log_id, event_time, pc_name, full_name, event_type, description):
        self.log_id = log_id
        self.event_time = event_time
        self.pc_name = pc_name
        self.full_name = full_name
        self.event_type = event_type
        self.description = description

class Employee:
    def __init__(self, user_id, name, username, email, department, device_id, join_date, risk_score, risk_reason, status):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.email = email
        self.department = department
        self.device_id = device_id
        self.join_date = join_date
        self.risk_score = risk_score
        self.risk_reason = risk_reason
        self.status = status

class Analyst(SystemAdmin):
    def __init__(self, admin_id: int, username: str, contact_number: str, email: str, last_login):
        # Reuse attributes from SystemAdmin
        super().__init__(admin_id, username, email, None, "Analyst", last_login)
        self.contact_number = contact_number  # Add contact_number specific to Analyst


