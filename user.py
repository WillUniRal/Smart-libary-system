from book import Book
from abc import ABC, abstractmethod
from random import randint
from datetime import datetime

import bcrypt
import uuid

class User(ABC) :
    def __init__(self,fname,lname,email,pass_word) :
        self.first_name = fname
        self.last_name = lname
        self.id = randint(100000000,999999999)
        self.__email = email
        self.__pass_word = bcrypt.hashpw(pass_word,bcrypt.gensalt())
        self.join_date = datetime.now()
        self._notification = []

    @property
    def name(self) :
        return self.first_name+" "+self.last_name
    
    @name.setter
    def set_name(self, value) :
        if not isinstance(value,tuple) : raise ValueError("Only accepts type (tuple)")
        if value[0] : self.first_name = value[0]
        if value[1] : self.last_name = value[1]

    def view_dashboard(self):
        return f"Welcome {self.name}! \n"\
        + "You currently have x book(s) Loaned \n"\
        + "x new notifications"
        
        
    
    def authenticate_pw(self,pw) :
        session = uuid.uuid4() if bcrypt.checkpw(pw,self.__pass_word) else None
        return session
            
    @abstractmethod
    def view_dashboard() :
        pass
    
    def loan_alert(self,book : Book,day):
        self._notification.append(f"The book \"{book.title}\" needs to be returned in {days(day)}")

def days(day):
    if day > 1 :
        return str(day)+" days"
    elif day > 0 :
        return str(day)+" day"
    else :
        return "today"


