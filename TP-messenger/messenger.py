from datetime import datetime
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--server', '-s', help = 'enter json path')
args = parser.parse_args()


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'({self.id}, {self.name})'
    
    # @classmethod
    # def from_dict(cls, user_dict: dict):
    #     return cls(user_dict['id'], user_dict['name'])

class Channel:
    def __init__(self, id: int, name: str, members: list):
        self.id = id
        self.name = name
        self.members = members
    
    def __repr__(self):
        return f'({self.id}, {self.name}, {self.members})'
    
    # @classmethod
    # def from_dict(cls, channel_dict: dict):
    #     return cls(channel_dict['id'], channel_dict['name'], channel_dict['members_id'])
    

class Messages:
    def __init__(self, id: int, date, sender_id: int, channel, content):
        self.id = id
        self.date = date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content

    def __repr__(self):
        return f'({self.id}, {self.date}, {self.sender_id}, {self.channel}, {self.content})'

    

class Server:
    def __init__(self, users: list[User], channels: list[Channel], messages: list[Messages]):
        self.users = users
        self.channels = channels
        self.messages = messages
    
    def __repr__(self):
        return f'({self.users}, {self.channels}, {self.messages})'
    
    def newu(self):
        name = input('Name :')
        self.users.append(User(len(self.users) + 1, name))

        self.save()
        menu()

    def newc(self):
        name = input('Channel name :')
        chan = Channel(len(self.channels) + 1, name, [])

        members = input('New members :')
        group = [user.strip() for user in members.split(',')]

        for user in self.users:
            if user.name in group :
                chan.members.append(user.id)
        
        self.channels.append(chan)

        self.save()
        menu()
    
    def add_member_to_group(self):

        print('Channels :')
        for channel in self.channels:
            id_channel = channel.id 
            group_name = channel.name
            print(f'{id_channel}. {group_name}')

        name_channel = input('Channel name :')
        name_user = input('Add :')
        id_user = None

        for user in self.users:
            if user.name == name_user:
                id_user = user.id
        
        for channel in self.channels:
            if channel.name == name_channel:
                channel.members.append(id_user)

        self.save()
        menu()

    def fonction_users(self):
        print('User list')
        print('---------')
        print('')

        for user in self.users:
            print(f'{user.id}. {user.name}')

        print('')
        print('u. new user')
        print('m. Main menu')
        print('')

        choice = input('Select an option : ')
        if choice == 'u':
            self.newu()
        elif choice == 'm':
            menu()
        else:
            print('Unknown option:', choice)
            menu()

    def fonction_channels(self):
        print('Channels list')
        print('-------------')
        print('')

        for channel in self.channels:
            id = channel.id
            name = channel.name
            print(f'{id}. {name}')

        print('')
        print('a. Add a member to a channel')
        print('c. Create channel')
        print('m. Main menu')
        print('')

        choice = input('Select an option : ')
        if choice == 'c':
            self.newc()
        elif choice == 'm':
            menu()
        elif choice == 'a':
            self.add_member_to_group()
        else:
            print('Unknown option:', choice)
            menu()

    def fonction_messages(self):
        print('Conversations')
        print('.............')
        print('')
        list_id = []

        print('Groups :')
        for channel in self.channels:
            id = channel.id 
            group_name = channel.name
            list_id.append(id)
            print(f'{id}. {group_name}')

        print('m. Main menu')
        print('')

        choice = input('Select an option :')
        if choice == 'm':
            menu()
        elif int(choice) > max(list_id):
            print('Unknown option:', choice)
            menu()
        else:
            message_to_group(int(choice), self)

    def save(self):
        with open(args.server, 'w') as file:
            json.dump(self.class_to_dict(), file, indent = 4)

    def class_to_dict(self):
        server = {'users': [], 'channels': [], 'messages': []}

        for user in self.users: 
            server['users'].append({'id': user.id, 'name': user.name})
    
        for channel in self.channels:
            server['channels'].append({'id': channel.id, 'name': channel.name,'member_ids': channel.members})

        for message in self.messages:
            server['messages'].append({'id': message.id,'reception_date': message.date,'sender_id': message.sender_id,
                'channel': message.channel,'content': message.content})
        
        return server


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

server = serverdata(args.server)


def message_to_group(channel_id: int, serv: Server):
    name = ''
    for channel in serv.channels:
        if channel.id == id:
            name = channel.name
    print(f'{name}')
    new_message = input('New message :')
    message_id = len(serv.messages) + 1
    sender_id = 1
    message = Messages(message_id, '2024-12-12', sender_id, channel_id, new_message)
    serv.messages.append(message)

    serv.save()
    menu()


def menu():
    print('=== Messenger ===')
    print('')
    print('1. See users')
    print('2. See channels')  
    print('3. Messages')
    print('x. Leave')
    print('')

    choice = input('Select an option: ')
    if choice == 'x':
        print('Bye!')
        return
    elif choice == '1':
        return server.fonction_users()
    elif choice == '2':
        return server.fonction_channels()
    elif choice == '3':
        return server.fonction_messages()
    else:
        print('Unknown option:', choice)
        return menu()

menu()