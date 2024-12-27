// tracking.js
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

// Mock disaster response data
let disasterResponses = [
    { id: 1, location: 'City A', status: 'Ongoing', resources: 5 },
    { id: 2, location: 'City B', status: 'Completed', resources: 8 },
];

// Event listeners for real-time monitoring
io.on('connection', (socket) => {
    console.log('User connected:', socket.id);

    // Send initial disaster response data
    socket.emit('update_responses', disasterResponses);

    // Simulate real-time updates
    setInterval(() => {
        // Mock update to disaster response data
        disasterResponses[0].resources -= 1;
        if (disasterResponses[0].resources <= 0) {
            disasterResponses[0].status = 'Completed';
        }
        io.emit('update_responses', disasterResponses);
    }, 5000);

    // Handle disconnection
    socket.on('disconnect', () => {
        console.log('User disconnected:', socket.id);
    });
});

// Start the server
const PORT = 5002;
server.listen(PORT, () => {
    console.log(`Real-time monitoring server running on http://localhost:${PORT}`);
});
