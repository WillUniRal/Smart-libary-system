from user import User

class Member(User):
    def view_dashboard(self):
        return """Welcome {self.name}!
        You currently have x book(s) Loaned
        x new notifications"""
        