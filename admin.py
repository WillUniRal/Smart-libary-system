from user import User

class Member(User):
    def view_dashboard(self):
        return f"Welcome {self.name}! \n"\
        + "You currently have x book(s) Loaned \n"\
        + "x new notifications"
    
# jaylyn = Member("Jaylyn","Cruz","jaycee@gmail.com")

# print(jaylyn.view_dashboard())
        