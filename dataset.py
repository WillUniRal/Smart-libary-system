# from user import User
from book import Book
from uuid import UUID
from admin import Admin,Librarian,Member,User
# from builtins import LookupError

class UserNotFoundError(LookupError) : ...

class Server :
    def __init__(self):
        self.__users : dict[str,User] = {}
        self.catalogue : list[Book] = []

    def find_user(self, email) :
        user : User = None
        return self.__users[email]
            
    def register(self, *users : User) :
        for i,user in enumerate(users) :
            if isinstance(user,User) :
                print(f"(SERVER) {i}: Succefully registered {user.name}, welcome to the libary")
                self.__users[user.email] = user
            else :
                print(f"(SERVER) {i}: The user that was entered into the system is not a valid user")

    def find_book(self, search) :
        hits : dict[str,Book] = {}
        for books in self.catalogue :
            if search in books.title :
                hits[books.title] = books
            if search in books.author :
                hits[books.author] = books

        return hits
    
server = Server()

e1 = Member("Freya","Myers","girlbossfreya@superrito.com","123IloveStanley") # fake identity
e2 = Librarian("Kiyumi","Maida","kyotoshidosha@bytedigi.com","nekoNekoNiii") #emailfake.com
e3 = Admin("Vladlen","Voronov","blyat448@armyspy.com","Lebedinoe883")

server.register(e1,e2,e3)

