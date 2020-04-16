"""Dictionaries"""
#6-1 Person:
print('----------------------------------------')
person = {
    'first_name': 'silke',
    'last_name': 'akkermann',
    'age': '25',
    'city': 'hamswehrum'
    }
print(person.get('first_name'))
print(person.get('last_name'))
print(person.get('age'))
print(person.get('city'))
#6-2 Favorite Numbers:
print('----------------------------------------')
favorite_numbers = {
    'eike': 25,
    'silke': 30,
    'werner': 777,
    'laura': 16,
    'gaby': 19
    }
print(favorite_numbers.get('eike'))
print(favorite_numbers.get('silke'))
print(favorite_numbers.get('werner'))
print(favorite_numbers.get('laura'))
print(favorite_numbers.get('gaby'))
