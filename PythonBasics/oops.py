# OOPS

# Class and Object in Python
# this is a simple calculator class with basic operations
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


# this is how we create an object of a class
calc = Calculator()
print("Addition of 1 & 2 is: ", calc.add(1, 2))
print("Substraction of 2 & 1 is: ", calc.subtract(2, 1))
print("Multiplication of 2 & 3 is: ", calc.multiply(2, 3))
print("Division of 6 & 2 is: ", calc.divide(6, 2))


# Constructor in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


# here we are creating an object of the Person class
person1 = Person("Raviprasad", 25)
person2 = Person("Alice", 21)

# calling the display method
person1.display()
person2.display()


# Inheritance in Python
# Base class
class Animal:
    def speak(self):
        print("This animal makes a sound")


# Derived class
class Dog(Animal):
    def speak(self):
        print("This animal barks")


# Derived class
class Cat(Animal):
    def specialty(self):
        print("This animal is very agile")


# creating objects of the derived classes
dog = Dog()
cat = Cat()

# calling methods
print("Dog-speak: ", dog.speak())  # Output: This animal barks
print("Cat-speak: ", cat.speak())  # Output: This animal makes a sound
print("Cat-specialty: ", cat.specialty())  # Output: This animal is very agile


# Polymorphism in Python
# polymorphism is the ability to use a common interface for multiple forms (data types).
# creating two classes with the same method name
class DogFeatures:
    def walk(self):
        return str(self.__class__.__name__), " walks on 4 legs"


class BirdFeatures:
    def walk(self):
        return str(self.__class__.__name__), " walks on 2 legs"


# function that takes an object and calls its fly method
def animal_walk(animal):
    return animal.walk()


# creating objects
dog_features = DogFeatures()
bird_features = BirdFeatures()

# calling the walk method on different objects
print(animal_walk(dog_features))
print(animal_walk(bird_features))


# Encapsulation in Python
# here we are creating a class with private attributes and methods
# here __ before the attribute makes it private
# here __ before the method makes it private
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# creating an object of BankAccount
account1 = BankAccount(123, 1000)
account2 = BankAccount(456, 2500)

# accessing public methods
# adding money in account1
account1.deposit(500)
print(f"Account1 balance after deposit: {account1.get_balance()}")
# withdrawing money from account1
account1.withdraw(1500)
print("Account1 balance after withdrawal: ", account1.get_balance())

# error demonstration
account2.withdraw(2600)
print("Account2 balance after failed withdrawal: ", account2.get_balance())

# trying to access private attribute will raise an error
print(account1.__balance)  # Uncommenting this line will raise an AttributeError

# Abstraction in Python
# abstract is a process of hiding the implementation details and showing only functionality to the user.
# we can achieve abstraction using abstract classes and methods

# here we are creating an abstract class Shape with an abstract method area
from abc import ABC, \
    abstractmethod  # here abc is abstract base class, ABC is a module, abstractmethod is a decorator, we use it to define abstract methods, which are methods that have a declaration but do not have an implementation, we cannot create objects of abstract classes, we need to create a derived class that implements the abstract methods, then we can create objects of the derived class, and use the methods defined in the abstract class, we use abstraction to hide the complexity of the system and show only the essential features to the user


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
