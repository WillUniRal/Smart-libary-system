from user import User
from datetime import date

class Member(User):
    def __init__(self, first_name,last_name,email,pass_word,**kwargs):
        super().__init__(first_name,last_name,email,pass_word,**kwargs)
        self.restricted_until = None
    def is_banned(self) :
        
        if self.restricted_until == None :
            return False
        return date.today() < self.restricted_until
            
    def dashboard(self):
        if self.is_banned():
            return "You are banned until: "+ str(self.restricted_until)
        else :
            return f"Welcome {self.name}! \n"\
            + f"You currently have {len(self.loans)} book(s) Loaned \n"\
            + f"{len(self._notifications)} new notification(s)"
    
# jaylyn = Member("Jaylyn","Cruz","jaycee@gmail.com")
# print(jaylyn.dashboard())
        