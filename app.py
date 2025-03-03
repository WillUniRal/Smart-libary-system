from member import Member
from librarian import Librarian
from getpass import getpass
from dataset import Server 

# Client console based for testing structure
# Has all functional requirements for end user 
def login() :
    email = input("Please enter your email: ")
    password = getpass()
    return email, password

if __name__ == "__main__" :
    credentials = login()
    server = Server()
    try :
        server.find_user(credentials[0])
    except :
        pass
    
