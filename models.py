from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Department(Base):
    """
    Represents a department in the company.
    """
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    employees = relationship("Employee", back_populates="department")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Department(id={self.id}, name='{self.name}')>"

class Employee(Base):
    """
    Represents an employee in the company.
    """
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    department = relationship("Department", back_populates="employees")

    def __init__(self, first_name, last_name, email, department_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.department_id = department_id

    def __repr__(self):
        return f"<Employee(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}', department_id={self.department_id})>"
