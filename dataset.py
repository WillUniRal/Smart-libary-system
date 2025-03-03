from user import User
from book import Book
from builtins import LookupError

class UserNotFoundError(LookupError) : ...

class Server :
    def __init__(self):
        self.__users : list[User] = []
        self.catalogue : list[Book] = []

    def find_user(self, email) :
        for user in self.__users :
            if user.email == email :
                return user
        raise UserNotFoundError
            
    def register(self, user : User) :
        self.__users.append(user)

    def find_book(self, search) :
        hits : dict[str,Book] = {}
        for books in self.catalogue :
            if search in books.title :
                hits[books.title] = books
            if search in books.author :
                hits[books.author] = books

        return hits