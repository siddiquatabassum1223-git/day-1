# OOP Employee Management System

A command-line Employee Management System built with core Python —
demonstrating Object-Oriented Programming, exception handling, file
handling (JSON), and a clean modular package structure.

## Features

- **OOP-based design**: `Employee` base class with `Manager` and `HR`
  subclasses (inheritance, polymorphism, encapsulation, abstraction)
- **Full CRUD**: add, view, search, update, and delete employees
- **JSON persistence**: employee records are saved to and loaded from
  `data/employees.json`
- **Custom exceptions**: `InvalidEmployeeIDError`, `DuplicateEmployeeIDError`,
  `EmployeeNotFoundError`, `InvalidSalaryError`
- **Salary & bonus calculator**: bonus rate varies by role (polymorphism)
- **Action logging**: every add/update/delete is timestamped in `data/logs.txt`
- **Menu-driven CLI** (`main.py`) plus a **non-interactive demo script**
  (`demo.py`) that seeds data and exercises every feature end-to-end
- **Unit tests** (`tests.py`) covering models and the manager service

## OOP Principles Demonstrated

| Principle     | Where                                                                 |
|----------------|------------------------------------------------------------------------|
| Encapsulation  | `email` and `salary` are private-style attributes accessed via properties, validated on every write |
| Inheritance    | `Manager` and `HR` inherit from `Employee`                            |
| Polymorphism   | `calculate_bonus()` behaves differently per subclass; `HR` overrides it entirely |
| Abstraction    | `EmployeeManager` exposes simple methods (`add_employee`, `search_employee`, …) without exposing JSON I/O details to the caller |

## Project Structure

```
employee_system/
├── main.py                   # Interactive CLI entry point
├── demo.py                   # Non-interactive demo / seed script
├── tests.py                  # Unit tests
├── requirements.txt
├── README.md
│
├── models/
│   └── employee.py           # Employee, Manager, HR classes
│
├── services/
│   └── employee_manager.py   # EmployeeManager: CRUD + JSON persistence
│
├── utils/
│   ├── validator.py          # Field validation helpers
│   ├── helper.py             # Formatting, logging, misc helpers
│   └── exceptions.py         # Custom exception classes
│
└── data/
    ├── employees.json        # Employee database (JSON)
    └── logs.txt              # Action log (created at runtime)
```

## Setup & Usage

1. **No external dependencies are required** — this project uses only the
   Python standard library. (See `requirements.txt`.)

2. **Run the interactive CLI:**

   ```bash
   cd employee_system
   python main.py
   ```

   Menu options: Add / View / Search / Update / Delete / Exit.

3. **Run the demo script** (seeds sample data and prints a full walkthrough,
   useful for a quick end-to-end demonstration):

   ```bash
   python demo.py
   ```

4. **Run the unit tests:**

   ```bash
   python -m unittest tests.py -v
   ```

## Sample Salary Slip Output

```
========================================
Employee ID   : EMP002
Name          : Anita Sharma
Role          : Manager
Email         : anita.sharma@example.com
Department    : Engineering
Experience    : 6.0 year(s)
Base Salary   : ₹80,000.00
Bonus         : ₹24,000.00
Total Salary  : ₹104,000.00
========================================
```

## Validation Rules

- **Employee ID**: must match `EMP` followed by digits (e.g. `EMP001`); must be unique
- **Email**: must be a valid email format
- **Salary**: must be a positive number
- **Experience**: must be zero or a positive number

## Exception Handling

- `InvalidEmployeeIDError` — malformed employee ID
- `DuplicateEmployeeIDError` — employee ID already exists
- `EmployeeNotFoundError` — update/delete target does not exist
- `InvalidSalaryError` — invalid salary or experience value
- File-not-found on first run is handled gracefully — the system starts
  with an empty roster instead of crashing

## Code Quality Standards

- Meaningful variable and function names
- PEP 8 formatting throughout
- Docstrings and inline comments where logic isn't self-evident
- Business logic separated across `models/`, `services/`, and `utils/`
- No duplicated logic — shared validation and formatting live in `utils/`
- All expected failure paths wrapped in specific, custom exceptions

## Git Workflow

```bash
git checkout development
git pull origin development
git checkout -b feature/oop-employee-system
```

Commit messages used:

```
feat: implement Employee class
feat: add EmployeeManager CRUD operations
feat: implement JSON data storage
feat: add salary bonus calculation
```

Push and open a Pull Request from `feature/oop-employee-system` into `development`.
