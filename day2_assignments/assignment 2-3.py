def crowd_test(people):
    population = len(people)
    if population > 5:
        print("there is a mob in the room")
    elif population >= 3 and population <= 5:
        print("the room is to crowded")
    elif population == 1 or population == 2:
        print("the room  is not being crowded")
    else:
        print("the room is empty")

if __name__ == '__main__':
    #start of coding exersice 6:
    people = ["john","mary","bob","ashley", "marcus", "jessica"]
    crowd_test(people)
    people.remove("john")
    people.remove("mary")
    crowd_test(people)

    
