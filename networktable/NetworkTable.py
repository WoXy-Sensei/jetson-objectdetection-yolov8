import ntcore
from utils.log import log

class NetworkTable:
    def __init__(self, clientName, tableName, serverAdress, teamNumber) -> None:
        self.clientName = clientName
        self.tableName = tableName
        self.serverAdress = serverAdress
        self.teamNumber = int(teamNumber)

        # create a NetworkTable instance
        self.inst = ntcore.NetworkTableInstance.getDefault()
        self.inst.setServer(self.serverAdress)
        self.inst.startClient4(self.clientName)
        self.inst.setServerTeam(self.teamNumber)
        self.datatable = self.inst.getTable(self.tableName)

        log(f"Client name: {self.clientName}", "info")

        def _connect_cb(event: ntcore.Event):
            if event.is_(ntcore.EventFlags.kConnected):
                log(f"Connected to {event.data.remote_id}", "success")
            elif event.is_(ntcore.EventFlags.kDisconnected):
                log(f"Disconnected from {event.data.remote_id}", "danger")
     

        self.connListenerHandle = self.inst.addConnectionListener(True, _connect_cb)

    def get_table(self):
        return self.datatable

    def close(self):
        self.inst.removeListener(self.connListenerHandle)
