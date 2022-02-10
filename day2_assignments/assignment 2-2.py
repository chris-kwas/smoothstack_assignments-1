def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

def integral_number(n):
    return {x : x*x for x in range(1,n + 1)}

def generate_number_list_and_tuple(sequence : str):
    answer= sequence.split(",")
    print(answer)
    print(tuple(answer))
    

class InputOutString(object):
    def __init__(self):
        self.string = ""       
    def getString(self):
        self.string = input("Enter string: ")
    def printString(self, string):
        print(self.string)
    def test_function(self):
        self.printString(self.getString())





if __name__ == '__main__':
    #start of coding exersice 4:
    lst = [1,"hello", 4.5]
    print(lst)
    lst = [1,1,[1,2]]
    print(lst[2][1])
    #lst=['a','b','c'] What is the result of lst[1:]?  = ['b','c']
    lst = ['a','b','c'] 
    print(lst[1:])
    weekdays = {
        "MONDAY" : 0,
        "TUESDAY": 1,
        "WEDNESDAY" : 2,
        "THURSDAY" : 3,
        "FRIDAY" : 4
    }
    #D={‘k1’:[1,2,3]} what is the output of D[k1][1] = 2
    lst = [1,[2,3]]
    lst = tuple(lst)
    word = set("Mississippi")
    word.add('X')
    print(word)
    #Output of set([1,1,2,3]) = {1,2,3}
    for x in range(2000,3000+1,1):
        if x % 7 == 0 and x % 5 != 0:
            print('{}{}'.format(x,","), end = "")
    print()
    #Question 2
	#Level 1
    #Write a program which can compute the factorial of a given numbers.
    print(factorial(int(input("Enter number for factorial here: "))))
    # Question 3
	# Level 1
    #With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). 
    print(integral_number(int(input("Enter number: "))))
    # Question 4
	# Level 1
    # Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
    #data = "34,67,55,33,12,98"
    data = input("Enter sequence of number seperated by only a comma: ")
    generate_number_list_and_tuple(data)
    # Question 5
	# Level 1
    # Define a class which has at least two methods:
	# getString: to get a string from console input
	# printString: to print the string in upper case.
	# Also please include simple test function to test the class methods.
    Iostring = InputOutString() 
    Iostring.test_function()