import json
from datetime import datetime
import requests
from model import User, Messages, Channel

# Ces 4 lignes étaient déjà présentes dans `messenger.py`

class LocalServer:
    def __init__(self, users: list[User], channels: list[Channel], messages: list[Messages], backup_file_name: str):
        self.users = users
        self.channels = channels
        self.messages = messages
        self.backup_file_name = backup_file_name
    
    def __repr__(self) -> str:
        return f'({self.users}, {self.channels}, {self.messages})'

    def save(self) -> None:
        with open(self.backup_file_name, 'w') as file:
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

    def get_users(self) -> 'list[User]':
        return self.users
    
    def get_channels(self) -> 'list[Channel]':
        return self.channels
    
    def get_messages(self) -> 'list[Messages]':
        return self.messages
    
    def add_user(self, name: str) -> None:
        # Attention, le nouvel id peut être plus grand que
        # le nombre d'utilisateurs. Par exemple si vous n'avez qu'un
        # seul utilisateur {"id": 2, "name": "User2"},
        # l'expression `len(self.get_users()) + 1` vous renverra 2,
        # et cet identifiant est déjà pris.
        new_id = max(user.id for user in self.get_users()) + 1
        self.get_users().append(User(new_id, name))
        self.save()

    # Il vaut mieux faire comme pour les utilisateurs et ne
    # prendre que le nom du nouveau channel en paramètre,
    # puis gérer l'id à l'intérieur du serveur.
    # En effet, l'id n'est pas généré de la même façon pour
    # `LocalServer` et pour `RemoteServer`
    def add_channel(self, name: str) -> Channel:
        new_id = max(channel.id for channel in self.channels) + 1
        # En interne de la classe, vous pouvez appeler
        # `self.channels` directement, car vous savez que la variable
        # existe. En revanche, il vaut mieux ne pas le faire
        # à l'extérieur, car si les objets `LocalServer` ont bien
        # un attribut `channels`, ce n'est pas le cas des `RemoteServer`.
        new_channel = Channel(new_id, name, [])
        self.channels.append(new_channel)
        self.save()

        return new_channel

    def send_message(self, sender_id: int, channel_id: int, content: str) -> None:
        message_id = max(message.id for message in self.messages) + 1
        message_timestamp = datetime.now()
        message = Messages(message_id, str(message_timestamp), sender_id, channel_id, content)
        self.get_messages().append(message)
        self.save()

    def add_member(self, id_channel: int, id_user: int) -> None:
        for channel in self.get_channels():
            if channel.id == id_channel:
                channel.members.append(id_user)

        self.save()
    
    # def print_details(self, id_channel):
    #     print('Membres :')
    #     for channel in self.channels : 
    #         if channel.id == id_channel :
    #             for id_user in channel.members :
    #                 for user in self.users :
    #                     if user.id == id_user :
    #                         print(f'{user.id}. {user.name}')

    #     print('')
    #     print('Messages :')
    #     for message in self.messages :
    #         if message.channel == id_channel :
    #             for user in self.users :
    #                 if message.sender_id == user.id :
    #                     print(f'{user.name} : {message.content}')
        
    #     print('m. Main menu')

    @classmethod
    def serverdata(cls, fichier):
        with open(fichier) as file:
            server_dico = json.load(file)
        
        server = cls([], [], [], fichier)

        for user in server_dico['users']: 
            server.users.append(User(user['id'], user['name'])) 
        
        for channel in server_dico['channels']:
            server.channels.append(Channel(channel['id'], channel['name'], channel['member_ids']))
        
        for mess in server_dico['messages']:
            server.messages.append(Messages(mess['id'], mess['reception_date'], mess['sender_id'], 
                            mess['channel'], mess['content']))
            
        return server

class RemoteServer:
    def __init__(self, url):
        self.url = url
    
    def get_users(self) -> 'list[User]':
        content = requests.get(f'{self.url}/users')
        users = []
        for user in content.json(): 
            users.append(User(user['id'], user['name'])) 
        return users
    
    def add_user(self, name: str) -> None:
        response = requests.post(f'{self.url}/users/create', json = {"name" : name})
        print(response.status_code, response.text)
    
    def get_channels(self) -> 'list[Channel]':
        content = requests.get(f'{self.url}/channels')
        channels = []
        for channel in content.json():
            channels.append(Channel(channel['id'], channel['name'], []))
        return channels
    
    def add_channel(self, name: str) -> Channel:
        response = requests.post(f'{self.url}/channels/create', json = {"name" : name})
        print(response.status_code, response.text)
        return Channel(response.json()['id'], response.json()['name'], [])
    
    def get_messages(self) -> 'list[Messages]':
        content = requests.get(f'{self.url}/messages')
        messages = []
        for message in content.json():
            messages.append(Messages(message['id'], message['reception_date'], message['sender_id'], 
                                     message['channel_id'], message['content']))
        return messages
    
    def send_message(self, sender_id: int, channel_id: int, content: str) -> None:
        response = requests.post(f'{self.url}/channels/{channel_id}/messages/post', json = 
                                 {"sender_id" : sender_id, "content" : content})
        print(response.status_code, response.text)
    
    def add_member(self, id_channel: int, id_user: int) -> None:
        response = requests.post(f'{self.url}/channels/{id_channel}/join', json =  {"user_id" : id_user})
        print(response.status_code, response.text)
