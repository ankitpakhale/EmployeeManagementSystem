from config import DatabaseConfig
from models import Base, Employee, Department
from sqlalchemy.exc import IntegrityError


def create_tables(session):
    """
    Creates the database tables for employees and departments.
    Drops existing tables first to avoid column errors.
    
    :param session: The database session.
    """
    # drop existing tables to avoid column conflicts
    Base.metadata.drop_all(session.bind)
    print("Existing tables dropped successfully.")
    Base.metadata.create_all(session.bind)
    print("Database tables created successfully.")


def create_department(session):
    """
    Creates departments in the database based on user input.

    :param session: The database session.
    """
    departments = input("Enter department names separated by commas (e.g., Engineering, Marketing): ").split(',')
    for dept_name in departments:
        dept_name = dept_name.strip()  # remove extra spaces
        try:
            department = Department(name=dept_name)
            session.add(department)
            session.commit()
            print(f"Department '{dept_name}' created successfully.")
        except Exception:
            session.rollback()
            print(f"Error: Department with name '{dept_name}' already exists.")


def read_departments(session):
    """
    Retrieves all department records from the database.

    :param session: The database session.
    """
    try:
        departments = session.query(Department).all()
        if departments:
            for department in departments:
                print(department)
        else:
            print("No departments found.")
    except Exception as e:
        print(f"Error reading departments: {e}")


def update_department(session, department_id, name):
    """
    Updates an existing department record.

    :param session: The database session.
    :param department_id: The ID of the department to update.
    :param name: Updated name of the department.
    """
    try:
        department = session.query(Department).filter_by(id=department_id).first()
        if department:
            department.name = name
            session.commit()
            print(f"Department {department_id} updated successfully.")
        else:
            print(f"Department with ID {department_id} not found.")
    except IntegrityError:
        session.rollback()
        print(f"Error: Department with name '{name}' already exists.")
    except Exception as e:
        session.rollback()
        print(f"Error updating department: {e}")


def delete_department(session, department_id):
    """
    Deletes a department and its associated employees from the database.
    
    :param session: The database session.
    :param department_id: The ID of the department to be deleted.
    """
    try:
        # Fetch the department to be deleted
        department = session.query(Department).filter(Department.id == department_id).first()

        if department:
            # Fetch and delete associated employees
            session.query(Employee).filter(Employee.department_id == department_id).delete()
            session.delete(department)
            session.commit()
            print(f"Department '{department.name}' and its associated employees deleted successfully.")
        else:
            print(f"Department with ID {department_id} not found.")
    except Exception as e:
        session.rollback()  # rollback on error
        print(f"Error deleting department: {e}")


def create_employee(session):
    """
    Creates a new employee record in the database based on user input.

    :param session: The database session.
    """
    first_name = input("Enter the first name of the employee: ")
    last_name = input("Enter the last name of the employee: ")
    email = input("Enter the email of the employee: ")
    department_id = int(input("Enter the department ID the employee belongs to: "))
    
    try:
        new_employee = Employee(first_name, last_name, email, department_id)
        session.add(new_employee)
        session.commit()
        print(f"Employee {new_employee} created successfully.")
    except IntegrityError:
        session.rollback()  # rollback the session in case of error
        print(f"Error: Employee with email '{email}' already exists.")
    except Exception as e:
        session.rollback()
        print(f"Error creating employee: {e}")


def read_employees(session):
    """
    Retrieves all employee records from the database along with their department.

    :param session: The database session.
    """
    try:
        employees = session.query(Employee).all()
        if employees:
            for employee in employees:
                print(f"{employee}, Department: {employee.department.name}")
        else:
            print("No employees found.")
    except Exception as e:
        print(f"Error reading employees: {e}")


def update_employee(session, employee_id):
    """
    Updates an existing employee record.

    :param session: The database session.
    :param employee_id: The ID of the employee to update.
    """
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if employee:
        print(f"Current details - First Name: {employee.first_name}, Last Name: {employee.last_name}, Email: {employee.email}, Department ID: {employee.department_id}")
        
        # Ask for updated details
        first_name = input("Enter the new first name (or press Enter to skip): ")
        last_name = input("Enter the new last name (or press Enter to skip): ")
        email = input("Enter the new email (or press Enter to skip): ")
        department_id = input("Enter the new department ID (or press Enter to skip): ")
        
        # Update fields only if user has provided new values
        if first_name:
            employee.first_name = first_name
        if last_name:
            employee.last_name = last_name
        if email:
            employee.email = email
        if department_id:
            employee.department_id = int(department_id)  # ensure it's an integer

        try:
            session.commit()
            print(f"Employee {employee_id} updated successfully.")
        except IntegrityError:
            session.rollback()
            print("Error: An employee with that email already exists.")
        except Exception as e:
            session.rollback()
            print(f"Error updating employee: {e}")
    else:
        print(f"Employee with ID {employee_id} not found.")


def delete_employee(session, employee_id):
    """
    Deletes an employee record from the database.

    :param session: The database session.
    :param employee_id: The ID of the employee to delete.
    """
    try:
        employee = session.query(Employee).filter_by(id=employee_id).first()
        if employee:
            session.delete(employee)
            session.commit()
            print(f"Employee {employee_id} deleted successfully.")
        else:
            print(f"Employee with ID {employee_id} not found.")
    except Exception as e:
        print(f"Error deleting employee: {e}")


def main():
    """
    The main entry point of the application.
    """
    # initialize the database configuration for PostgreSQL or SQLite
    db_config = DatabaseConfig(db_url="sqlite:///employees.db")  # Change to PostgreSQL as needed

    # create a session
    session = db_config.get_session()

    # drop existing tables and create new ones
    create_tables(session)

    # Example usage of CRUD operations for Department
    create_department(session)

    print("\nAll Departments:")
    read_departments(session)

    # Example usage of CRUD operations for Employee
    create_employee(session)

    print("\nAll Employees:")
    read_employees(session)

    # Update employee
    employee_id_to_update = int(input("Enter the employee ID to update: "))
    update_employee(session, employee_id_to_update)

    print("\nAll Employees after update:")
    read_employees(session)

    # Delete department
    department_id_to_delete = int(input("Enter the department ID to delete: "))
    delete_department(session, department_id_to_delete)

    print("\nAll Departments after deletion:")
    read_departments(session)

    # close the session and dispose of the connection
    session.close()
    db_config.close()


if __name__ == "__main__":
    main()
