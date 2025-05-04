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
    
    def message_to_group(self, channel_id: int) -> None:
        # Plutôt que de stocker les id et name séparément,
        # vous auriez pu prendre un objet `Channel` en paramètre.
        name = ''
        for channel in self.server.get_channels():
            if channel.id == channel_id:
                name = channel.name
        print(f'{name}')
        new_message = input('New message :')
        sender_id = 1 # Vous pouvez aussi demander à l'utilisateur
                      # quel est son nom ou son id

        self.server.send_message(sender_id, channel_id, new_message)
        self.menu()

    def fonction_messages(self):
        print('Conversations')
        print('.............')
        print('')
        # Il vaut mieux utiliser un nom qui désigne ce qui est représenté
        # plutôt que comment c'est représenté.
        # Par exemple `channel_ids` est plus informatif que `list_id`.
        # Le fait que cette variable soit une liste sera toujours
        # indiqué par son type, visible dans l'IDE à tout moment.
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
        # Il vaut mieux vérifier la présence de `choice` dans la liste,
        # car rien ne vous assure qu'une liste contient tous les ids
        # entre 1 et son max.
        elif choice not in list_id:
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

    def add_member_to_group(self) -> None:

        print('Channels :')
        for channel in self.server.get_channels():
            id_channel = channel.id 
            group_name = channel.name
            print(f'{id_channel}. {group_name}')

        id_channel = int(input('Channel :'))
        name_user = input('Add :')
        id_user = None

        for user in self.server.get_users():
            if user.name == name_user:
                id_user = user.id
        # N'oubliez pas de vérifier que `id_user is not None`,
        # l'utilisateur a pu se tromper

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
        
    # Il vaut mieux éviter d'utiliser des abréviations comme "u",
    # car vous perdez beaucoup plus en lisibilité que
    # ce que vous avez économisé en temps d'écriture
    def newu(self):
        name = input('Name :')
        self.server.add_user(name)
        self.menu()

    def newc(self) -> None:
        name = input('Channel name :')
        # C'est du ressort du serveur de créer l'objet `Channel`,
        # notamment car c'est lui qui décide comment gérer l'id.
        chan = self.server.add_channel(name)

        members = input('New members :')
        group = [user.strip() for user in members.split(',')]

        for user in self.server.get_users():
            if user.name in group :
                self.server.add_member(chan.id, user.id)

        self.menu()
