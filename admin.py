
from datetime import date
from dateutil.relativedelta import relativedelta
from librarian import User,Member,Librarian

class Admin(Librarian):
    def view_dashboard(self):
        return f"Welcome {self.name}! \n"\
        + "You currently have x book(s) Loaned \n"\
        + "x new notifications \n"\
        + "x new Library members this month"
    
    def assign_role(self, object : User, user_class) :
        new_role = user_class(**vars(object))
        return new_role
    
    def ban_user(self, member : Member, **timekws) :
        member.restricted_until = date.today() + relativedelta(**timekws)
    

        