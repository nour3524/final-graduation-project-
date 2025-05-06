class UserDataDTO():
    def __init__(self, ID: int, Username: str, Name: str):
        self.ID = ID
        self.UserName = Username
        self.Name = Name
        
class AddUserDTO():
    def __init__(self, Email: str, Username: str, PasswordHash: str, Role: str):
        self.Username = Username
        self.Email = Email
        self.PasswordHash = PasswordHash     
        self.Role = Role   