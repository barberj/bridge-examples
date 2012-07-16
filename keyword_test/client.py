from configit import conf_from_file
config = conf_from_file('../development.py')

from BridgePython import Bridge

bridge = Bridge(api_key=config.public_api_key)
client = None

def service_response(resp):
    print(resp)

service = bridge.get_service('simple')
try:
    service.simple(simple='simple text', callback=service_response)
except TypeError as e:
    print(e)

service.simple('simple text', service_response)

bridge.connect()
