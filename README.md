# Fall Semester Project

The goal of this project is to use object-oriented programming (OOP) concepts in Python to implements a simple system for managing a financial expenses. It includes two main classes: `Expense` and `ExpenseDatabase`.

## Table of Contents

- [Classes](#classes)
  - [Expense](#Expense)
  - [ExpenseDatabase](#ExpenseDatabase)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Creating Expense Instances](#creating-Expense-instances)
  - [Managing the ExpenseDatabase Database](#managing-the-ExpenseDatabase-database)

## Classes

### Expense

The `Expense` class represents an individual financial expense:

- `id`: A unique identifier generated as a UUID string.
- `title`: A string representing the title of the expense.
- `amount`: A float representing the amount of the expense.
- `created_at`: A timestamp indicating when the expense was created (UTC).
- `updated_at`: A timestamp indicating the last time the expense was updated (UTC).

#### Methods:

- `__init__(self, title, amount)`: Initializes the attributes.
- `update(self, title=None, amount=None)` : Allows updating the title and/or amount, updating the updated_at timestamp.
- `to_dict(self)` : Returns a dictionary representation of the expense.

### ExpenseDatabase

The `ExpenseDatabase` class manages a collection of Expense objects.

#### Attributes:

- `expenses` : A list storing Expense instances.

#### Methods:

- `__init__(self)` : Initializes a new `ExpenseDatabase` instance with an empty list of expenses.
- `add_expense(self, expense)` : Adds an expense.
- `remove_expense(self, expense_id)` : Removes an expense.
- `get_expense_by_id(self, expense_id)` : Retrieves an expense by ID.
- `get_expense_by_title(self, expense_title)` : Retrieves expenses by title.
- `to_dict(self)` : Returns a list of dictionaries representing expenses.


## Setup Instructions

### Prerequisites

- Python

```
https://www.python.org/downloads/
```
- Git

```
https://git-scm.com/
```

### Installation

* Clone the GitHub repository:

```
git clone https://github.com/emmlard/expense-manager-python.git
```
* Navigate into the expense-manager-python directory

```
cd expense-manager-python
```
* Run the python file

```
python3 expense.py
```

## Usage

### Creating Expense Instances

```
# Creating objects of the class Expense.
expense1 = Expense(title='Dining Out', amount=150)
expense2 = Expense(title='Entertanment', amount=150)
expense3 = Expense(title='Groceries', amount=450)
expense4 = Expense(title='Transportation', amount=100)
expense5 = Expense(title='Utilities', amount=1500)

# Updating the object
expense1.update(title='Entertianment')
expense4.update(amount=200)

# printing a dictionary representation of the expense.
# Create a list of expenses
expenses = [expense1, expense2, expense3, expense4, expense5]

for expense in expenses:
  print(expense.to_dict())
```

### Managing the ExpenseDatabase Database

```
# Creating an object of the class ExpenseDatabase.
expense_db = ExpenseDatabase()

# Create a list of expenses
expenses = [expense1, expense2, expense3, expense4, expense5]

# Adding expense to the database using .add_expense(expense) method.
for expense in expenses:
  expense_db.add_expense(expense)

# Removing expense from the database using .remove_expense(expense_id) method.
expense_db.remove_expense(expense_id)

# Get expense by the id using .get_expense_by_id(expense_id) method.
expense_db.get_expense_by_id(expense_id)

# Retrieves expenses by title using .get_expense_by_title(expense_title) method. This return a list of expense(s) with the expense_title provided.
expense_db.get_expense_by_title(expense_title)

# Returns the expense(s) in the database as list of dictionary.
expense_db.to_dict()
```


