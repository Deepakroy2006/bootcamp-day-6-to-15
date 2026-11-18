from pydantic import BaseModel, EmailStr
from typing import Optional


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    salary: float
    department_id: int
    designation_id: int
    manager_id: Optional[int] = None


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    salary: Optional[float] = None
    department_id: Optional[int] = None
    designation_id: Optional[int] = None
    manager_id: Optional[int] = None


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    salary: float
    department_id: int
    designation_id: int
    manager_id: Optional[int] = None

    class Config:
        from_attributes = True