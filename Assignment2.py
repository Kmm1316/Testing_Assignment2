
weight: int = int(input("What is your current weight (lbs)?:\n"))
height: int = int(input("What is your current height (inches)?:\n"))

weight_in_kg: int = weight * 0.45
height_in_m: int = height * 0.025

BMI: int = weight_in_kg/(height_in_m ** 2)

print()
print(f"Your weight in kilos is: {weight_in_kg:.1f} \nYour height in meters is: {height_in_m:.1f}\n")

print(f"Your BMI is approximately: {BMI:.1f}")

if BMI < 18.5:
    print("Your BMI is less than 18.5, !!Under Weight!!\n")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Your BMI is within normal range, Normal Weight\n")
elif BMI >= 25 and BMI <= 29.9:
    print("Your BMI is greater than 25, !!Over Weight!!\n")
else:
    print("Your BMI is way out of scope, !!Obese!!\n")