def price_change(accounting_routine):
    return list(map(lambda account: account[2] * account[3] < 100 and (account[0], ((account[2] * account[3]) + 10)) or (account[0], account[2] * account[3]) , accounting_routine))
    

def func2(second_accounting_routine):
    return list(map(lambda entry: (entry[0], entry[1][1] * entry[1][2]), second_accounting_routine))


if __name__ == '__main__':
    #start of coding exersice 9:
    #Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is smaller than 100,00 €. 
    #Write a Python program using lambda and map    
    accounting_routine = list()#[int,string,int,float]
    accounting_routine.append([34587, "Learning Python, Mark Lutz", 4, 40.95])
    accounting_routine.append([98762, "Programming Python, Mark Lutz", 5, 56.80])
    accounting_routine.append([77226, "Head First Python, Paul Barry", 3, 32.95])
    accounting_routine.append([88112, "Einführung in Python3, Bernd Klein", 3, 24.99])
    print(price_change(accounting_routine))

    #Write a program which returns a list of two tuples with (order number, total amount of order).
    #[ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 
    second_accounting_routine = list()#[int,string,int,float]
    second_accounting_routine.append([34587, ("Learning Python, Mark Lutz", 4, 40.95)])
    second_accounting_routine.append([98762, ("Programming Python, Mark Lutz", 5, 56.80)])
    second_accounting_routine.append([77226, ("Head First Python, Paul Barry", 3, 32.95)])
    second_accounting_routine.append([88112, ("Einführung in Python3, Bernd Klein", 3, 24.99)])
    print(func2(second_accounting_routine))
    