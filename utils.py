import inspect
from enum import IntEnum

class Permission(IntEnum) :
    USER = 0 # Default
    MEMBER = 1
    LIBRARIAN = 2
    ADMIN = 3

class Menu:

    menus : list[str] = []
    arguments : dict[str,tuple] = {}
    premissions : dict[str,Permission] = {}

    def __init__(self, perm : str, server):
        self.server = server
        self.premission = Permission[perm.upper()]
        self.len : int = 0

    @classmethod
    def sub_menu(cls) :
        def decorator(func) :
            if func.__name__ in cls.menus : return func
            # add the menu 
            cls.menus.append(func.__name__)
            # set up args
            sig = inspect.signature(func)
            params = sig.parameters
            # print(params)
            cls.arguments[func.__name__] = list(params.keys())[1:] # skip self
            # permission = name of the class it was called from
            caller_class : str = func.__qualname__.split(".")[0]
            cls.premissions[func.__name__] = Permission[caller_class.upper()]

            return func
            
        return decorator
    
    @classmethod
    def debug_sub_menus(cls) :
        # print(len(cls.menus)) 0 why? - fixed I wasn't calling decorator function 
        # Menu.sub_menu   ❌
        # Menu.sub_menu() ✅
        
        for func_name in cls.menus :
            print(f"Function: {func_name}\nBelongs to: {cls.premissions[func_name]}\nArgs:")
            for args in cls.arguments[func_name] : print(args)
                
    def __str__(self) :
        result = "What would you like to do today: \n"
        for index, sub_menu in enumerate(self.menus,start=1) :
            if self.premission < self.premissions[sub_menu] : break
            result += sub_menu.replace("_"," ").capitalize()
            result += ": "+str(index)+"\n"
        self.len = index
        return result.rstrip("\n")
    
    def open(self) :
        option = self.get_choice()-1
        sub_m = self.menus[option]
        self.get_args(sub_m)

    def arg_search(self,arg,func) :
        while True :
            argy = func(input(f"Search for a {arg}: "))
            if argy is None :
                print(f"No {arg} found")
                continue
            else :
                return argy

    def get_args(self,func_key) :
        args = []
        for arg in self.arguments[func_key] :
            if arg == "user":
                args.append(self.arg_search(arg,self.server.get_user))
            elif arg == "duration" :
                # do something extra
                pass
            elif arg == "book" :
                args.append(self.arg_search(arg,self.server.get_book))
            elif arg == "func" :
                args.append(self.server.get_book)
            else :
                n = "n" if arg[0] in ('a','e,','i','o') else ""
                args.append(input(f"Enter a{n} {arg}: "))
        return args

    def get_choice(self) :
        while True :
            print(self)
            try :
                choice = int(input(">"))
            except ValueError :
                print("Invalid choice")
                continue
            if not 1 <= choice <= self.len:
                print("Option not avalible")
                continue
            return choice
            



