class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def roll(self):
        print(self.name + ' is rolling!')

    def sit(self):
        print(self.name + ' is sitting!')

    def the_dog(self):
        print(self.name + ' is a ' + str(self.age) + '-year-old dog!')


my_dog = Dog('旺财', 9)
my_dog.the_dog()
my_dog.roll()
my_dog.sit()

print('*************************')


class PetDog(Dog):
    def __init__(self, name, age, belong):
        super().__init__(name, age)
        self.belong = belong

    def petDogBelong(self):
        print(self.name + ' belongs to ' + self.belong + '!')

    def the_dog(self):
        print('It\'s mine')


my_pet = PetDog('Fun', 3, 'ldl')
my_pet.sit()
my_pet.roll()
my_pet.the_dog()
my_pet.petDogBelong()
