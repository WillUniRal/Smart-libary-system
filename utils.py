import inspect
from enum import IntEnum
# from user import User

class Permission(IntEnum) :
    USER = 0 # Default
    MEMBER = 1
    LIBRARIAN = 2
    ADMIN = 3

class Menu:
    # (name of function, function itself)
    menus : list[tuple] = []
    end_menu : tuple = ()
    arguments : dict[str,tuple[str]] = {}
    premissions : dict[str,Permission] = {}

    def __init__(self, perm : str, server, user):
        self.server = server
        self.premission = Permission[perm.upper()]
        self.len : int = 0
        self.user = user
        if not self.end_menu[0] in str(self.menus) :
            self.menus.append(self.end_menu)
            self.push_func(self.end_menu[1])
        self.menus = self.get_avalible_commands()
        self.last_menu = None

    @classmethod
    def sub_menu(cls,end=False) :
        def decorator(func) :
            if func.__name__ in str(cls.menus) : return func
            # add the menu 
            if end : 
                cls.end_menu = (func.__name__,func)
                return func
            
            cls.menus.append((func.__name__,func))
            cls.push_func(func)

            return func

        return decorator
        
    @classmethod 
    def push_func(cls,func) :
        # set up args
            sig = inspect.signature(func)
            params = sig.parameters
            # print(params)
            cls.arguments[func.__name__] = list(params.keys())[1:] # skip self
            # permission = name of the class it was called from
            caller_class : str = func.__qualname__.split(".")[0]
            cls.premissions[func.__name__] = Permission[caller_class.upper()]
    
    
    @classmethod
    def debug_sub_menus(cls) :
        # print(len(cls.menus)) 0 why? - fixed I wasn't calling decorator function 
        # Menu.sub_menu   ❌
        # Menu.sub_menu() ✅
        
        for func_name in cls.menus :
            func_name = func_name[0]
            print(f"Function: {func_name}\nBelongs to: {cls.premissions[func_name]}\nArgs:")
            for args in cls.arguments[func_name] : print(args)
                
    def __str__(self) :
        result = "What would you like to do today: \n"
        # menus = self.get_avalible_commands()
        for index, sub_menu in enumerate(self.menus,start=1) :
            sub_menu = sub_menu[0]
            result += sub_menu.replace("_"," ").capitalize()
            result += ": "+str(index)+"\n"
        self.len = index
        return result.rstrip("\n")
    
    def get_avalible_commands(self) :
        commands = []
        for sub_menu in self.menus :
            key = sub_menu[0]
            # permission u hav 0 < 1 permission for command
            if self.premission < self.premissions[key] : continue
            commands.append(sub_menu)
        return commands

    
    def open(self) :
        option = self.get_choice()-1
        sub_m = self.menus[option][0]
        args = self.get_args(sub_m)
        # print(args)
        self.last_menu = self.menus[option][0]
        returned_val = self.menus[option][1](self.user,*args)
        if isinstance(returned_val,tuple) :
            self.server.register(returned_val[1])


    def arg_search(self,arg,func) :
        while True :
            argy = func(input(f"Search for a {arg}: "))
            if argy is None :
                print(f"No {arg} found")
                continue
            else :
                return argy

    def get_args(self,func_key) :
        args= []
        for arg in self.arguments[func_key] :
            if arg == "user" or arg == "member":
                args.append(self.arg_search(arg,self.server.get_user))
            elif arg == "duration" :
                while True :
                    durkws = input("Enter a duration: ").replace(" ","").lower()
                    kwargs = durkws.split(",")
                    duration_dict = []
                    try :
                        for kw_eq_val in kwargs :
                            kw_val = kw_eq_val.split("=")
                            kw_val[1] = int(kw_val[1])
                            if not kw_val[0] in ('days','weeks','months','years') : raise ValueError
                            duration_dict.append(kw_val)
                    except :
                        print("SyntaxError: days=x,weeks=y...")
                        continue
                    else:
                        args.append(dict(duration_dict))
                        break
            elif arg == "book" :
                args.append(self.arg_search(arg,self.server.get_book))
            elif arg == "loan" :
                args.append(self.user.get_loan())
            elif arg == "func" :
                args.append(self.server.get_book)
            else :
                n = "n" if arg[0] in ('a','e,','i','o') else ""
                args.append(input(f"Enter a{n} {arg.replace("_"," ")}: "))
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
            



