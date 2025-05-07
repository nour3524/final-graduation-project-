from typing import List, Optional
from pydantic import BaseModel
class UserSignInVM(BaseModel):
    Email: str
    Password: str
class UserSignUpVM(BaseModel):
    Username: str
    Email: str
    Password: str
    Role: str