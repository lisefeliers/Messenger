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
    
class Server:
    def __init__(self, users, channels, messages):
        self.users = users
        self.channels = channels
        self.messages = messages


def serverdata(fichier):
    with open(fichier) as file:
        server_dico = json.load(file)
    
    server = Server([], [], [])

    for user in server_dico['users']: 
        server.users.append(User(user['id'], user['name'])) 
    
    for channel in server_dico['channels']:
        server.channels.append(Channel(channel['id'], channel['name'], channel['member_ids']))
    
    for mess in server_dico['messages']:
        server.messages.append(Messages(mess['id'], mess['reception_date'], mess['sender_id'], 
                        mess['channel'], mess['content']))
        
    return server

server = serverdata('serverdata.json')


def users(serv: Server):
    print('User list')
    print('---------')
    print('')

    for user in serv.users:
        print(f'{user.id}. {user.name}')

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

    for channel in serv.channels:
        id = channel.id
        name = channel.name
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


def newu(serv: Server):
    nom = input('Nom :')
    serv.users.append(User(len(serv.users) + 1, nom))

    save(serv)
    menu()

def newc(serv: Server):
    nom = input('Group name :')
    chan = Channel(len(serv.channels) + 1, nom, [])

    membres = input('New members :')
    groupe = [user.strip() for user in membres.split(',')]

    for user in serv.users:
        if user.name in groupe :
            chan.members.append(user.id)
    
    serv.channels.append(chan)

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
