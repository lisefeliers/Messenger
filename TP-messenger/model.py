
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'({self.id}, {self.name})'


class Channel:
    def __init__(self, id: int, name: str, members: list):
        self.id = id
        self.name = name
        self.members = members
    
    def __repr__(self):
        return f'({self.id}, {self.name}, {self.members})'
    

class Messages:
    def __init__(self, id: int, date, sender_id: int, channel, content):
        self.id = id
        self.date = date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content

    def __repr__(self):
        return f'({self.id}, {self.date}, {self.sender_id}, {self.channel}, {self.content})'