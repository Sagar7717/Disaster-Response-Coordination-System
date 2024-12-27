// communication.js
const express = require('express');
const { Server } = require('socket.io');
const http = require('http');

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
    cors: {
        origin: '*',
    },
});

// Event listeners for agency communication
io.on('connection', (socket) => {
    console.log('A user connected:', socket.id);

    // Broadcast messages
    socket.on('send_message', (data) => {
        io.emit('receive_message', data);
    });

    // Handle disconnection
    socket.on('disconnect', () => {
        console.log('A user disconnected:', socket.id);
    });
});

// Start the server
const PORT = 5001;
server.listen(PORT, () => {
    console.log(`Communication server running on http://localhost:${PORT}`);
});
