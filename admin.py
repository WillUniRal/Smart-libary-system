
from datetime import date
from dateutil.relativedelta import relativedelta
from librarian import User,Member,Librarian
from librarian import Menu

class Admin(Librarian):
    def view_dashboard(self):
        return f"Welcome {self.name}! \n"\
        + "You currently have x book(s) Loaned \n"\
        + "x new notifications \n"\
        + "x new Library members this month"
    
    @property
    def sub_menu() :
        return super().sub_menu
    
    @Menu.sub_menu()
    def assign_role(self, object : User, user_class) :
        new_role = user_class(**vars(object))
        return new_role
    
    @Menu.sub_menu()
    def ban_user(self, member : Member, **timekws) :
        member.restricted_until = date.today() + relativedelta(**timekws)
    

        