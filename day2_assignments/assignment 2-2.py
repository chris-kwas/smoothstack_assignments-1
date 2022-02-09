if __name__ == '__main__':
    #start of coding exersice 4:
    lst = [1,"hello", 4.5]
    print(lst)
    lst = [1,1,[1,2]] #ask about this question in class
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
    #rest of questions on problem sheet had answers provided unsure if I need to put answers here