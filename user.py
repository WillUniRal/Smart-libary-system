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
        self.email = email
        self.__pass_word = bcrypt.hashpw(pass_word,bcrypt.hashpw())
        self.join_date = datetime.now()

    @property
    def name(self) :
        return self.first_name+" "+self.last_name
    
    def authenticate_pw(self,pw) :
        session = uuid.uuid4() if bcrypt.checkpw(pw,self.__pass_word) else None
        return session
            
    @abstractmethod
    def view_dashboard() :
        pass