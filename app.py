from member import Member
from librarian import Librarian
from getpass import getpass

# Client console based for testing structure
# Has all functional requirements for end user 
def login() :
    email = input("Please enter your email: ")
    password = getpass()

if __name__ == "__main__" :

    login()
    
