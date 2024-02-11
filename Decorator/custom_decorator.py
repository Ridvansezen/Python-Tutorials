def decorator(func):
    def function(*args, **kwargs):
        name = func(*args, **kwargs)
        print(f"Founction name : {func.__name__}")
        
        return name
        
    return function
