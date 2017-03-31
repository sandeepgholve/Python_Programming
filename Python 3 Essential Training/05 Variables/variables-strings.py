#!/usr/bin/python3

def main():
    normalString = "Sandeep\t Gholve. \nThis is second line"
    print(normalString)
    rawString = r"This is \t raw \n String. Does not evaluate tabs and new line character"
    print(rawString)
    
    print("My Age is {}.".format(33))
    
    
    paragraph = '''        This way I can have line after line
        spanned across multiple lines.
        
        bla
        bla
        bla
        Dhinchak
    '''
    print(paragraph)

if __name__ == "__main__" : main()