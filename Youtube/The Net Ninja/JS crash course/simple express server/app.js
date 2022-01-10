const express = require('express');
const app = express();
let file_path = __dirname + '\\views\\';

app.listen(3000);

app.get('/', (req, res) => {
    res.sendFile(file_path + 'index.html');
});
app.get('/about', (req, res) => {
    res.sendFile(file_path + 'about.html');
});
app.get('/about-us', (req, res) => {
    res.redirect('/about');
});

app.use((req, res) => {
    res.statusCode = 404;
    res.sendFile(file_path + '404.html');
});
