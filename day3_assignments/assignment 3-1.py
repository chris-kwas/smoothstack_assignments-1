import random

def celsius_to_fahrenheit(temp):
    return int(temp * (9 / 5) + 32)

def fahrenheit_to_celsius(temp):
    return int((temp - 32) * (5/9))

if __name__ == '__main__':
    #start of coding exersice 7:
    
    # Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
    for x in range(1500,2700+1,5):
        if x % 7 == 0 and x % 5 == 0:
            print('{}{}'.format(x,","), end = "")
    print()

    # Write a Python program to convert temperatures to and from celsius, fahrenheit
    print(celsius_to_fahrenheit(60))
    print(fahrenheit_to_celsius(45))

    # Write a Python program to guess a number between 1 to 9
    x = random.randint(1,9)
    print("guess number from 1-9")
    guess = int(input())
    while guess != x:
        print("wrong guess try another number")
        guess = int(input())
    print("You guess the correct number")


    #Write a Python program to construct the following pattern, using a nested for loop.
    step = 1
    x = 1
    while x >= 1:
        for y in range(x):
            print("*", end = "")
        print()
        x += step
        if x == 5:
            step = -1
            
    #Write a Python program that accepts a word from the user and reverse it
    reversed_word = input("Input word ")[::-1]
    print(reversed_word)

    #Write a Python program to count the number of even and odd numbers from a series of numbers
    numbers = (1,2,3,4,5,6,7,8,9)
    even_amt = 0
    odd_amt = 0

    for num in numbers:
        if num % 2 == 0:
            even_amt += 1
        else:
            odd_amt += 1


    #Write a Python program that prints each item and its corresponding type from the following list.
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    for data in datalist:
        print(data, type(data))

    #Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement. 
    for num in range(6 + 1):
        if num == 3 or num == 6:
            continue
        else:
            print(num, end =" ")
