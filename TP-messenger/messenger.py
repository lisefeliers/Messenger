from datetime import datetime
import json

with open('serverdata.json') as file:
    server = json.load(file)


# server = {
#     'users': [
#         {'id': 1, 'name': 'Alice'},
#         {'id': 2, 'name': 'Bob'}
#     ],
#     'channels': [
#         {'id': 1, 'name': 'Town square', 'member_ids': [1, 2]}
#     ],
#     'messages': [
#         {
#             'id': 1,
#             'reception_date': datetime.now(),
#             'sender_id': 1,
#             'channel': 1,
#             'content': 'Hi 👋'
#         }
#     ]
# }

def users(serv):
    print('User list')
    print('---------')
    print('')
    p = len(serv['users'])
    for k in range(p):
        print(serv['users'][k]['id'],serv['users'][k]['name']) 
    print('')
    print('u. new user')
    print('m. Main menu')
    print('')

def channels(serv):
    print('Channels list')
    print('-------------')
    print('')
    n = len(server['channels'])
    for k in range(n):
        print(server['channels'][k]['id'], server['channels'][k]['name']) 
    print('')
    print('c. create channel')
    print('m. Main menu')
    print('')

def save(serv):
    with open('serverdata.json', 'w') as file:
        json.dump(server, file, indent = 4)


def newu(serv):
    nom = input('nom :')
    serv['users'].append({'id' : len(serv['users']) + 1, 'name' : nom})

    save(serv)
    menu()

def newc(serv):
    nom = input('nom du groupe :')
    chan = {'id' : len(serv['channels']) + 1, 'name' : nom, 'member_ids' : []}

    membres = input('nouveaux membres :')
    groupe = [user.strip() for user in membres.split()]

    for user in serv['users']:
        if user['name'] in groupe :
            chan['member_ids'].append(user['id'])
    
    serv['channels'].append(chan)

    save(serv)
    menu()

def menu():
    print('=== Messenger ===')
    print('')
    print('1. See users')
    print('2. See channels')  
    print('x. Leave')
    print('')


menu()
choice = ''
while choice != 'x':
    choice = input('Select an option: ')
    if choice == 'x':
        print('Bye!')

    elif choice == '2':
        channels(server)
        choice2 = input('Select an option : ')
        if choice2 == 'c':
            newc(server)
        elif choice2 == 'm':
            menu()
        else:
            print('Unknown option:', choice2)
            menu()

    elif choice == '1':
        users(server)
        choice2 = input('Select an option : ')
        if choice2 == 'u':
            newu(server)
        elif choice2 == 'm':
            menu()
        else:
            print('Unknown option:', choice2)
            menu()

    else:
        print('Unknown option:', choice)
        menu()



