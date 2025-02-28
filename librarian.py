from user import User
from loan import Loan

class Librarian(User):
    def view_dashboard(self):
        return f"Welcome {self.name}! \n"\
        + "You currently have x book(s) Loaned \n"\
        + "x new notifications"
    
    def approve_loan(self, user : User, book, days):
        if len(user.loans) > 3 :
            print("This user can't loan more than 2 books at once")
            return
        new_loan = Loan(user,book,days)
        user.loans.append(new_loan)

    

        