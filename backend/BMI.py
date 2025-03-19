class BMI():

    def __init__(self, weight: float, height: float) -> None:
        self.weight: float = weight
        self.height: float = height
        self.weight_in_kg: float = self.weight * 0.45
        self.height_in_m: float = self.height * 0.025
        self.BMI: float


    def calculate_BMI(self, kg: float, m: float) -> None:
        try:
            if(kg) < 0:
                return "Can't weigh less that 0 lbs"
            elif(m) < 0:
                return "Can't be shorter than 0 m"
            
            self.BMI: float = kg/(m**2)
            return round(self.BMI, 1)
        except TypeError:
            return "ERROR: Wrong data type entered!"
        except ZeroDivisionError:
            return "ERROR: Can't divide by zero!"
        
    def categorize_BMI(self) -> None:
        if self.BMI < 18.5:
            print("Under Weight\n")
        elif self.BMI >= 18.5 and self.BMI <= 24.9:
            print("Normal Weight\n")
        elif self.BMI >= 25 and self.BMI <= 29.9:
            print("Over Weight\n")
        else:
            print("Obese!!\n")
    