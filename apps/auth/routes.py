from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import SignupSchema
from .models import User, Tenant, Role, Permission
from ..db import get_session
from fastapi_users import FastAPIUsers

router = APIRouter()

@router.get("/signup")
async def signup(
    data: SignupSchema,
    session=Depends(get_session)
):
    # create tanent
    tanent = Tenant(
        name=data.tenant,
        country_code=data.country_code,
        currency_code=data.currency_code,
        phone_number=data.phone_number,
    )
    
    user = User(
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
        tenant_id=tanent.id,
    )
    
    with session.begin():
        session.add(tanent)
