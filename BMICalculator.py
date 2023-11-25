def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Please enter valid values.")
    else:
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        print(f"Your BMI is {bmi:.2f} and you are {category}.")

if __name__ == "__main__":
    main()
