# Matthew Lane (ml2162) - CSE 4283-01: Assignment 2

# This function will prompt the user for a measurement,
# and only accept a number above the floor value.
def obtain_measurement(name, floor):
    while True:
        try:
            unit = input(f"{name}: ")
            unit = int(unit)
            if unit < floor:
               raise
            break
        except:
            print(f"Please enter a valid number above {floor}.")
    return unit

# This function will prompt the user for their height
# in feet and inches, and weight in pounds.
def obtain_measurements():
    # Get height
    print("Please enter your height using feet and inches.")
    feet   = obtain_measurement("Feet",   1)
    inch   = obtain_measurement("Inches", 0)

    # Combine feet and inches
    inches = (feet * 12) + inch

    # Get weight
    print("Please enter your weight in pounds.")
    pounds = obtain_measurement("Pounds", 1)

    return inches, pounds

# This function will convert a height in inches and
# weight in pounds into a BMI and BMI category.
def calculate_bmi(inches, pounds):
    # Convert weight in pounds to kilograms
    kilograms = pounds * 0.45

    # Convert inches to meters
    meters = inches * 0.025

    # Perform BMI calculation to one decimal place
    bmi = round(kilograms / (meters**2), 1)

    # Determine category
    category = ""
    if bmi < 18.5:
        category = "Underweight"
    if (bmi >= 18.5) and (bmi < 25):
        category = "Normal weight"
    if (bmi >= 25) and (bmi < 30):
        category = "Overweight"
    if bmi >= 30:
        category = "Obese"

    return bmi, category

# Only continue if using interactive shell
if __name__ == "__main__":
    # Prompt user to input measurements
    inches, pounds = obtain_measurements()

    # Perform the calculation
    bmi, bmi_category = calculate_bmi(inches, pounds)

    # Display results to user
    print(f"\nYour BMI is {bmi}\nYour category is {bmi_category}")
