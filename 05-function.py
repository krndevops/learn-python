def sample():
    print("Hello World")

sample()


def sample1(x,y):
    print(x+y)

sample1(10, 20)
sample1(20, 30)

def namePrint(firstname, lastname):
   f = firstname.title()
   l = lastname.title()
   return (f"Hello {f} {l}")

   namePrint(firstname="John", lastname="Wesley")
   namePrint(lastname="Sarah", firstname="John")

   name=namePrint(lastname="Wesley", firstname="John")
   print(name)

