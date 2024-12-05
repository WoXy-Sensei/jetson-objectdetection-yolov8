from networktable.NetworkTable import NetworkTable
from networktable.NetworkTableManagement import NetworkTableManagement
import os
import random

class Robot:
    def __init__(self):
        clientName = os.getenv("CLIENT_NAME")
        tableName = os.getenv("TABLE_NAME")
        serverAdress = os.getenv("SERVER_ADRESS")
        teamNumber = os.getenv("TEAM_NUMBER")
        print(clientName, tableName, serverAdress, teamNumber)
        self.inst = NetworkTable(clientName, tableName, serverAdress, teamNumber).get_table()
        self.manager = NetworkTableManagement(self.inst)
        self.test = self.manager.doublePublisher("test", 0)

    def send_data(self, name , data):
        self.manager.set(name, data)
    
    def get_data(self, name):
        return self.manager.get(name)