def BMI_classification(weight, height):
    bmi = weight / pow(height,2)
    if bmi < 18.5:
        return "under"
    elif bmi < 25.0:
        return "normal"
    elif bmi < 30.0:
        return "over"
    else:
        return "obese"


#Day 5 –Weekend exercise work – please use functions for this problem
input_amt = int(input("How many entries "))

bmis = list()
for x in range(input_amt):
    weight = int(input("Enter weight "))
    height = float(input("Enter height "))
    bmis.append(BMI_classification(weight, height))

for bmi in bmis:
    print(bmi, end = " ")
