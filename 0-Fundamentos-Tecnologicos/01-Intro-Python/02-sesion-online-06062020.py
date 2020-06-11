"""
06/06/2020
Several easy exercises to start coding in Python
"""

# 1. Mean of two numbers

import statistics

x = float(input('Introduce the first number: '))
y = float(input('Introduce the second number: '))
total = x + y

mean_1 = (total)/2

print("The mean is {}".format(mean_1))

# 2. Calculate the body mass index

weight = float(input("Introduce your weight (kg): "))
height = float(input("Introduce yout height (m): "))

body_mass = round(weight/(height**2),2)

print("The body mass index is {}".format(body_mass))

# 3. Convert from inch to cm

inch = float(input("Introduce the distance in inchs: "))
cm = inch*2.54

print("{} inchs is equal to {} cm".format(inch,cm))

# 4. Convert the temperature from Celsius to Fahrenheit

celsius = float(input("Introduce the temperature in Celsius: "))
fahrenheit = 1.8*celsius + 32

print("{} celsius are equal to {} fahrenheit".format(celsius,fahrenheit))

# 5. Arithmetic Progression

terms = int(input("How long is the arithmetic progression? "))
first_term = float(input("Which is the first term? "))
difference = float(input("Which is the difference between the terms? "))

arith_pro = (terms/2)*(2*first_term + (terms-1)*difference)

print("The sum of the {} first numbers of an arithmetic progression, which first term is {} and the difference between the terms is {} is {}".format(terms,first_term,difference,arith_pro))

