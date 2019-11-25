#3-1 names:
names = ['christian','david','arne','jan','kevin','julian']
for name in names:
    print(name.title())
#3-2 greetings
names = ['christian','david','arne','jan','kevin','julian']
for name in names:
    message = f'Hey {name.title()}, how are you?'
    print(message)
#3-3 your own list:
fav_list = ['d3','poe','d4']
for game in fav_list:
    message = f'I would like to play {game} more than reading right now.'
    print(message)
#3-4 guest list:
guest_list = ['silke','laura','mam','pap','jannes']
for guest in guest_list:
    message = f'Hiermit moechten wir dich {guest.title()} zum Dinner einladen.'
    print(message)
#3-5 changing guest list:
guest_list = ['silke','laura','mam','pap','jannes']
missing_guest = guest_list[4]
message = f'{missing_guest} kann leider nicht erscheinen!'
print(message)
guest_list[4] = 'Arko'
for guest in guest_list:
    message = f'Zum Dinner erscheinen {guest.title()}.'
    print(message)
