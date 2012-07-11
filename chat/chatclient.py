from configit import conf_from_file
config = conf_from_file('../development.py')

from BridgePython import Bridge

bridge = Bridge(api_key=config.public_api_key)

class ChatHandler(object):
    def message(self, sender, message):
        print (sender + ':' + message)

def join_callback(channel, name):
    print ("Joined channel : " + name)
    channel.message('steve', 'Bridge is pretty nifty')

auth = bridge.get_service('auth')
auth.join('bridge-lovers', 'secret123', ChatHandler(), join_callback)

bridge.connect()
