height = float(input("What's your height? (m)"))
weight = float(input("What's your weight? (Kg)"))
print("Height:", height)
print("weight:", weight)
bmi = round(weight / height ** 2, 2)
print ("Your BMI is: ", bmi)

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You've normal weight")
elif 25 <= bmi <29.9:
    print("You are overweight")
else:
    print("You are obese")

