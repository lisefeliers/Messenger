from model import User, Messages, Channel
from server import Server

class Client:
    def __init__(self, server : Server):
        self.server = server
    
    def menu(self):
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
            return self.fonction_users(self.server)
        elif choice == '2':
            return self.fonction_channels(self.server)
        elif choice == '3':
            return self.fonction_messages(self.server)
        else:
            print('Unknown option:', choice)
            return self.menu()
    
    def message_to_group(self, channel_id: int, serv : Server):
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
        self.menu()

    def fonction_messages(self, serv : Server):
        print('Conversations')
        print('.............')
        print('')
        list_id = []

        print('Groups :')
        for channel in serv.channels:
            id = channel.id 
            group_name = channel.name
            list_id.append(id)
            print(f'{id}. {group_name}')

        print('m. Main menu')
        print('')

        choice = input('Select an option :')
        if choice == 'm':
            self.menu()
        elif int(choice) > max(list_id):
            print('Unknown option:', choice)
            self.menu()
        else:
            self.message_to_group(int(choice), serv)

    def fonction_channels(self, serv : Server):
        print('Channels list')
        print('-------------')
        print('')

        for channel in serv.channels:
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
            self.newc(serv)
        elif choice == 'm':
            self.menu(serv)
        elif choice == 'a':
            self.add_member_to_group(serv)
        else:
            print('Unknown option:', choice)
            self.menu()
    
    def fonction_users(self, serv : Server):
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
            self.newu(serv)
        elif choice == 'm':
            self.menu()
        else:
            print('Unknown option:', choice)
            self.menu()

    def add_member_to_group(self, serv : Server):

        print('Channels :')
        for channel in serv.channels:
            id_channel = channel.id 
            group_name = channel.name
            print(f'{id_channel}. {group_name}')

        name_channel = input('Channel name :')
        name_user = input('Add :')
        id_user = None

        for user in serv.users:
            if user.name == name_user:
                id_user = user.id
        
        for channel in serv.channels:
            if channel.name == name_channel:
                channel.members.append(id_user)

        serv.save()
        self.menu()
    
    def newu(self, serv : Server):
        name = input('Name :')
        serv.users.append(User(len(serv.users) + 1, name))

        serv.save()
        self.menu()

    def newc(self, serv : Server):
        name = input('Channel name :')
        chan = Channel(len(serv.channels) + 1, name, [])

        members = input('New members :')
        group = [user.strip() for user in members.split(',')]

        for user in serv.users:
            if user.name in group :
                chan.members.append(user.id)
        
        serv.channels.append(chan)

        serv.save()
        self.menu()