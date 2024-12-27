// server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize Express app
const app = express();
app.use(cors());
app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/disaster_relief', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

const resourceSchema = new mongoose.Schema({
    name: String,
    quantity: Number,
    location: String,
    status: { type: String, default: 'available' },
});

const Resource = mongoose.model('Resource', resourceSchema);

// Routes
app.get('/resources', async (req, res) => {
    try {
        const resources = await Resource.find();
        res.json(resources);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch resources' });
    }
});

app.post('/resources', async (req, res) => {
    try {
        const newResource = new Resource(req.body);
        await newResource.save();
        res.status(201).json(newResource);
    } catch (error) {
        res.status(400).json({ error: 'Failed to add resource' });
    }
});

app.patch('/resources/:id', async (req, res) => {
    try {
        const updatedResource = await Resource.findByIdAndUpdate(
            req.params.id,
            req.body,
            { new: true }
        );
        res.json(updatedResource);
    } catch (error) {
        res.status(400).json({ error: 'Failed to update resource' });
    }
});

app.delete('/resources/:id', async (req, res) => {
    try {
        await Resource.findByIdAndDelete(req.params.id);
        res.status(204).send();
    } catch (error) {
        res.status(400).json({ error: 'Failed to delete resource' });
    }
});

// Start the server
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
