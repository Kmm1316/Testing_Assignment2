class BMI():

    def __init__(self, weight: float, height: float) -> None:
        self.weight: float = weight
        self.height: float = height
        self.weight_in_kg: float = self.weight * 0.45
        self.height_in_m: float = self.height * 0.025
        self._BMI: float

    def calculate_BMI(self, kg: float, m: float) -> None:
        try:
            if(kg) < 0:
                return "Can't weigh less that 0 lbs"
            elif(m) < 0:
                return "Can't be shorter than 0 m"
            
            self.__BMI: float = kg/(m**2)
            return round(self.__BMI, 1)
        except TypeError:
            return "ERROR: Wrong data type entered!"
        except ZeroDivisionError:
            return "ERROR: Can't divide by zero!"
        
    def categorize_BMI(self) -> str:
        bmi: float = self._BMI
        if bmi < 18.5:
            print("Under Weight\n")
            return "Under Weight"
        elif bmi >= 18.5 and bmi <= 24.9:
            print("Normal Weight\n")
            return "Normal Weight"
        elif bmi >= 25 and bmi <= 29.9:
            print("Over Weight\n")
            return "Over Weight"
        else:
            print("Obese\n")
            return "Obese"
        
    