# Employee Management System

## Description
The Employee Management System is a simple application that allows you to manage employees and their associated departments. It provides functionality for creating, reading, updating, and deleting (CRUD) employee and department records using SQLAlchemy and a SQLite database.

## Project Structure
EmployeeManagementSystem/
│
├── main.py                # Main entry point for the project
├── models.py              # File to define database models
├── config.py              # Configuration file for database setup
└── requirements.txt       # List of required dependencies


## Features
- Create departments and employees
- Read and display department and employee records
- Update employee information
- Delete departments and associated employees

## Technologies Used
- Python
- SQLAlchemy
- SQLite
- Object-Oriented Programming (OOP)
- Design Patterns

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/ankitpakhale/EmployeeManagementSystem.git
   cd EmployeeManagementSystem
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     . .venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   python3 main.py
   ```

## Usage
- Follow the prompts in the console to enter department and employee details.
- Use the provided options to update or delete records as needed.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
Ankit Pakhale
