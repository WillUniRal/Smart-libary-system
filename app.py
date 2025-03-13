from member import Member
from getpass import getpass
from dataset import server, UserNotFoundError,User
from user import Menu
# Client console based for testing structure
# Has all functional requirements for end user 


def auth(session) :
    def decorator(func) :
        def wrapper(*args,**kwargs) :
            try :
                user = server.sessions[session]
            except KeyError :
                print("Unauthorised")
            else :
                func(*args,**kwargs,user=user)
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

@auth(sess)
def open_menu(user : User = None):
    
    # Menu.debug_sub_menus()
    user_menu = Menu(user.permission,server,user)
    while user.logged_in :
        print(user.dashboard())
        user_menu.debug_sub_menus()
        user_menu.open()
        if user_menu.last_menu != "log_out" : input()

open_menu()



    
