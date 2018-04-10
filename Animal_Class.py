class Animal(object):

    #Think Java constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.counter = 0

    #standard methods
    def printName(self):
        print(self.name)
        
    def birthday(self):
        birthday = "maybe"
        while(birthday != "yes"):
            self.counter = self.counter + 1
            #scanf/std::cin is same as input
            birthday = input("Is it his birthday? ")
            if(birthday == "yes"):
                print("Happy Birthday!")
                self.age = self.age + 1
            elif(birthday == "no"):
                if(self.counter == 10):
                    print("What don't you understand about this?"),
                print("Well maybe later")

    #standard getters and setters
    def getAge(self):
        print(self.age)

lion = Animal("Jim", 14)
lion.printName()
lion.birthday()
lion.getAge()
