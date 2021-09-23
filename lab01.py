# Write a program that asks the user for a number of milliliters (mL) and outputs the equivalent number of teaspoons and tablespoons.
# **Note:** Assume there are (rounding up) 5mL in a teaspoon and 3 teaspoons in a tablespoon.
#

volume_mL = input("Please enter a value in mL to convert")
teaspoon = int(volume_mL)/5
tablespoon = int(teaspoon)//3
teaspoon = teaspoon-(tablespoon*3)
print(volume_mL, "mL converts to", round(teaspoon), "teaspoon(s) and", round(tablespoon), "tablespoon(s)")


