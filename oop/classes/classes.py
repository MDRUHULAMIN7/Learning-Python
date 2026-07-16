class Factory:
    a = 12 #attribute 
    def hello(self): #method
        print("how are you")

    print("I am getting Initialized ")

# print(Factory().a)

Factory().hello()

ruhul = Factory()

print(ruhul.a)