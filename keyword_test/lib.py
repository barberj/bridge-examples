"""
Wrapper provided by googlegroup to handle keywords.
https://groups.google.com/d/topic/bridge-users/kk3x7cIc-5s/discussion
"""
class Wrap():
    def __init__(self, bridge):
        self.bridge = bridge
    def get_service(self, svcName):
        return RemoteService(self.bridge.get_service(svcName))
    def publish_service(self, svcName, svc):
        return self.bridge.publish_service(svcName, WrappedService(svc))
    def join_channel(self, name, handler, writeable=True, callback=None):
        return self.bridge.joinChannel(name, WrappedService(handler),
                                       writeable, callback)
    def get_channel(self, channelName):
        return RemoteService(self.bridge.get_channel(channelName))
    def connect(self):
        self.bridge.connect()
    def __getattr__(self, attr):
        return getattr(self.bridge, attr)

def test_params(*args, **kwargs):
    print args
    print kwargs

class RemoteService():
    def __init__(self, svc):
        self.svc = svc
    def __getattr__(self, attr):
        if getattr(self.svc, attr):
            return lambda *args, **kwargs: getattr(self.svc, attr)(*(args + (kwargs,)))
            return lambda *args, **kwargs: test_params(*(args +(kwargs,)))
        raise AttributeError(attr)

class WrappedService():
    def __init__(self, svc):
        self.svc = svc
    def __getattr__(self, attr):
        if getattr(self.svc, attr):
            return lambda *args: getattr(self.svc, attr)(*args[:-1], **args[-1])
            return lambda *args: test_params(*args[:-1], **args[-1])
        raise AttributeError(attr)
