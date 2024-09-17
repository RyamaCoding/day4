import random

names_string = input("Give me everybody's names seperated by a comma. ")
names = names_string.split(", ")

random_name = random.randint(0, len(names) - 1)

# Alternatively
# person_who_will_pay = random.choice(names)

bill = print(f"{names[random_name]} is going to buy the meal today")
