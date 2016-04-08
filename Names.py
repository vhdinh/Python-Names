users = {
    'Students': [
        {'first_name': 'Michael', 'last_name' : 'Jordan'},
        {'first_name': 'John', 'last_name' : 'Rosales'},
        {'first_name': 'Mark', 'last_name' : 'Guillen'},
        {'first_name': 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name' : 'Choi'},
        {'first_name': 'Martin', 'last_name' : 'Puryear'}
    ]
}

for key, person in users.items():
    print key
    count = 0
    for names in person:
        count = count + 1
        print count, " - ", names['first_name'].upper(),names['last_name'].upper()," - ", len(names['first_name']) + len(names['last_name'])