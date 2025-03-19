import pytest
from ..backend.BMI import BMI

def test_calculateBMI():
    B = BMI(176, 71)
    B.calculate_BMI(B.weight_in_kg, B.height_in_m)
    print(B.categorize_BMI())
    assert B.categorize_BMI() == "Over Weight"

def test_calculateBMI_1():
    B = BMI(245, 74)
    B.calculate_BMI(B.weight_in_kg, B.height_in_m)
    assert B.categorize_BMI() == "Obese"

def test_calculateBMI_2():
    B = BMI(130, 71)
    B.calculate_BMI(B.weight_in_kg, B.height_in_m)
    assert B.categorize_BMI() == "Normal Weight"

def test_calculateBMI_3():
    B = BMI(100, 71)
    B.calculate_BMI(B.weight_in_kg, B.height_in_m)
    assert B.categorize_BMI() == "Under Weight"

