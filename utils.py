import inspect
from enum import Enum

class Permission(Enum) :
    USER = 1
    LIBRARIAN = 2
    ADMIN = 3

class Menu:

    menus : list[str] = []
    arguments : dict[str,tuple] = {}
    premissions : dict[str,Permission] = {}

    def __init__(self, perm : str):
        self.premission = Permission[perm.upper()]

    @classmethod
    def sub_menu(cls) :
        def decorator(func) :
            # add the menu 
            cls.menus.append(func.__name__)
            # set up args
            sig = inspect.signature(func)
            params = sig.parameters
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
        for index, sub_menu in enumerate(self.menus) :
            if self.premission < self.premissions[sub_menu] : return
            result += sub_menu.replace("_"," ").capitalize()
            result += ": "+str(index)+"\n"
            
        return result


