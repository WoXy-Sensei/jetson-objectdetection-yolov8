import websockets
from utils.log import log


class WebSocketServerManager:
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.connected_clients = {}
        self.server = None

    async def start_server(self):
        """Start the WebSocket server."""
        self.server = await websockets.serve(self.handler, self.host, self.port)
        log(f"WebSocket server running on ws://{self.host}:{self.port}")
        await self.server.wait_closed()

    async def handler(self, websocket, path):
        """Handle new client connections and messages."""
        self.connected_clients.add(websocket)
        log(f"Client connected: {websocket.remote_address}", "success")
        try:
            async for message in websocket:
                await self.process_message(websocket, message)
        except websockets.exceptions.ConnectionClosed:
            log(f"Client disconnected: {websocket.remote_address}", "warning")
        finally:
            self.connected_clients.remove(websocket)

    async def process_message(self, websocket, message):
        """Process a received message and broadcast it to all clients."""
        log(f"Received from {websocket.remote_address}: {message}")
        # Broadcast the message to all connected clients except the sender
        await self.broadcast(f"From {websocket.remote_address}: {message}", sender=websocket)

    async def broadcast(self, message, sender=None):
        """Send a message to all connected clients."""
        if self.connected_clients:
            for client in self.connected_clients:
                if client != sender:
                    try:
                        await client.send(message)
                    except Exception as e:
                        log(
                            f"Failed to send message to {client.remote_address}: {e}","danger")

    async def stop_server(self):
        """Stop the WebSocket server and close all connections."""
        if self.server:
            self.server.close()
            await self.server.wait_closed()
        # Close all connected clients
        for client in self.connected_clients:
            await client.close()
        print("WebSocket server stopped.", "warning")
