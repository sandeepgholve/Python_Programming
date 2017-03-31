#!/usr/bin/python3

class AnimalAction():
    def quack(self): return self._doAction('quack')
    def feathers(self): return self._doAction('feathers')
    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')
    
    def _doAction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}'.format(self.animalName(), action)
    
    def animalName(self):
        return self.__class__.__name__.lower()
    
class Duck(AnimalAction):
    strings = dict(
            quack = 'Quaaaaack.',
            feathers = 'The duck has gray and white feathers.'         
        )
    
class Person(AnimalAction):
    strings = dict(
            quack = 'The Person imitates the duck.',
            feathers = 'The Person takes a feather from ground and show it.',
            bark = 'The Person says woof!',
            fur = 'The Person put on a fur coat.'            
        )
    
class Dog(AnimalAction):
    strings = dict(
            bark = 'Arf!',
            fur = 'The dog has white fur with black spots.'            
        )

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())
    
def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())
    
def main():
    donald = Duck()
    john = Person()
    fido = Dog()
    
    print('- In the forest:')
    for o in (donald, john, fido):
        in_the_forest(o)

    print('- In the doghouse:')
    for o in (donald, john, fido):
        in_the_doghouse(o)
        
if __name__ == "__main__": main()

    