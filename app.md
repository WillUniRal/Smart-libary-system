
## auth {
    dec (FUNC){
        wrap (args){
            try {
                user object = request user object from server with sess
            } except key error {
                this means there is no user with that session
            } else {
                FUNC(args, user object)
            }
        }
    }
}

## login {
    set error to always same
    while True {
        get email and password
        check if email is in database if not print error
        login to server and get session
        if all successful return session
    }
}


## decorate with auth 
## open menu {
    user menu = create menu 
    while user is logged in {
        print the dash board
        open the user menu
        if last user menu to open was not log out then PAUSE before next options
    }
}

## main code
while True {
    sess = login()
    open_menu(sess)
}



    
