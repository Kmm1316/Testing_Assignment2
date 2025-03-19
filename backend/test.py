from BMI import BMI

weight: int = int(input("What is your current weight (lbs)?:\n"))
height: int = int(input("What is your current height (inches)?:\n"))

B = BMI(weight=weight, height=height)

print()
B.input_conversion()
B.categorize_BMI()