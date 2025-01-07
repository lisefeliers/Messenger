import json
import argparse
from model import User, Messages, Channel

parser = argparse.ArgumentParser()
parser.add_argument('--server', '-s', help = 'enter json path')
args = parser.parse_args()

class Server:
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