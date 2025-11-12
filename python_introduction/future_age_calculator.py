# future_age_calculator.py

# Ask the user for their current age
age_input = input("How old are you? ")

# Convert the input from string to integer
current_age = int(age_input)

# Calculate the age in 2050
years_until_2050 = 2050 - 2023  # 27 years
age_in_2050 = current_age + years_until_2050

# Print the result
print(f"In 2050, you will be {age_in_2050} years old.")
