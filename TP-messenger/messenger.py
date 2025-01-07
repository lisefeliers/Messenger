import argparse
import requests 
from server import Server
from client import Client

parser = argparse.ArgumentParser()
parser.add_argument('--server', '-s', help = 'enter json path')
args = parser.parse_args()

server = Server.serverdata(args.server)
client = Client(server)
client.menu()