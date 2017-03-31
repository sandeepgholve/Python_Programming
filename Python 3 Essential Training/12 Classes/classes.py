#!/usr/bin/python3

class Duck:
    def __init__(self):
        print('Constructor')

    def quack(self):
        print('Quaaaack!')
        
    def walk(self):
        print('Walks like a Duck')
        
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    
if __name__ == '__main__' : main()