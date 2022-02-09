
def three_is_a_crowd_part_1(people):
    amt_of_people = len(people)
    if amt_of_people > 3:
        print("the room is crowded")

def three_is_a_crowd_part_2(people):
    amt_of_people = len(people)
    if amt_of_people > 3:
        print("the room is crowded")
    else:
        print("The room is not very crowded")


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

    #Three is a Crowd
    #Make a list of names that includes at least four people.
    people = ["john","mary","bob","ashley"]
    #Write an if test that prints a message about the room being crowded, if there are more than three people in your list.
    three_is_a_crowd_part_1(people)
    people.remove("john")
    people.remove("mary")
    three_is_a_crowd_part_1(people)

    #Three is a Crowd - Part 2
    #Add an else statement to your if tests. If the else statement is run, have it print a message that the room is not very crowded.
    three_is_a_crowd_part_2(people)


    #Six is a Mob
    people = ["john","mary","bob","ashley", "marcus", "jessica"]
    crowd_test(people)
    people.remove("john")
    people.remove("mary")
    crowd_test(people)

    
