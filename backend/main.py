from BMI import BMI

print("Welcome to my BMI calculator application!")

menu: str = '''
Please choose an option with which you would like to proceed.
1. Normal execution (asks for input and sends output)
2. Test functions
3. Test category Outputs
0. Exit
            '''

choice: int
func_choice: int

while 1:
    print(menu)
    choice = int(input())

    if choice != 0 and choice != 3:
        print("Next: please enter your weight and height for the next steps\n")
        weight: float = float(input("What is your weight in lbs?: "))
        height: float = float(input("what is your height in inches?: "))
        B = BMI(weight, height)

    if choice == 1:
        print()
        print(f"Your BMI is {B.calculate_BMI(B.weight_in_kg, B.height_in_m)}, You are considered {B.categorize_BMI()}")

    elif choice == 2:
        print("Which function would you like to test output?: \n"
        "1. calculate_BMI() - will convert your weight and height into your BMI approximate\n"
        "2. categorize_BMI() - will categorize you based on your BMI approximate")
        func_choice = int(input())

        if func_choice == 1:
            B = BMI(weight, height)
            print(f"Your BMI approximate is {B.calculate_BMI(B.weight_in_kg, B.height_in_m)}")
        
        elif func_choice == 2:
            B.calculate_BMI(B.weight_in_kg, B.height_in_m)
            B.categorize_BMI()

    elif choice == 3:
        B = BMI(1, 1)
        nums: list = [18.4, 18.6, 28, 35]
        for i in nums:
            B._BMI = i
            B.categorize_BMI()
    else:
        break

print("Program has exited, Thanks!")