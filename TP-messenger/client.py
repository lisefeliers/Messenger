from model import  Messages, Channel
from server import LocalServer, RemoteServer

class Client:
    def __init__(self, server : LocalServer| RemoteServer):
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
            return self.fonction_users()
        elif choice == '2':
            return self.fonction_channels()
        elif choice == '3':
            return self.fonction_messages()
        else:
            print('Unknown option:', choice)
            return self.menu()
    
    def message_to_group(self, channel_id: int):
        name = ''
        for channel in self.server.get_channels():
            if channel.id == channel_id:
                name = channel.name
        print(f'{name}')
        new_message = input('New message :')
        message_id = len(self.server.get_messages()) + 1
        sender_id = 1
        message = Messages(message_id, '2024-12-12', sender_id, channel_id, new_message)
        
        self.server.send_message(message)
        self.menu()

    def fonction_messages(self):
        print('Conversations')
        print('.............')
        print('')
        list_id = []

        print('Groups :')
        for channel in self.server.get_channels():
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
            self.message_to_group(int(choice))

    def fonction_channels(self):
        print('Channels')
        print('-------------')
        print('')

        for channel in self.server.get_channels():
            id = channel.id
            name = channel.name
            print(f'{id}. {name}')

        print('')
        print('a. Add a member to a channel')
        print('d. Details channel')
        print('c. Create channel')
        print('m. Main menu')
        print('')

        choice = input('Select an option : ')
        if choice == 'c':
            self.newc()
        elif choice == 'm':
            self.menu()
        elif choice == 'a':
            self.add_member_to_group()
        elif choice == 'd':
            self.detail()
        else:
            print('Unknown option:', choice)
            self.menu()
    
    def fonction_users(self):
        print('User list')
        print('---------')
        print('')

        for user in self.server.get_users():
            print(f'{user.id}. {user.name}')

        print('')
        print('u. new user')
        print('m. Main menu')
        print('')

        choice = input('Select an option : ')
        if choice == 'u':
            self.newu()
        elif choice == 'm':
            self.menu()
        else:
            print('Unknown option:', choice)
            self.menu()

    def add_member_to_group(self):

        print('Channels :')
        for channel in self.server.get_channels():
            id_channel = channel.id 
            group_name = channel.name
            print(f'{id_channel}. {group_name}')

        id_channel = input('Channel :')
        name_user = input('Add :')
        id_user = None

        for user in self.server.get_users():
            if user.name == name_user:
                id_user = user.id
        
        self.server.add_member(id_channel, id_user)
        self.menu()
    
    # def detail(self):
    #     print('Channels :')
    #     for channel in self.server.get_channels():
    #         id_channel = channel.id 
    #         group_name = channel.name
    #         print(f'{id_channel}. {group_name}')
        
    #     id_channel = input('Channel :')
        
    #     self.server.print_details(id_channel)
        
    def newu(self):
        name = input('Name :')
        self.server.add_user(name)
        self.menu()

    def newc(self):
        name = input('Channel name :')
        chan = Channel(len(self.server.get_channels()) + 1, name, [])

        members = input('New members :')
        group = [user.strip() for user in members.split(',')]

        for user in self.server.get_users():
            if user.name in group :
                chan.members.append(user.id)
        
        self.server.add_channel(chan)
        self.menu()