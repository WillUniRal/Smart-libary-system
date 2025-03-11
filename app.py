from member import Member
from getpass import getpass
from dataset import server, UserNotFoundError,User
from user import Menu
# Client console based for testing structure
# Has all functional requirements for end user 


def auth(session) :
    def decorator(func) :
        def wrapper(*args,**kwargs) :
            print(session)
            for sessions in server.sessions.keys() :
                print("avalible:",sessions)
            user = server.sessions[session]
            if user :
                func(*args,**kwargs,user=user)
            else :
                print("Unauthorised")
        return wrapper
    return decorator

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

print(sess)

@auth(sess)
def open_menu(user : User = None):
    print(user.view_dashboard())
    Menu.debug_sub_menus()

open_menu()



    
