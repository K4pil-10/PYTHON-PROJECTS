height = float(input("enter your height in meter: "))
weight = float(input('Enter your weight in kg: '))
bmi= weight / (height ** 2)
# print(round(bmi,2))
if bmi >=25:
    print("Over-weight")
elif bmi >=18:
    print("Normal-Weight")
else :
    print("Under-weight")