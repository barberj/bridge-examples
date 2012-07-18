from configit import conf_from_file
from datetime import datetime
config = conf_from_file('../development.py')

from BridgePython import Bridge

class Retval(object):
    def __json__(self):
        return dict(timestamp=datetime.now().isoformat())

class SimpleHandler(object):
    def simple(self, callback=None):
        if callback:
            callback(Retval().__json__())

bridge = Bridge(api_key=config.private_api_key)
bridge.publish_service('simple', SimpleHandler())

bridge.connect()
