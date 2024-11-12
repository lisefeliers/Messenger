from datetime import datetime
import json


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Channel:
    def __init__(self, id, name, members):
        self.id = id
        self.name = name
        self.members = members
        
class Messages:
    def __init__(self, id, date, sender_id, channel, content):
        self.id = id
        self.date = date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content
    

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
    print('c. Create channel')
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
    nom = input('Nom :')
    serv['users'].append({'id' : len(serv['users']) + 1, 'name' : nom})

    save(serv)
    menu()

def newc(serv):
    nom = input('Group name :')
    chan = {'id' : len(serv['channels']) + 1, 'name' : nom, 'member_ids' : []}

    membres = input('New members :')
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
