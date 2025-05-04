class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        # Préciser le nom de la classe dans la fonction `__repr__`
        # vous aidera à comprendre plus rapidement ce qui s'affiche
        return f'User({self.id}, {self.name})'


class Channel:
    def __init__(self, id: int, name: str, members: list):
        self.id = id
        self.name = name
        self.members = members
    
    def __repr__(self) -> str:
        return f'Channel({self.id}, {self.name}, {self.members})'
    

class Messages:
    def __init__(self, id: int, date, sender_id: int, channel, content):
        self.id = id
        self.date = date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content

    def __repr__(self) -> str:
        return f'Messages({self.id}, {self.date}, {self.sender_id}, {self.channel}, {self.content})'
