class Menu:
    def __init__(self):
        self.arguments : dict[str,tuple] = {}
        self.menus : list[str] = []

    def sub_menu(self, func : callable) :
        def head_func(*args,**kwargs) :
            # add the menu 
            self.arguments[func.__name__] = args
            self.menus.append(func.__name__)
            # call func
            func(*args,**kwargs)
            
        return head_func
    
    def __str__(self) :
        result = "What would you like to do today: \n"
        for index, sub_menu in enumerate(self.menus) :
            result += sub_menu.replace("_"," ").capitalize()
            result += ": "+str(index)+"\n"
            
        return result


