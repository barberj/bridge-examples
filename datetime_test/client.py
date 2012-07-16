from configit import conf_from_file
config = conf_from_file('../development.py')

from BridgePython import Bridge

bridge = Bridge(api_key=config.public_api_key)
client = None

def service_response(resp):
    print(resp)

service = bridge.get_service('simple')
service.simple(service_response)
"""
Prints out:
$ python client.py
<BridgePython.reference.Reference object at 0x10b84f8d0>

Haven't figured out how to get this Reference object to give me the datetime.
"""

bridge.connect()
