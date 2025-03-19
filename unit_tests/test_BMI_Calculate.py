import pytest
from ..backend.BMI import BMI

B = BMI(weight=176, height=71)

# used parametrize to test multiple values for the BMI
# the values are their exact fraction inputs, 
# due to the math not being rounded until output
@pytest.mark.parametrize("weight, height, expected", 
                         [(89.91, 1.725, 30.2),
                          (79.2, 1.775, 25.1),
                          (76.86, 1.6, 30.0),
                          ("hello", 10, "ERROR: Wrong data type entered!"),
                          ([1, 0], 1, "ERROR: Wrong data type entered!"),
                          (170, 0, "ERROR: Can't divide by zero!"),
                          (-1, 50, "Can't weigh less that 0 lbs"),
                          (10, -1, "Can't be shorter than 0 m")])

def test_conversion1(weight, height, expected):
    assert B.calculate_BMI(weight, height) == expected
    