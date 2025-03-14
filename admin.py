
from datetime import date
from dateutil.relativedelta import relativedelta
from librarian import User,Member,Librarian
from librarian import Menu

class Admin(Librarian):
    def dashboard(self):
        return f"Welcome {self.name}! \n"\
        + f"You currently have {len(self.loans)} book(s) Loaned \n"\
        + f"{len(self._notifications)} new notification(s)"\
        + "x new Library members this month"
    
    @Menu.sub_menu()
    def assign_role(self, user : User, role) :
        classes = [Member,Librarian,Admin]
        role_class = next((cls for cls in classes if cls.__name__ == role), None)
        if role_class :
            new_role = globals()[role](**vars(user))
            return new_role
        else :
            print("Invalid Role")
            return None
    
    @Menu.sub_menu()
    def ban_member(self, member : Member, duration) :
        member.restricted_until = date.today() + relativedelta(**duration)
    
#testing
if __name__ == '__main__' :
    example = Admin("Vladlen","Voronov","blyat448@armyspy.com","Lebedinoe883")
    from dataset import server
    from loan import Loan
    from book import Book
    dababy = Book("les go","DaBaby",23423,"very cool book")
    server.catalogue.append(dababy)
    example.loans.append(Loan(example,dababy,5))
    admin_menu = Menu(example.permission,server,example)

    admin_menu.open()