from member import Member
from getpass import getpass
from dataset import server, UserNotFoundError,User

# Client console based for testing structure
# Has all functional requirements for end user 


def auth(func) :
    def wrapper(session,*args,**kwargs) :
        user = server.sessions[session]
        if user :
            func(*args,**kwargs,user=user)
        else :
            print("Unauthorised")
    return wrapper

def login() :
    
    error_msg = "The email or password entered is incorrect"
    while True :
        user_email = input("Please enter your email: ")
        password = getpass()

        try :
            user = server.find_user(user_email)
            if user is None : raise UserNotFoundError
        except UserNotFoundError as e :
            print(error_msg)
            # print(e.with_traceback())
            continue
        except:
            print(f"An unknown error occured, please try again")
            continue
        
        new_session = server.log_in(user,password)
        if new_session : return new_session
        else : 
            print(error_msg)
            continue

sess = login()

@auth(sess)
def open_menu(user : User = None):
    user.view_dashboard()

open_menu()



    
