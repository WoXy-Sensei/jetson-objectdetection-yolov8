from ntcore import NetworkTable
from utils.log import log


class NetworkTableManagement:
    def __init__(self, table: NetworkTable):
        self.table = table
        self.publishers = {}
        self.subscribers = {}

    def doublePublisher(self, name, value):
        self.publishers[name] = self.table.getDoubleTopic(name).publish()
        publisher = self.publishers[name]
        publisher.set(value)
        log("Created publisher for -> " + name, "success")

    def stringPublisher(self, name, value):
        self.publishers[name] = self.table.getStringTopic(name).publish()
        publisher = self.publishers[name]
        publisher.set(value)
        log("Created publisher for -> " + name, "success")

    def integerPublisher(self, name, value):
        self.publishers[name] = self.table.getIntegerTopic(name).publish()
        publisher = self.publishers[name]
        publisher.set(value)
        log("Created publisher for -> " + name, "success")

    def booleanPublisher(self, name, value):
        self.publishers[name] = self.table.getBooleanTopic(name).publish()
        publisher = self.publishers[name]
        publisher.set(value)
        log("Created publisher for -> " + name, "success")

    def set(self, name, value):
        if (name in self.publishers):
            self.publishers[name].set(value)
        else:
            log("No publisher for -> " + name, "danger")

    def doubleSubscriber(self, name, callback):
        self.subscribers[name] = self.table.getDoubleTopic(name).subscribe(0.0)
        log("Created subscriber for -> " + name, "success")

    def stringSubscriber(self, name, callback):
        self.subscribers[name] = self.table.getStringTopic(name).subscribe("")
        log("Created subscriber for -> " + name, "success")

    def integerSubscriber(self, name, callback):
        self.subscribers[name] = self.table.getIntegerTopic(name).subscribe(0)
        log("Created subscriber for -> " + name, "success")

    def booleanSubscriber(self, name, callback):
        self.subscribers[name] = self.table.getBooleanTopic(
            name).subscribe(False)
        log("Created subscriber for -> " + name, "success")

    def get(self, name):
        if (name in self.subscribers):
            return self.subscribers[name].get()
        else:
            log("No subscriber for -> " + name, "danger")
            return None
