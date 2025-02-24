from book import Book
from user import User
from datetime import date,timedelta

class Loan :
    def __init__(self, user : User, book : Book, days):
        self.user = user
        self.book = book
        self.issued_at = date.today()
        self.due_date = self.issued_at + timedelta(days=days)
        

