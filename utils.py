class Menu:

    menus : list[str] = []
    arguments : dict[str,tuple] = {}
    premissions : dict[str,str] = {}

    @classmethod
    def sub_menu(cls, *args) :
        def decorator(func : callable) :
            # add the menu 
            cls.menus.append(func.__name__)
            # set up args and position
            cls.arguments[func.__name__] = args
            cls.premissions[func.__name__] = func.__qualname__.split(".")[0]

            return func
            
        return decorator
    
    @classmethod
    def debug_sub_menus(cls) :
        for func_name in cls.menus :
            print(f"Function: {func_name}\nBelongs to: {cls.premissions[func_name]}\nArgs:")
            for args in cls.arguments[func_name] : print(args)
                
    def __str__(cls) :
        result = "What would you like to do today: \n"
        for index, sub_menu in enumerate(cls.menus) :
            result += sub_menu.replace("_"," ").capitalize()
            result += ": "+str(index)+"\n"
            
        return result


