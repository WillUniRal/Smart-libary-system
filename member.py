from user import User

class Member(User):
    def __init__(self, fname, lname, email, pass_word):
        super().__init__(fname, lname, email, pass_word)
        self.restricted_until = None

    def view_dashboard(self):
        return f"Welcome {self.name}! \n"\
        + "You currently have x book(s) Loaned \n"\
        + "x new notifications"
    
# jaylyn = Member("Jaylyn","Cruz","jaycee@gmail.com")
# print(jaylyn.view_dashboard())
        