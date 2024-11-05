from datetime import datetime

server = {
    'users': [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 1, 'name': 'Town square', 'member_ids': [1, 2]}
    ],
    'messages': [
        {
            'id': 1,
            'reception_date': datetime.now(),
            'sender_id': 1,
            'channel': 1,
            'content': 'Hi 👋'
        }
    ]
}

def users(serv):
    print('User list')
    print('---------')
    print('')
    p = len(serv['users'])
    for k in range(p):
        print(serv['users'][k]['id'],serv['users'][k]['name']) 
    print('')

def channels(serv):
    print('Channels list')
    print('-------------')
    print('')
    n = len(server['channels'])
    for k in range(n):
        print(server['channels'][k]['id'], server['channels'][k]['name']) 
    print('')

def newu(serv):
    nom = input('nom :')
    serv['users'].append({'id' : len(serv['users']) + 1, 'name' : nom})

print('=== Messenger ===')
print('')
print('1. See users')
print('2. See channels')  
print('x. Leave')
print('')
print('u. new user')

choice = ''
while choice != 'x':
    choice = input('Select an option: ')
    if choice == 'x':
        print('Bye!')
    elif choice == '2':
        channels(server)
    elif choice == '1':
        users(server)
    elif choice == 'u':
        newu(server)
    else:
        print('Unknown option:', choice)



