from user import User
from datetime import date

class Member(User):
    def __init__(self, fname, lname, email, pass_word):
        super().__init__(fname, lname, email, pass_word)
        self.restricted_until = None
    def is_banned(self) :
        print(self.restricted_until)
        try :
            return date.today() > self.restricted_until
        except :
            return False
    def dashboard(self):
        if self.is_banned():
            return "You are banned until: "+ str(self.restricted_until)
        else :
            return f"Welcome {self.name}! \n"\
            + f"You currently have {len(self.loans)} book(s) Loaned \n"\
            + f"{len(self._notifications)} new notification(s)"
    
# jaylyn = Member("Jaylyn","Cruz","jaycee@gmail.com")
# print(jaylyn.dashboard())
        