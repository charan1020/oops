#decorator is a special type of function that modifies the behavior of another function or method.
def add_sprinkles(func):#add_sprinkles is the decorator function
    def wrapper(*args,**kwargs):#wrapper function is used to wrap the original function
        print("Adding sprinkles 🍫🍫...")
        func(*args,**kwargs)
        print("Sprinkles added!")
    return wrapper
def add_fudge(func):#add_fudge is another decorator function
    def wrapper(*args,**kwargs):#wrapper function is used to wrap the original function
        print("Adding fudge...")
        func(*args,**kwargs)
        print("Fudge added!")
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream🍨")   

get_ice_cream("vanilla")