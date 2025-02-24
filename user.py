from abc import ABC, abstractmethod
from random import randint
from datetime import datetime

class User(ABC) :
    def __init__(self,fname,lname,email) :
        self.first_name = fname
        self.last_name = lname
        self.id = randint(100000000,999999999)
        self.email = email
        self.join_date = datetime.now()
    @property
    def name(self) :
        return self.first_name + " " +self.last_name
    @abstractmethod
    def view_dashboard() :
        pass