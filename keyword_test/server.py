from configit import conf_from_file
config = conf_from_file('../development.py')

from BridgePython import Bridge

class SimpleHandler(object):
    def simple(self, simple=None, callback=None):
        if simple and callback:
            callback('Simple is {0}'.format(simple))
        elif callback:
            callback('Simple not passed')

bridge = Bridge(api_key=config.private_api_key)
bridge.publish_service('simple', SimpleHandler())

bridge.connect()
