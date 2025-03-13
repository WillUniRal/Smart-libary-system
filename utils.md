# enum Permission {
##  values {
        USER = 0
        MEMBER = 1
        LIBRARIAN = 2
        ADMIN = 3
    }
# }

# class Menu {

##  class variables 
    menus 
    end menu
    arguments
    permissions 
    

##  constructor {
        1. set server and user instances
        2. convert perm to uppercase and set as Permission enum
        3. check if end menu exists in menus, add if missing
        4. filter available commands based on permissions
    }

##  @classmethod sub menu( end is default as false ) {
        1. decorator function to register menu commands
        2. check if function already exists in menus
        3. if end flag: set as end menu
        4. else: add to menus and register function
    }

##  @classmethod push func(func) {
        1. get function parameters using reflection
        2. store arguments in arguments dict (skip 'self')
        3. determine caller class from qualified name
        4. map function to corresponding Permission level
    }

##  @classmethod debug sub menus() {
        1. iterate through registered menus
        2. print function permissions and arguments
    }

##  string representation {
        1. build menu display string
        2. format options with numbers
        3. track menu length
    }

##  get available commands  {
        1. filter menus based on user permission level
        2. return accessible commands
    }

##  open  {
        1. get user choice
        2. retrieve selected function and arguments
        3. execute selected menu command
    }

##  arg search(arg, search func) {
        1. prompt user for search input
        2. validate search results
        3. return valid result
    }

##  get args  {
        1. resolve required arguments for function
        2. handle special cases (user, book, loan)
        3. collect user inputs
    }

##  get choice {
        1. display menu
        2. validate user input
        3. return choice between 1 and len
    }
# }