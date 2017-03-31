#!/usr/bin/python3

class Animal:
    def talk(self): print('I have something to say')
    def walk(self): print('I am walking here !')
    def clothes(self): print('I have nice clothes')

class Duck(Animal):
    def __init__(self, **kwargs):
        self._variabes = kwargs

    def quack(self):
        print('Quaaaack!')
        
    def walk(self):
        print('Walks like a Duck')
        
    def set_variable(self, key, value):
        self._variabes[key] = value
    
    def get_variable(self, key):
        return self._variabes.get(key, None)
        
class Dog(Animal):
    def bark(self):
        print('Woof')

    def fur(self):
        print('The dog has brown and white fur')

def main():
    donald = Duck(feet = 2)
    print(donald.get_variable('color'))
    donald1 = Duck(color = 'Red', feet = 2)
    print(donald1.get_variable('color'))
    print(donald1.get_variable('feet'))
    donald1.clothes()
    
    tommy = Dog()
    tommy.clothes()
    
if __name__ == '__main__' : main()