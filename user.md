
# ABSTRACT class User {
##  constructor {
        1. set fname and lname
        2. make random id
        3. set email

        4. password, encrypt it

        5. set join date to today
        6. set misc
    }

##  name property {
        add fname and lname then return
    }
    
##  email getter 
    
##  permissions {
        return the name of the class
    }
    
##  logged in bool {
        return if there is or isn't a session
    }
    
##  name setter {
        one function to set
        check if instance is tuple
        name = (fname, lname) 
    }

##  email setter 

##  authenticate password {
        check pw with pw private attribute
        return the session if successful
    }
            
##  define ABSTRACT dashboard {pass}
    
##  loan alert {
        adds alert to notif
    }

##  get loan {
        1. get choice from inputs
        2. select loan using choice
        3. return loan
    }
    
##  @tagged: use as sub_menu(ending menu is true)
##  log out {
        set session to none
    }

##  @tagged: use as sub_menu()
##  check notis {
        if no notis print no notis
        else for each noti in notis and print noti
    }

##  @tagged: use as sub_menu()
##  book search {
        get the function for searching for a book in server
        book : Book = function(search term) 
        call book.info() (duck typing)
    }

##  @tagged: use as sub_menu()
##  return book {
        check if loan arg is empty
        if not call hand in on loan
##  }
# }

## days helper {
    return if today,
    if multiple (days)
    if single (day)
}

