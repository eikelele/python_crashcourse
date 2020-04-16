"""Python Crash Course Chapter 3: Introducing Lists"""
#3-1 names:
print('--------------------')
names = ['christian','david','arne','jan','kevin','julian']
for name in names:
    print(name.title())
#3-2 greetings
print('--------------------')
names = ['christian','david','arne','jan','kevin','julian']
for name in names:
    message = f'Hey {name.title()}, how are you?'
    print(message)
#3-3 your own list:
print('--------------------')
fav_list = ['d3','poe','d4']
for game in fav_list:
    message = f'I would like to play {game} more than reading right now.'
    print(message)
#3-4 guest list:
print('--------------------')
guest_list = ['silke','laura','mam','pap','jannes']
for guest in guest_list:
    message = f'Hiermit moechten wir dich, {guest.title()}, zum Dinner einladen.'
    print(message)
#3-5 changing guest list:
print('--------------------')
guest_list = ['silke','laura','mam','pap','jannes']
missing_guest = guest_list[4]
message = f'{missing_guest} kann leider nicht erscheinen!'
print(message)
guest_list[4] = 'Arko'
for guest in guest_list:
    message = f'Zum Dinner erscheinen {guest.title()}.'
    print(message)
#3-6 More guests
print('--------------------')
print('Es werden weitere Gaeste zum Essen erscheinen!')
guest_list.insert(0,'einstein')
guest_list.insert(3,'danny')
guest_list.append('alfred')
for guest in guest_list:
    message = f'Hallo {guest.title()}! Hiermit bist du zum Dinner eingeladen!'
    print(message)
#3-7 Shrinking the guest list:
print('--------------------')
for guest in guest_list:
    message = f"Hi {guest.title()}! I can only invite two people, because the dinner table didn't arrive. Sorry!"
    print(message)
print(guest_list)
while len(guest_list) !=2: #decrease the number of guests by .pop()-method till 2 are left
    not_guest = guest_list.pop()
    message = f" Sorry {not_guest.title()}! The invitation is canceled."
    print(message)
for guest in guest_list:
    message = f"Hey {guest.title()}! You are still invited!"
    print(message)
while len(guest_list) != 0: #decrease the number of guests to 0 by .pop()-method
    del(guest_list[0])
print(guest_list)
print(f"The list has {len(guest_list)} items.")
#3-8
print('--------------------')
locations = ['Blue Lagoon', 'Seychellen', 'Rom', 'Bao Bao', 'Helsinki']
print(f"Original order: {locations}")
print(f"Sorted() function order: {sorted(locations)}.")
print(f"Order not changed: {locations}") #original order not changed because sorted() is temporarily
print(f"Sorted function with reverse flag: {sorted(locations, reverse = True)}") #with reverse flag True
print(f"Order still not changed: {locations}") #original order not changed
locations.reverse() #Can't use reverse()-method inside of print because it is permanentely
print(f"After using reverse() method: {locations}")
locations.reverse() #Use .reverse method to reverse list to original Order
print(f"Back to original order: {locations}")
locations.sort() #Sort alphabetically permanentely
print(f"Sorted alphabetically by .sort() method: {locations}")
locations.sort(reverse = True)
print(f"Reverse alphabetically sorted by .sort() function: {locations}")
#3-9 Dinner guests:
print('--------------------')
guest_list = ['silke','laura','mam','pap','jannes']
print(f"Es sind insgesamt {len(guest_list)} Gaeste eingeladen.")
#3-10 Every function:
print('--------------------')
fav_food = ['hamburger','lasagne', 'gyros pita', 'wiener schnitzel mit pommes']
print(f"Meine Lieblingsgerichte sind: {fav_food}")
fav_food.append('fischbroetchen')
print(f"Ergaenzung 1: {fav_food}")
fav_food.remove('lasagne')
print(f"Ergaenzung 2: {fav_food}")
fav_food.insert(0,'doener')
print(f"Ergaenzung 3: {fav_food}")
fav_food.sort()
print(f"alphabetically sorted: {fav_food}")
fav_food.reverse()
print(f"Reverse: {fav_food}")
print(f"Ich habe {len(fav_food)} Lieblingsgerichte.")
print(f"Mein liebstes Gericht ist {fav_food[-1].title()}.")
most_fav_food = fav_food.pop()
print(most_fav_food.title())
