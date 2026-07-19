def decorate(func):
    def wrapper():
        print(' i will print myself before the function hello')
        func()
        print(' i will print after the function')
    return wrapper

@decorate
def hello():
    print("hello i am ruhul amin ")

hello()