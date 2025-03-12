from collections.abc import Callable
from book import Book
from abc import ABC, abstractmethod
from random import randint
from datetime import datetime
# from utils import get_caller

# # print("name:",get_caller())
# # if get_caller() != "loan" :
# #     from loan import Loan

from utils import Menu

import bcrypt
import uuid

class User(ABC) :
    def __init__(self,fname,lname,email,pass_word) :
        self.first_name = fname
        self.last_name = lname
        self.id = randint(100000000,999999999)
        self.__email = email

        salt = bcrypt.gensalt()
        if isinstance(pass_word,str) : pw_bytes = bytes(pass_word,encoding="utf-8")

        self.__pass_word = bcrypt.hashpw(pw_bytes,salt)

        self.join_date = datetime.now()
        self._notification = []
        self.loans = [] # : list[Loan]
        self.__session = None

    @property
    def name(self) :
        return self.first_name+" "+self.last_name
    
    @property
    def email(self) :
        return self.__email
    
    @name.setter
    def name(self, value) :
        if not isinstance(value,tuple) : raise ValueError("Only accepts type (tuple)")
        if value[0] : self.first_name = value[0]
        if value[1] : self.last_name = value[1]
        # name = 

    @email.setter
    def email(self, value) :
        #send confirmation email
        self.email = value


    # def view_dashboard(self):
    #     return f"Welcome {self.name}! \n"\
    #     + "You currently have x book(s) Loaned \n"\
    #     + "x new notifications"
        
    def authenticate_pw(self,pw) :
        pw = bytes(pw,encoding="utf-8")
        session = uuid.uuid4() if bcrypt.checkpw(pw,self.__pass_word) else None
        self.__session = session
        return session
            
    @abstractmethod
    def view_dashboard() :
        pass
    
    def loan_alert(self,book : Book,day):
        self._notification.append(f"The book \"{book.title}\" needs to be returned in {days(day)}")

    @Menu.sub_menu()
    def book_search(self,name,author,func : Callable = print):
        func(name,author)

    @Menu.sub_menu()
    def return_a_book(self,loan,book : Book):
        book.return_book()



def days(day):
    if day > 1 :
        return str(day)+" days"
    elif day > 0 :
        return str(day)+" day"
    else :
        return "today"


