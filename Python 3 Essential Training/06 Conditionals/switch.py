#!/usr/bin/python3

def main():
    choices = dict(
            one = "first",
            two = "second",
            three = "third",
            four = "fourth",
            five = "fifth"
        )
    
    v = "one"
    
    print(choices[v])
    
    v = "seven"
    print(choices.get(v, "use default as 'other'"))
    
if __name__ == "__main__" : main()