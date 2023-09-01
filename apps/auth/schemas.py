

from pydantic import BaseModel, EmailStr, UUID4
from ..utils import BaseModelSchema


class SignupSchema(BaseModelSchema):
    # user info
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    # tenant info
    tenant: str
    country_code: str
    currency_code: str
    phone_number: str
    

class UserSchema(BaseModelSchema):
    # user info
    id: UUID4
    email: EmailStr
    first_name: str
    last_name: str
    
    


