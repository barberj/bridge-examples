from configit import conf_from_file
config = conf_from_file('../development.py')

from BridgePython import Bridge


class AuthHandler(object):
    def join(self, channel_name, user, password, handler, callback):
        if True or password == "secret123":
            print ('{0} has joined chat at {1}.'.format(
                user, channel_name))
            bridge.emit('join', channel_name, handler, callback)
        else:
            print ('{0} is not authorized.'.format(
                user))

def join(channel_name, handler, callback):
    bridge.join_channel(channel_name, handler, callback=callback)

def leave(channel_name, handler, callback):
    bridge.leave_channel(channel_name, handler, callback=callback)

bridge = Bridge(api_key=config.private_api_key)

# events
bridge.on('join', join)
bridge.on('leave', leave)

# services
bridge.publish_service('auth', AuthHandler())

bridge.connect()
