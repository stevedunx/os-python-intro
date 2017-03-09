# Part 1

index = 4

def print_me(x):
    print("The number is {0}".format(x))

def print_index():
    print("The index is {0}".format(index))

def test_function():
    index = 999
    print_me(index)
    print_index()

test_function()

# Part 2

class Dog:
    def __init__(self, name, breed, isFriendly=True):
        self.name = name
        self.breed = breed
        self.isFriendly = isFriendly

    def make_doggy_sound(self):
        return "Woof!" if self.isFriendly else "Grrr..."       


dogs = []
dogs.append(Dog("Doge", "Shiba Inu", False))
dogs.append(Dog("Pupperino", "Russell Terrier"))
# You don't need to make dogs explicitly friendly, but you can if you want to...
dogs.append(Dog("Bo", "Portuguese Water Dog", True)) 
dogs.append(Dog(isFriendly=False, breed="Werewolf", name="Fenrir", False))

for dog in dogs:
    print(dog.name)
    print(dog.make_doggy_sound())
