import pytest
from ..backend.BMI import BMI

B = BMI(176, 71)

def test_calculateBMI():
    B.calculate_BMI(B.weight_in_kg, B.height_in_m)
    assert B.categorize_BMI() == "Over Weight"