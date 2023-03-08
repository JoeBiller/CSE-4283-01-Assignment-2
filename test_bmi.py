# Matthew Lane (ml2162) - CSE 4283-01: Assignment 2

# Import all the functions from the main file
from bmi import *

# Here will perform a basic test on the obtain_measurement function
def test_obtain_measurement(monkeypatch):
    # We will substitute the input function to return 1
    # This will simulate the user inputting 1
    monkeypatch.setattr('builtins.input', lambda _: 1)

    # By inputting 1, the function should return 1
    assert obtain_measurement("Test", 0) == 1

# Here will perform a basic test on the obtain_measurements function
def test_obtain_measurements(monkeypatch):
    # We will substitute the input function to return 5
    # This will simulate the user inputting 5
    monkeypatch.setattr('builtins.input', lambda _: 5)

    # By only inputting 5, the function should return a height
    # in inches of 65 and a weight in pounds of 5
    assert obtain_measurements() == (65, 5)

# Here we will test if calculate_bmi can correctly
# calculate a BMI that is Underweight
def test_calculate_bmi_underweight():
    # For the given range (-infinity, 18.5), we calculate the
    # following Weak N x 1 points...
    # OFF = 18.4
    assert calculate_bmi(63, 101.43) == (18.4, "Underweight")
    # ON = 18.5
    assert calculate_bmi(63, 101.98) == (18.5, "Normal weight")

# Here we will test if calculate_bmi can correctly
# calculate a BMI that is Normal weight
def test_calculate_bmi_normal_weight():
    # For the given range [18.5, 25), we calculate the
    # following Weak N x 1 points...
    # OFF = 18.4
    assert calculate_bmi(63, 101.43) == (18.4, "Underweight")
    # ON = 18.5
    assert calculate_bmi(63, 101.98) == (18.5, "Normal weight")
    # INT = 21.8
    assert calculate_bmi(63, 120.17) == (21.8, "Normal weight")
    # OFF = 24.9
    assert calculate_bmi(63, 137.26) == (24.9, "Normal weight")
    # ON = 25
    assert calculate_bmi(63, 137.81) == (25, "Overweight")

# Here we will test if calculate_bmi can correctly
# calculate a BMI that is Overweight
def test_calculate_bmi_overweight():
    # For the given range [25, 30), we calculate the
    # following Weak N x 1 points...
    # OFF = 24.9
    assert calculate_bmi(63, 137.26) == (24.9, "Normal weight")
    # ON = 25
    assert calculate_bmi(63, 137.81) == (25, "Overweight")
    # INT = 27.5
    assert calculate_bmi(63, 151.59) == (27.5, "Overweight")
    # OFF = 29.9
    assert calculate_bmi(63, 164.82) == (29.9, "Overweight")
    # ON = 30
    assert calculate_bmi(63, 165.38) == (30, "Obese")

# Here we will test if calculate_bmi can correctly
# calculate a BMI that is Obese
def test_calculate_bmi_obses():
    # For the given range [30, infinity), we calculate the
    # following Weak N x 1 points...
    # OFF = 29.9
    assert calculate_bmi(63, 164.82) == (29.9, "Overweight")
    # ON = 30
    assert calculate_bmi(63, 165.38) == (30, "Obese")
