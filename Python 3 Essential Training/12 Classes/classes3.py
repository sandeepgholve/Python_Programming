#!/usr/bin/python3

class Duck:
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
        
def main():
    donald = Duck(feet = 2)
    print(donald.get_variable('color'))
    donald1 = Duck(color = 'Red', feet = 2)
    print(donald1.get_variable('color'))
    print(donald1.get_variable('feet'))
    
if __name__ == '__main__' : main()