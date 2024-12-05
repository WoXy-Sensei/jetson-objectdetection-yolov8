from networktable.NetworkTable import NetworkTable
from networktable.NetworkTableManagement import NetworkTableManagement
import os
from utils.log import log
from dotenv import load_dotenv


class Robot:
    def __init__(self):
        load_dotenv(override=True)
        clientName = os.getenv("CLIENT_NAME")
        tableName = os.getenv("TABLE_NAME")
        serverAdress = os.getenv("SERVER_ADRESS")
        teamNumber = os.getenv("TEAM_NUMBER")
        log(f"""
            Client Name: {clientName}
            Table Name: {tableName}
            Server Adress: {serverAdress}
            Team Number: {teamNumber}
        """)
        self.inst = NetworkTable(clientName, tableName, serverAdress, teamNumber).get_table()
        self.manager = NetworkTableManagement(self.inst)
        # Create a publishers and subscribers
        self.test = self.manager.doublePublisher("test", 0)

    def send_data(self, name, data):
        self.manager.set(name, data)

    def get_data(self, name):
        return self.manager.get(name)
