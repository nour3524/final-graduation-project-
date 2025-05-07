def map_object(row, object):
    return object(*row)
from models import SystemAdmin
def map_user_to_dict(object: SystemAdmin):
    return {
        "ID": object.AdminID,
        "UserName": object.Username,
        "Email": object.Email
    }