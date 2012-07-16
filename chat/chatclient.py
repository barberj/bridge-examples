from configit import conf_from_file
config = conf_from_file('../development.py')

from BridgePython import Bridge

bridge = Bridge(api_key=config.public_api_key)
client = None

def get_text(msg=None):
    if msg:
        print(msg)
    return raw_input('>>> ')


class ChatHandler(object):
    def __init__(self, sender):
        self.sender = sender

    def join(self, channel_name='bridge-lovers'):
        auth = bridge.get_service('auth')
        password = get_text('Enter password:')
        auth.join(channel_name,
            self.sender,
            password,
            self,
            join_callback)

    def message(self, message):
        print (self.sender + ': ' + message)

def join_callback(channel, channel_name):
    global client
    print ("Joined channel {0}.".format(channel_name))
    client.channel = channel
    bridge.emit('converse')

def ready():
    global client
    client = ChatHandler(get_text('What is your name?'))
    client.join(get_text('Enter channel to join:'))

def message():
    txt = get_text()
    client.channel.message(txt)
    bridge.emit('converse')

# events
bridge.on('ready', ready)
bridge.on('converse', message)

bridge.connect()
