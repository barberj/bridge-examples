from configit import conf_from_file
config = conf_from_file('../development.py')

from BridgePython import Bridge
from lib import Wrap

bridge = Wrap(Bridge(api_key=config.public_api_key))
client = None

def service_response(resp):
    print(resp)

service = bridge.get_service('simple')
try:
    print 'trying 1'
    service.simple(simple='test 1', callback=service_response)
except TypeError as e:
    print(e)

try:
    print 'trying 2'
    service.simple('test 2', service_response)
except TypeError as e:
    print(e)

try:
    print 'trying 3'
    service.simple('test 3', callback=service_response)
except TypeError as e:
    print(e)
bridge.connect()
