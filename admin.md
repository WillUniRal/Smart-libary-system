
# class Admin inherits librarian {
##  ABSTRACT dashboard {
        display some user info
        display useful admin info
    }
##  @tagged: use as sub_menu()
##  assign role {
        for list of classes
        if role in list of classes {
            new_role = (get the role in globals)->contructerFunc(variables of object instance)
            return new_role
        } else { 
            print("Invalid Role")
            return None
        }
    }
    
##  @tagged: use as sub_menu()
##  ban member {
        set member restricted to the duration (kwargs: days=x, weeks=y, ...)
    }
# }