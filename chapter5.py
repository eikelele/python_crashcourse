"""Python Crash Course Chapter 5: IF STATEMENTS"""
#5-1 Conditional tests:
print('----------------------------------------')
print("Is pizza one of my favourite food? I predict True")
fav_foods = ['burger', 'pizza', 'pasta']
print('pizza' in fav_foods)
print("Is Java my favourite programming language? I predict False")
fav_prog_language = 'python'
print(fav_prog_language == 'java')
print('----------------------------------------')
#5-2 More Conditional Tests:
print("Is Subaru my favourite car brand?")
fav_car_brand = "bmw"
print(f"Equality: {fav_car_brand == 'subaru'}")
if fav_car_brand != "subaru":
    print(f"My favourite car brand is {fav_car_brand} so the inequality is True!")

users = ['eike', 'danny', 'annika']
user_input = input("Insert username please: ").lower()
if user_input in users:
    print("Username is already used!")
else:
    print("Valid username.")

numbers = [number for number in range (1,50)]
for number in numbers:
    if number != 42:
        print("Not 42!")
    else:
        print("It's 42!!!")
for number in numbers:
    if number >= 21 and number <= 50:
        print("You can attend!")
    else:
        print("You can NOT attend!")
print('----------------------------------------')
#Multiple conditions example page 83
requested_toppings = ['mushrooms', 'extra cheese', 'zucchini']
toppings = ['mushrooms', 'extra cheese', 'extra salami', 'paprika']
ordered_toppings = []

for topping in requested_toppings:
    if topping in toppings:
        ordered_toppings.append(topping)
        print(topping)
print('----------------------------------------')
if 'mushrooms' in requested_toppings:
    print("Adding mushrroms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished your pizza.")
print('----------------------------------------')
#5-3 Alien Colors #1:
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
print('----------------------------------------')
#5-4 ALien Colors #2:
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")
print('----------------------------------------')
#5-5 Alien Colors #3:
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
elif alien_color == 'red':
    print("You earned 15 points!")
print('----------------------------------------')
#5-6 Stages of Life:
age = 27
if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager!")
elif age >= 20 and age < 65:
    print("You are an adult!")
elif age >= 65:
    print("You are an elder!")
print('----------------------------------------')
#5-7 Favourite Fruit:
favorite_fruits = ['banana', 'strawberry', 'peach']
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")
if 'cherry' in favorite_fruits:
    print("You really like cherries!")
if 'peach' in favorite_fruits:
    print("You really like peaches!")
print('----------------------------------------')
#5-8 Hello Admin:
usernames = ['eike.saathoff', 'danny.roelling', 'christian.luensmann', 'alfred.saathoff', 'admin']
for user in usernames:
    if user == 'admin':
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
#5-9 No Users:
print('----------------------------------------')
usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
#5-10 Checking Usernames:
print('----------------------------------------')
current_users = ['eike', 'eikelele', 'Yevelin', 'Methok', 'Kidneyinc', 'Grindol']
new_users = ['eIke', 'eikeLeLe', 'Ningirsu', 'Abbuva', 'Hitchi']
if new_users:
    for user in new_users:
        if user.lower() in current_users:
            print(f"Username '{user}' already in use! Pick another one!")
        else:
            current_users.append(user)
else:
    print("Empty list!")
for user in current_users:
    print(user)
#5-11 Ordinal Numbers:
print('----------------------------------------')
numbers = [number for number in range(1,10)]
if numbers:
    for number in numbers:
        if number == 1:
            print(f"{number}st")
        elif number == 2:
            print(f"{number}nd")
        elif number == 3:
            print(f"{number}rd")
        else:
            print(f"{number}th")
else:
    print("Empty list!")
