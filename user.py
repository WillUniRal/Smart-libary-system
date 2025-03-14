from collections.abc import Callable
from book import Book
from abc import ABC, abstractmethod
from random import randint
from datetime import datetime

from utils import Menu

import bcrypt
import uuid

class User(ABC) :
    def __init__(self,first_name,last_name,email,pass_word,id=None,join_date=None,_notifications=None,loans=None,**kwargs) :
        self.first_name = first_name
        self.last_name = last_name
        self.id = self.init_attribute(id,randint(100000000,999999999))
        
        self.__email = email

        salt = bcrypt.gensalt()
        if isinstance(pass_word,str) : 
            pw_bytes = bytes(pass_word,encoding="utf-8")
            self.__pass_word = bcrypt.hashpw(pw_bytes,salt)
        else : 
            # the password has been recieved in bytes meaning
            # this is most likely a transfer so its already hashed
            self.__pass_word = pass_word
        self.join_date = self.init_attribute(join_date,datetime.now())

        self._notifications = self.init_attribute(_notifications,[])
        self.loans = self.init_attribute(loans,[])# : list[Loan]
        self.__session = None

    def init_attribute(self,arg,value) :
        if arg == None :
            return value
        else : return arg


    @property
    def name(self) :
        return self.first_name+" "+self.last_name
    
    @property
    def email(self) :
        return self.__email
    
    @property
    def permission(self) :
        return type(self).__name__
    
    @property 
    def logged_in(self):
        return True if self.__session else False
    
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


    # def dashboard(self):
    #     return f"Welcome {self.name}! \n"\
    #     + "You currently have x book(s) Loaned \n"\
    #     + "x new notifications"
        
    def authenticate_pw(self,pw) :
        pw = bytes(pw,encoding="utf-8")
        session = uuid.uuid4() if bcrypt.checkpw(pw,self.__pass_word) else None
        self.__session = session
        return session

    # def notif(self,func) :
    #     if self._notifications : return func
            
    @abstractmethod
    def dashboard() :
        pass
    
    def loan_alert(self,book : Book,day):
        self._notifications.append(f"The book \"{book.title}\" needs to be returned in {days(day)}")

    def get_loan(self) :
        if len(self.loans) <= 0 : return None
        print("Books currently loaned: ")
        while True :
            for index, loan in enumerate(self.loans,start=1) :
                print(f"{index}: {loan.book}")
            try :
                option = int(input("Select a book> "))
            except ValueError:
                print("Invalid option")
            else :
                if not 1 <= option <= len(self.loans) :
                    print("Not an option")
                    continue
                return self.loans[option-1]
    
    @Menu.sub_menu(True)
    def log_out(self):
        self.__session = None

    @Menu.sub_menu()
    def check_notifications(self) :
        if not self._notifications :
            print("You have no new notifications")
            return
        for notis in self._notifications :
            print(notis)

    @Menu.sub_menu()
    def book_search(self,search_for_titles_or_an_author,func):
        book : Book = func(search_for_titles_or_an_author)
        if book : book.info()

    @Menu.sub_menu()
    def return_a_book(self,loan):
        if loan is None :
            print("You dont have any books to return")
            return
        loan.hand_in()

def days(day):
    if day > 1 :
        return str(day)+" days"
    elif day > 0 :
        return str(day)+" day"
    else :
        return "today"


