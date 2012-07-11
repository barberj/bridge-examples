from configit import conf_from_file
config = conf_from_file('../development.py')

from BridgePython import Bridge

class AuthHandler(object):
  def join(self, room, password, obj, callback):
    if password == "secret123":
      print ('Welcome!')
      # new: join channel using the client's objects
      bridge.join_channel(room, obj, callback=callback)
    else:
      print ('Sorry!')

bridge = Bridge(api_key=config.private_api_key)
bridge.publish_service('auth', AuthHandler())

bridge.connect()
