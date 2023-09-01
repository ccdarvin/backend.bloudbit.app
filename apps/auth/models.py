

from typing import List
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, DateTime


import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

from datetime import datetime

from ..db import Base


class Tenant(Base):
    __tablename__ = "tenants"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    country_code: Mapped[str] = mapped_column(String(2), nullable=True)
    currency_code: Mapped[str] = mapped_column(String(3), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=True)
    
    created_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    
    def __repr__(self):
        return f"<Tenant(id={self.id}, name={self.name})>"
    
    
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    created_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
    
    
class Permission(Base):
    __tablename__ = "permissions"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<Permission(id={self.id}, name={self.name})>"
    

class Role(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    taneant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), nullable=False)
    tenant: Mapped["Tenant"] = relationship()
    
    created_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    
    def __repr__(self):
        return f"<Role(id={self.id}, name={self.name})>"
    
    
class Profile(Base):
    __tablename__ = "profiles"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship()
    
    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), nullable=False)
    tenant: Mapped["Tenant"] = relationship()
    
    roles: Mapped[List["Role"]] = relationship(secondary="profiles_roles")
    created_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    
    def __repr__(self):
        return f"<Profile(id={self.id}, user_id={self.user_id})>"
    
    
class Invitation(Base):
    __tablename__ = "invitations"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    code: Mapped[str] = mapped_column(String(4), nullable=False, unique=True)
    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"), nullable=False)
    tenant: Mapped["Tenant"] = relationship()
    
    created_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    
    def __repr__(self):
        return f"<Invitation(id={self.id}, email={self.email})>"