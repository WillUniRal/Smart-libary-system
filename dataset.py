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
        self.sessions : dict[UUID,User] = {}

    def find_user(self, email) :
        user : User = None
        try :
            user = self.__users[email]
        except KeyError:
            return None
        return user
    
    def get_names(self) :
        result : dict[str,User]= {}
        for user in self.__users.values() :
            result[user.name] = user
        return result
    
    def search_names(self,search : str) :
        hits = {}
        for key, value in self.get_names().items():
            if search.lower() in key.lower() :
                hits[key] = value
        return hits
    
    def get_user(self,name) :
        search_result = self.search_names(name)
        hits = list(enumerate(search_result.keys(),start=1))

        if not hits :
            print("No users found")
            return None
        
        while True :
            
            for index, names in hits :
                print(f"{index}: {names}")
            try :
                option = int(input("Which result:"))
            except ValueError :
                print("invalid option")
                continue
            else :
                if not 1 <= option <= len(hits) : 
                    print("Not an option")
                    continue
                return search_result[hits[option-1][1]]

    def log_in(self, user : User, pw) :
        session = user.authenticate_pw(pw)
        if session :
            self.sessions[session] = user
            return session
        else :
            return None
            
    def register(self, *users : User) :
        for i,user in enumerate(users) :
            if isinstance(user,User) :
                print(f"(SERVER) {i}: Succefully registered {user.name}, welcome to the libary")
                self.__users[user.email] = user
            else :
                print(f"(SERVER) {i}: The user that was entered into the system is not a valid user")

    def find_book(self, search : str) :
        hits : dict[str,Book] = {}
        for books in self.catalogue :
            if search.lower() in books.title.lower() :
                hits[books.title] = books
            if search in books.author.lower() :
                hits[books.author] = books

        return hits
    
    def get_book(self,srch) :
        # print(self.catalogue)
        books = self.find_book(srch)
        if not books :
            print("No books found")
            return None
        
        while True :
            
            booky = []
            for index, book in enumerate(books.values(),start=1) :
                print(f"{index}: {book}")
                booky.append(book)
            try :
                option = int(input("Which result: "))
            except ValueError :
                print("Invalid option")
                continue
            else :
                if not 1 <= option <= len(booky) :
                    print("Not an option")
                    continue
                return booky[option-1]
                

    
server = Server()

e1 = Member("Freya","Myers","girlbossfreya@superrito.com","123IloveStanley") # fake identity
e2 = Librarian("Kiyumi","Maida","kyotoshidosha@bytedigi.com","nekoNekoNiii") #emailfake.com
e3 = Admin("Vladlen","Voronov","blyat448@armyspy.com","Lebedinoe883")

server.register(e1,e2,e3)

