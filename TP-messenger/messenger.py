from datetime import datetime
import json

def serverdata(fichier):
    with open(fichier) as file:
        server = json.load(file)
        return server

server = serverdata('serverdata.json')

def users(serv):
    print('User list')
    print('---------')
    print('')

    for user in serv['users']:
        id = user['id']
        name = user['name']
        print(f'{id}. {name}')

    print('')
    print('u. new user')
    print('m. Main menu')
    print('')

    choice = input('Select an option : ')
    if choice == 'u':
        newu(server)
    elif choice == 'm':
        menu()
    else:
        print('Unknown option:', choice)
        menu()

def channels(serv):
    print('Channels list')
    print('-------------')
    print('')

    for channel in serv['channels']:
        id = channel['id']
        name = channel['name']
        print(f'{id}. {name}')

    print('')
    print('c. create channel')
    print('m. Main menu')
    print('')

    choice = input('Select an option : ')
    if choice == 'c':
        newc(server)
    elif choice == 'm':
        menu()
    else:
        print('Unknown option:', choice)
        menu()

def save(serv):
    with open('serverdata.json', 'w') as file:
        json.dump(serv, file, indent = 4)


def newu(serv):
    nom = input('nom :')
    serv['users'].append({'id' : len(serv['users']) + 1, 'name' : nom})

    save(serv)
    menu()

def newc(serv):
    nom = input('Group name :')
    chan = {'id' : len(serv['channels']) + 1, 'name' : nom, 'member_ids' : []}

    membres = input('new members :')
    groupe = [user.strip() for user in membres.split(',')]

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

    choice = input('Select an option: ')
    if choice == 'x':
        print('Bye!')
        return
    elif choice == '1':
        return users(server)
    elif choice == '2':
        return channels(server)
    else:
        print('Unknown option:', choice)
        return menu()

menu()
