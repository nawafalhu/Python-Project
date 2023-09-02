# User height and weight
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Calculation the BMI 
BMI = round(weight / (height ** 2), 2)

# BMI classification
if BMI < 18.5 : 
    print('underweight')
    print('Your BMI is', int(BMI))
elif BMI >= 18.5 and BMI < 25 :
    print('normal weight')
    print('Your BMI is', int(BMI))
elif BMI >= 25 and BMI < 30 :
    print("slightly overweight")
    print('Your BMI is', int(BMI))
elif BMI >= 30 and BMI < 35 : 
    print('obese')
    print('Your BMI is', int(BMI))
else :
    print('clinically obese.')
    print('Your BMI is', int(BMI))
    