# from __future__ import annotations
from member import Member,User
from loan import Loan
from user import Menu

class Librarian(Member):
    def dashboard(self):
        return f"Welcome {self.name}! \n"\
        + f"You currently have {len(self.loans)} book(s) Loaned \n"\
        + f"{len(self._notifications)} new notification(s)"
    
    @Menu.sub_menu()
    def approve_loan(self, user : User, book, amount_of_days):
        try :
            amount_of_days = int(amount_of_days)
        except ValueError :
            print("invalid amount of days")
            
        if len(user.loans) > 3 :
            print("This user can't loan more than 2 books at once")
            return
        new_loan = Loan(user,book,amount_of_days)
        user.loans.append(new_loan)

    

        