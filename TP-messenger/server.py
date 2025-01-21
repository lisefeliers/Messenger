import json
import argparse
import requests
from model import User, Messages, Channel

parser = argparse.ArgumentParser()
parser.add_argument('--server', '-s', help = 'enter json path')
parser.add_argument('-u', '--url')
args = parser.parse_args()

class LocalServer:
    def __init__(self, users: list[User], channels: list[Channel], messages: list[Messages]):
        self.users = users
        self.channels = channels
        self.messages = messages
    
    def __repr__(self):
        return f'({self.users}, {self.channels}, {self.messages})'

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
    
    def get_users(self):
        return self.users
    
    def get_channels(self):
        return self.channels
    
    def get_messages(self):
        return self.messages
    
    def add_user(self, name):
        self.get_users().append(User(len(self.get_users()) + 1, name))
        self.save()

    def add_channel(self, chan):
        self.get_channels().append(chan)
        self.save()
    
    def send_message(self, message):
        self.get_messages().append(message)
        self.save()

    def add_member(self, id_channel, id_user) : 
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
        
        server = cls([], [], [])

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
    
    def get_users(self):
        content = requests.get(f'{self.url}/users')
        users = []
        for user in content.json(): 
            users.append(User(user['id'], user['name'])) 
        return users
    
    def add_user(self, name):
        response = requests.post(f'{self.url}/users/create', json = {"name" : name})
        print(response.status_code, response.text)
    
    def get_channels(self):
        content = requests.get(f'{self.url}/channels')
        channels = []
        for channel in content.json():
            channels.append(Channel(channel['id'], channel['name'], []))
        return channels
    
    def add_channel(self, chan : Channel):
        response = requests.post(f'{self.url}/channels/create', json = {"name" : chan.name})
        print(response.status_code, response.text)
    
    def get_messages(self):
        content = requests.get(f'{self.url}/messages')
        messages = []
        for message in content.json():
            messages.append(Messages(message['id'], message['reception_date'], message['sender_id'], 
                                     message['channel_id'], message['content']))
        return messages
    
    def send_message(self, message : Messages):
        response = requests.post(f'{self.url}/channels/{message.channel}/messages/post', json = 
                                 {"sender_id" : 14, "content" : message.content})
        print(response.status_code, response.text)
    
    def add_member(self, id_channel, id_user):
        response = requests.post(f'{self.url}/channels/{id_channel}/join', json =  {"user_id" : id_user})
        print(response.status_code, response.text)