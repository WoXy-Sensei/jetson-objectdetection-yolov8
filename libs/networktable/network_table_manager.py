from ntcore import NetworkTable
from libs.utils.log import log


class NetworkTableManager:
    def __init__(self, table: NetworkTable):
        self.table = table
        self.publishers = {}
        self.subscribers = {}

    def doublePublisher(self, name, value):
        """
        Create a double publisher

        Args:
            name (str): The name of the publisher
            value (float): The value of the publisher
        """
        self.publishers[name] = self.table.getDoubleTopic(name).publish()
        publisher = self.publishers[name]
        publisher.set(value)
        log("Created publisher for -> " + name, "success")

    def stringPublisher(self, name, value):
        """
        Create a string publisher

        Args:
            name (str): The name of the publisher
            value (str): The value of the publisher
        """
        self.publishers[name] = self.table.getStringTopic(name).publish()
        publisher = self.publishers[name]
        publisher.set(value)
        log("Created publisher for -> " + name, "success")

    def integerPublisher(self, name, value):
        """
        Create an integer publisher

        Args:
            name (str): The name of the publisher
            value (int): The value of the publisher
        """
        self.publishers[name] = self.table.getIntegerTopic(name).publish()
        publisher = self.publishers[name]
        publisher.set(value)
        log("Created publisher for -> " + name, "success")

    def booleanPublisher(self, name, value):
        """
        Create a boolean publisher

        Args:
            name (str): The name of the publisher
            value (bool): The value of the publisher
        """
        self.publishers[name] = self.table.getBooleanTopic(name).publish()
        publisher = self.publishers[name]
        publisher.set(value)
        log("Created publisher for -> " + name, "success")

    def set(self, name, value):
        """
        Set the value of a publisher

        Args:
            name (str): The name of the publisher
            value (any): The value of the publisher
        """
        if (name in self.publishers):
            self.publishers[name].set(value)
        else:
            log("No publisher for -> " + name, "danger")

    def doubleSubscriber(self, name):
        """
        Create a double subscriber

        Args:
            name (str): The name of the subscriber
        """
        self.subscribers[name] = self.table.getDoubleTopic(name).subscribe(0.0)
        log("Created subscriber for -> " + name, "success")

    def stringSubscriber(self, name):
        """ 
        Create a string subscriber

        Args:
            name (str): The name of the subscriber
        """
        self.subscribers[name] = self.table.getStringTopic(name).subscribe("")
        log("Created subscriber for -> " + name, "success")

    def integerSubscriber(self, name):
        """
        Create an integer subscriber

        Args:
            name (str): The name of the subscriber
        """
        self.subscribers[name] = self.table.getIntegerTopic(name).subscribe(0)
        log("Created subscriber for -> " + name, "success")

    def booleanSubscriber(self, name):
        """ 
        Create a boolean subscriber

        Args:
            name (str): The name of the subscriber
        """
        self.subscribers[name] = self.table.getBooleanTopic(
            name).subscribe(False)
        log("Created subscriber for -> " + name, "success")

    def get(self, name):
        """ 
        Get the value of a subscriber

        Args:  
            name (str): The name of the subscriber
        """
        if (name in self.subscribers):
            return self.subscribers[name].get()
        else:
            log("No subscriber for -> " + name, "danger")
            return None
