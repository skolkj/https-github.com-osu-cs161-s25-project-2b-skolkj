# Author: Kara Sokol
# GitHub username: skolkj
# Date: 4/18/2025
# Description: Asks the user how many integers they would like to enter, prompt them to enter, then determine and print the min and max values.
nbr_int = int(input("How many integers would you like to enter?"))
min=0
max=0
print ("Please enter ",nbr_int,"integers.")
for i in range (1, nbr_int+1):
    number = int(input())
    if number < min:
        min=number
    if number > max:
        max=number
print("min: ", min)
print("max: ", max)

