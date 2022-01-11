const express = require('express');
const morgan = require('morgan');

const app = express();

app.set('view engine', 'ejs');
app.set('views', __dirname + '\\views');

app.listen(3000);

app.use((req, res, next) => {
    console.log(
        'new request, host: ',
        req.hostname,
        ' path: ',
        req.path,
        ' method: ',
        req.method
    );
    next();
});

app.use((req, res, next) => {
    console.log(
        'new request, host: ',
        req.hostname,
        ' path: ',
        req.path,
        ' method: ',
        req.method
    );
    next();
});

app.get('/', (req, res) => {
    const blogs = [
        { title: 'Luigi', snippet: 'lorem ipsum' },
        { title: 'Mario', snippet: 'lorem ipsum' },
        { title: 'Bowser', snippet: 'lorem ipsum' },
    ];
    res.render('index', { title: 'home', blogs });
});
app.get('/about', (req, res) => {
    res.render('about', { title: 'About Page' });
});

app.get('/blogs/create', (req, res) => {
    res.render('create', { title: 'Create a blog' });
});

app.use((req, res) => {
    res.status(404).render('404', { title: 'About Page' });
});

// app.use((req, res) => {
//     res.statusCode = 404;
//     res.sendFile(file_path + '404.html');
// });
