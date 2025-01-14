import argparse
import requests 
from server import LocalServer, RemoteServer
from client import Client

parser = argparse.ArgumentParser()
parser.add_argument('--server', '-s', help = 'enter json path')
parser.add_argument('-u', '--url')
args = parser.parse_args()


if args.server is not None :
    server = LocalServer.serverdata(args.server)
elif args.url is not None :
    server = RemoteServer(args.url)
else : 
    print('Error : -s or -u should be set')
    exit(-1)

client = Client(server)
client.menu() 


# server = Server.serverdata(args.server)
# client = Client(server)
# client.menu()