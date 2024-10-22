# age = 20
# name = input("Vad geter dy")
#
# if age > 18:
#     print(name + " är vuxen")
#
# for x in range(0, 10, 2):
#     print(x)
#
# number1 = "13.5"
# number2 = 17
# print(number1 + number2)
#
# child_ages = [3, 4, 8, 11]
# child_ages[4] = 14

# Uppgift 5
print("Nu är jag riktigt taggad på att få skriva lite kod")

# Uppgift 6
birth_year=2004
age=20
print(birth_year+age)

# Uppgift 7
first_name = input("Vad heter du i förnamn? ")
last_name = input("Vad heter du i efternamn? ")
print("Du heter " + first_name + " " + last_name)

# Uppgift 8
user_height_input = input("Hur lång är du? ")
user_height = int(user_height_input)

if user_height < 100:
    print("Du är " + str(user_height) + " cm lång")
else:
    print("Om man kapar av dina ben blir du " + str(user_height/2) + " cm lång")

# Uppgift 9
for i in range(1, 31):
    print(i)

# Uppgift 10
passwords = ["password", "monkey", "qwerty", "letmein", "admin", "starwars"]

for i in range(len(passwords)):
    passwords[i] = passwords[i] + "123"

for i in range(len(passwords)):
    print(passwords[i])

# Uppgift 11
def print_message(message):
    print(message)

print_message("Snart klar!")

# Uppgift 12
def multiply(a, b):
    return a * b

print(multiply(70, 6))

# Uppgift 14
def get_water_state(water_temp):
    if water_temp < 0:
        return "solid"
    elif water_temp >= 100:
        return "gas"
    else:
        return "liquid"