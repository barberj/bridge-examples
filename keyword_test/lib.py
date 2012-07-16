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

class RemoteService():
    def __init__(self, svc):
        self.svc = svc
    def __getattr__(self, attr):
        if getattr(self.svc, attr):
            return lambda **kwargs: getattr(self.svc, attr)(kwargs)
        raise AttributeError(attr)

class WrappedService():
    def __init__(self, svc):
        self.svc = svc
    def __getattr__(self, attr):
        if getattr(self.svc, attr):
            return lambda kwargs: getattr(self.svc, attr)(**kwargs)
        raise AttributeError(attr)
