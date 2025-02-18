# Python Weight Converter with Error Handling

try:
    weight = float(input("Enter your weight: "))
    unit = input("Kilograms or Pounds? (K or L): ").strip().upper()  # Handle spaces & case

    if unit == "K":
        weight = weight * 2.205
        unit = "Lbs."
        print(f"Your weight: {round(weight, 1)} {unit}")
    elif unit == "L":
        weight = weight / 2.205
        unit = "Kgs."
        print(f"Your weight: {round(weight, 1)} {unit}")
    else:
        print(f"'{unit}' is not a valid unit. Please enter 'K' or 'L'.")

except ValueError:
    print("Invalid input. Please enter a numeric value for weight.")
