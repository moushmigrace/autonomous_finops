const express = require("express");
const os = require("os");

const app = express();
const PORT = 3000;

let activeRequests = 0;

app.get("/health", (req, res) => {
    res.json({
        status: "ok",
        cpu: os.loadavg(),
        memory: process.memoryUsage(),
        activeRequests
    });
});

// CPU stress API
app.get("/cpu-stress", (req, res) => {
    const duration = parseInt(req.query.duration) || 5000;
    const start = Date.now();

    while (Date.now() - start < duration) {
        Math.sqrt(Math.random());
    }

    res.send(`CPU stressed for ${duration} ms`);
});

app.get("/metrics", (req, res) => {
    res.json({
        cpuLoad: os.loadavg(),
        memoryUsage: process.memoryUsage(),
        uptime: process.uptime(),
        activeRequests
    });
});

// Memory stress API
app.get("/memory-stress", (req, res) => {
    const sizeMB = parseInt(req.query.size) || 100;
    const arr = [];

    for (let i = 0; i < sizeMB * 1024 * 1024 / 8; i++) {
        arr.push(i);
    }

    res.send(`Allocated ${sizeMB} MB memory`);
});

// Simulate normal traffic
app.get("/users", async (req, res) => {
    activeRequests++;

    setTimeout(() => {
        activeRequests--;
    }, 1000);

    res.json({
        users: Math.floor(Math.random() * 1000),
        activeRequests
    });
});

// Idle endpoint
app.get("/idle", (req, res) => {
    res.send("System idle");
});

// I/O stress simulation
app.get("/io-stress", async (req, res) => {
    activeRequests++;

    await new Promise(resolve => setTimeout(resolve, 5000));

    activeRequests--;

    res.send("I/O stress completed");
});
app.get("/spike", async (req, res) => {
    for (let i = 0; i < 100000000; i++) {
        Math.random();
    }

    res.send("Traffic spike simulated");
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});