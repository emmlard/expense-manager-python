from uuid import uuid4
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        """
        This function initializes the class Expense with the following attributes:
        id : UUID
            A unique identifier generated as a UUID string.
        title : str
            A string representing the title of the expense.
        amount : float
            A float representing the amount of the expense.
        created_at : datetime
            A timestamp indicating when the expense was created (UTC).
        updated_at : datetime
            A timestamp indicating the last time the expense was updated (UTC).
        """

        self.id = uuid4()
        self.title = str(title)
        self.amount = float(amount)
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        """
        This function allows updating the title and/or amount, updating the updated_at timestamp.
        """
        try:
            if title != None or amount != None:
                self.title = str(title) if title is not None else self.title
                self.amount = float(amount) if amount is not None else self.amount
                self.updated_at = datetime.utcnow()
                print(f"succesfully updated at {self.updated_at}")
            else:
                print(f'Please provide the attribute to update.')
        except (TypeError, ValueError):
            print(f"Provide a valid string as the title and/or a valid number as the amount.") 

    def to_dict(self):
        """
        This function returns a dictionary representation of the expense.
        """
        return {"id": str(self.id), "title": self.title, "amount": self.amount, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}


class ExpensesDatabase:
    def __init__(self):
        """
        This function initializes the class ExpensesDatabase with the following attributes:
        expenses : list
            A list storing Expense instances.
        """
        self.expenses = []

    def add_expense(self, expense):
        """
        This function adds an expense to the database.
        """
        self.expenses.append(expense.to_dict())

    def remove_expense(self, expense_id):
        """
        This function removes an expense from the database by ID.
        """
        for item in self.expenses:
            if item['id'] == expense_id:
                self.expenses.remove(item)
                print(f'expense_id with {expense_id} has been succesfully removed.')
                break
        else:
            print(f'expense_id wiith {expense_id} does not exist.')
            return None

    def get_expense_by_id(self, expense_id):
        """
        This function get an expense by ID.
        """
        for item in self.expenses:
            if item['id'] == expense_id:
                return item
        else:
            print(f'expense_id with {expense_id} does not exist.')
            return None 

    def get_expense_by_title(self, expense_title):
        """
        This function get expenses by title (returning a list).
        """
        matching_expenses = [item for item in self.expenses if item['title'] == expense_title]
        if matching_expenses:
            return matching_expenses
        else:
            print(f'expense_title with {expense_title} does not exist.')
            return None

    def to_dict(self):
        """
        This function returns a list of dictionaries representing each expense in the database.
        """
        return self.expenses