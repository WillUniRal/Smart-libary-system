from __future__ import annotations
from book import Book
from user import User
from datetime import date
from dateutil.relativedelta import relativedelta

class Loan :
    def __init__(self, user : User, book : Book, days):
        self.user = user
        self.book = book
        self.issued_at = date.today()
        self.due_date = self.issued_at + relativedelta(days=days)

    @property
    def days_due_in(self) :
        return (self.issued_at - self.due_date).days

    def send_notification(self) :
        self.user.loan_alert(self.book,self.days_due_in)

    def hand_in(self) :
        self.book.return_book()
        self.user.loans.remove(self)
        

        

