# class Server {
##  constructor {
        1. initialize users dictionary (private)
        2. initialize catalogue list
        3. initialize sessions dictionary
    }

##  add books method {
        iterate over each book in books
        if book is valid (instance of Book) {
            add book to catalogue
            print success message
        } else {
            print failure message
        }
    }

##  find user method {
        1. try to retrieve user from users dictionary using email
        2. if KeyError occurs, return None
        3. return user if found
    }

##  get names method {
        1. create result dictionary
        2. iterate over users dictionary
        3. add user's name and instance to result
        4. return result
    }

##  search names method {
        1. call get names to retrieve all names
        2. iterate over names
        3. check if search term is in name (case-insensitive)
        4. add matching names to hits dictionary
        5. return hits
    }

##  get user method {
        1. call search names with given name
        2. enumerate results and display options
        3. prompt user to select an option
        4. validate input
        5. return selected user
    }

##  log in method {
        authenticate user with password
        if authentication successful {
            store session in sessions dictionary
            return session
        } else {
            return None
        }
    }

##  register method {
        iterate over each user in users
        if user is valid (instance of User){
            add user to users dictionary
            print success message
        } else {
            a. print failure message
        }
    }

##  find book method {
        1. iterate over catalogue
        2. check if search term matches book title or author (case-insensitive)
        3. add matching books to hits dictionary
        4. return hits
    }

##  get book method {
        1. call find book with search term
        2. if no books found, print message and return None
        3. enumerate results and display options
        4. prompt user to select an option
        5. validate input
        6. return selected book
    }
# }

# Custom Exception Class
class UserNotFoundError extends LookupError { ... }

# Main Program Logic
server = new Server()

# Create Users
## e1 = new Member(
    fname="Freya",                # First name of the member
    lname="Myers",                # Last name of the member
    email="girlbossfreya@superrito.com",  # Email address of the member
    password="123IloveStanley"    # Password for the member's account
)

## e2 = new Librarian(
    fname="Kiyumi",               # First name of the librarian
    lname="Maida",                # Last name of the librarian
    email="kyotoshidosha@bytedigi.com",  # Email address of the librarian
    password="nekoNekoNiii"       # Password for the librarian's account
)

## e3 = new Admin(
    fname="Vladlen",              # First name of the admin
    lname="Voronov",              # Last name of the admin
    email="blyat448@armyspy.com", # Email address of the admin
    password="Lebedinoe883"       # Password for the admin's account
)

# Create Books
## b1 = new Book(
    title="Less goooo",           # Title of the book
    author="Da Baby",             # Author of the book
    pages=3432,                   # Number of pages in the book
    description="I just signed a deal, I'm on\nYeah, yeah \nI go where I want \nGood, good"  # Description of the book
)

## b2 = new Book(
    title="The Hunger Games",     # Title of the book
    author="Suzanne Collins",     # Author of the book
    pages=123,                    # Number of pages in the book
    description="2 people from 12 districts, Fight to the death, only one can survive"  # Description of the book
)

## b3 = new Book(
    title="Harry Potter",         # Title of the book
    author="J.K Rowling",         # Author of the book
    pages=934,                    # Number of pages in the book
    description="You're a wizard harry"  # Description of the book
)

# Register Users
server register(ei)

# Add Books
server add books(bi)