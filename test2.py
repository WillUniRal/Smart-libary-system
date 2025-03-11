# prompts

"""
I am creating a menu class that has the attributes
menus: which is a list of function names, 
args: that is a dictionary of the function name as its key and its value is its argumentsfor that menu.
how would I tag a function in another class so it could be used for a sub menu,
I tried decorators but they aren't called when the function is defined
"""

"""how to get the class name from Menu of the class that called the function"""

# responses are from qwen 2.5 that have been modified and tested 
class Menu:
    menus = []
    args = {}

    @classmethod
    def register(cls, **kwargs):
        """Decorator to register a function as a menu item with arguments."""
        def decorator(func):
            print(func.__qualname__)

            cls.menus.append(func.__name__)
            cls.args[func.__name__] = kwargs
            return func
        return decorator
    # modified qwen code where i was testing if __str__ could be used for classmethod (it does not work)
    def __str__(cls):
        return f"Menus: {cls.menus}\nArgs: {cls.args}"

# Another class with menu functions
class OtherClass:
    @Menu.register(arg1=5, arg2=10)  # Specify arguments here
    def my_menu_item(self, arg1, arg2):
        print(f"Function called with args: {arg1}, {arg2}")

    @Menu.register()  # No arguments needed
    def another_menu_item(self):
        print("Another function called")

# Usage example
if __name__ == "__main__":
    # Access registered functions and their arguments
    # print("Menus:", Menu.menus)  # Output: Menus: ['my_menu_item', 'another_menu_item']
    # print("Args:", Menu.args)    # Output: Args: {'my_menu_item': {'arg1': 5, 'arg2': 10}, ...}

    print(Menu) # Meta class needed, thats long i dont want to do that cos dull /test

    # To call a function, you need an instance of OtherClass
    obj = OtherClass()
    for func_name in Menu.menus:
        func = getattr(obj, func_name)
        func_args = Menu.args.get(func_name, {})
        func(**func_args)