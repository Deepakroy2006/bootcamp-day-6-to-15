from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Employee Management API")

@app.get("/")
def home():
    return {"message": "Employee Management API is running successfully"}

class Employee(BaseModel):
    name: str
    email: EmailStr
    department: str
    designation: str
    salary: float


employees = [
    {
        "employee_id": 1,
        "name": "Deepak Kumar",
        "email": "deepak@example.com",
        "department": "IT",
        "designation": "Software Developer",
        "salary": 45000
    },
    {
        "employee_id": 2,
        "name": "Aman Kumar",
        "email": "aman@example.com",
        "department": "HR",
        "designation": "HR Executive",
        "salary": 40000
    }
]


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee

    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/employees", status_code=201)
def create_employee(employee: Employee):
    new_id = max([e["employee_id"] for e in employees], default=0) + 1

    new_employee = {
        "employee_id": new_id,
        **employee.model_dump()
    }

    employees.append(new_employee)

    return new_employee


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    for index, existing_employee in enumerate(employees):
        if existing_employee["employee_id"] == employee_id:

            updated_employee = {
                "employee_id": employee_id,
                **employee.model_dump()
            }

            employees[index] = updated_employee
            return updated_employee

    raise HTTPException(status_code=404, detail="Employee not found")


@app.patch("/employees/{employee_id}")
def patch_employee(employee_id: int, employee: dict):
    for existing_employee in employees:
        if existing_employee["employee_id"] == employee_id:

            existing_employee.update(employee)
            return existing_employee

    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: int):
    for index, employee in enumerate(employees):
        if employee["employee_id"] == employee_id:
            employees.pop(index)
            return

    raise HTTPException(status_code=404, detail="Employee not found")




#  uvicorn main:app --reload





