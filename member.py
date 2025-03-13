from user import User

class Member(User):
    def __init__(self, fname, lname, email, pass_word):
        super().__init__(fname, lname, email, pass_word)
        self.restricted_until = None

    def dashboard(self):
        return f"Welcome {self.name}! \n"\
        + f"You currently have {len(self.loans)} book(s) Loaned \n"\
        + f"{len(self._notifications)} new notification(s)"
    
# jaylyn = Member("Jaylyn","Cruz","jaycee@gmail.com")
# print(jaylyn.dashboard())
        