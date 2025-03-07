from member import Member
from getpass import getpass
from dataset import server, UserNotFoundError

# Client console based for testing structure
# Has all functional requirements for end user 



def login() :
    
    error_msg = "The email or password entered is incorrect"
    while True :
        user_email = input("Please enter your email: ")
        password = getpass()

        try :
            user = server.find_user(user_email)
        except UserNotFoundError as e :
            print(error_msg)
            # print(e.with_traceback())
            continue
        except:
            print(f"An unknown error occured, please try again")
            continue
        
        new_session = user.authenticate_pw(password)
        if new_session : return new_session
        else : 
            print(error_msg)
            continue
    


if __name__ == "__main__" :
    
    sess = login()
    
