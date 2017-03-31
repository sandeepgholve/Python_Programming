#!/usr/bin/python3

class Duck:
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'White')

    def quack(self):
        print('Quaaaack!')
        
    def walk(self):
        print('Walks like a Duck')
        
    def set_color(self, color):
        self._color = color
    
    def get_color(self):
        return self._color
        
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    
    print(donald.get_color())
    donald.set_color('Blue')
    print(donald.get_color())
    
if __name__ == '__main__' : main()