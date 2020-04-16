"""Python Crash Course Chapter 4: Working with lists"""
#4-1 Pizzas
print('----------------------------------------')
fav_pizzas = ['salami', '4 kaese', 'peperoni salami']
for pizza in fav_pizzas:
    print(f"I like {pizza.title()} pizza!")
print("I really love pizza! ")
#4-2 Animals
print('----------------------------------------')
animals = ['dog', 'fish', 'deer']
for animal in animals:
    print(f"A {animal.title()} is a really great pet!")
print("Animals are great!")
#4-3 Counting to twenty
print('----------------------------------------')
for value in range(1,21):
    print(value)
#4-4 One Million
#print('----------------------------------------')
#for value in range(1,1_000_001):
#    print(value)
#4-5 Summing a Million
print('----------------------------------------')
million_list = [value for value in range(1,1_000_001)]
print(sum(million_list))
#4-6 Odd numbers:
print('----------------------------------------')
for value in range(1,21,2):
    print(value)
#4-7 Threes:
print('----------------------------------------')
for value in range(1,31):
    if value % 3 == 0:
        print(value)
#4-8 Cubes:
print('----------------------------------------')
cubes = []
for value in range(1,11):
    print(value**3)
#4-9 Cube comprehension:
print('----------------------------------------')
cubes = [value**3 for value in range(1,11)]
print(cubes)
#4-10 Slices
print('----------------------------------------')
print(f"The first three items in the list are: {million_list[:3]}")
print(f"Three items of the middle of the list: {million_list[int((len(million_list)/2)):int(((len(million_list)/2)+3))]}")
print(f"Last the items of the list: {million_list[-3:]}")
#4-11 My Pizzas, Your Pizzas
print('----------------------------------------')
friend_pizzas = fav_pizzas[:]
friend_pizzas.append("thunfisch")
print(f"My favourite pizzas are: {[pizza.title() for pizza in fav_pizzas]}")
print(f"My friends favourite pizzas are: {[pizza.title() for pizza in friend_pizzas]}")
#4-12 More Loops:
print('----------------------------------------')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print([food.title() for food in my_foods])
print([food.title() for food in friend_foods])
#4-13 Buffet:
print('----------------------------------------')
basic_foods = ('pizza salami', 'spaghetti bolognese', 'bruscetta', 'pizza tonno', 'wiener schnitzel')
print([food for food in basic_foods])
#basic_foods[0] = 'pizza margherita'
basic_foods = ('pizza salami', 'spaghetti bolognese', 'bruscetta', 'pizza margherita', 'currywurst')
print([food for food in basic_foods])
