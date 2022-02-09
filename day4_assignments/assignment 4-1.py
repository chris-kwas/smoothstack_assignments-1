
def func():
    print('Hello World')

def func1(name):
    print("Hi My name is {}".format(name))

def func3(x,y,z):
    if z:
        return x
    else:
        return y

def func4(x,y):
    return x * y

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_greaterthan(x, y):
    if x > y:
        return True
    else:
        return False

def addition(*nums):
    return sum(nums)

def evens(*nums):
    evens_numbers = list()
    for num in nums:
        if num % 2 == 0:
            evens_numbers.append(num)
    return evens_numbers

def string_modifier(text):
    new_string = ""
    for x in range(len(text)):
        if x % 2 == 0:
            new_string += text[x].upper()
        else:
            new_string += text[x].lower()
    return new_string

def func10(x, y):
    if x % 2 == 1 or y % 2 == 1:
        return x if x > y else y
    else:
        return x if x < y else y

def func11(string1, string2):
    if string1[0] == string2[0]:
        return True

def func12(num):
    return 7 + ((7 - num) * 2)

def func13(text):
    text_length = len(text)
    new_text = ""
    for x in range(text_length):
        if x == 0 or x == 3:
            new_text += text[x].upper()
        else:
            new_text += text[x]
    return new_text

if __name__ == '__main__':
    #start of coding exersice 8:
    #1.Create a function func() which prints a text ‘Hello World’
    func()
    #2.Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’
    func1("Google")
    #3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)
    func3("hello","goodbye", False)
    #4.define a function func4(x,y) which returns the product of both the values.
    func4(1, 2)
    #5.define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not.
    is_even(56)
    #6.define a function that takes two arguments ,and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.
    is_greaterthan(10, 7)
    #7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.
    print(addition(1,2,3,4))
    #8.Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.
    print(evens(1,2,3,4))
    #9.Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase 
    print(string_modifier("helLo"))
    #10.Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd.
    print(func10(6, 10))
    #11.Write a function which takes  two-strings and returns true if both the strings start with the same letter.
    print(func11("Hello", "House"))
    #12.Given a value,return a value which is twice as far as other side of 7
    print(func12(11))
    #13.A function that capitalizes first and fourth character of a word in a string.
    print(func13("hello"))