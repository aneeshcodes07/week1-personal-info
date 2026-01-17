# Personal Information Manager
# Author: Aneesh VS
# Week 1 Internship Project – Python Basics

print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# ----- Static Information -----
name = "Aneesh VS"
age = 20    # change to your age
city = "Madikeri"
hobby = "Coding"

# ----- User Input -----
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What's your favorite food? ").strip()
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ").strip()

favorite_color = input("What's your favorite color? ").strip()
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ").strip()

# ----- Calculations -----
age_in_months = age * 12

# ----- Display Output -----
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)
