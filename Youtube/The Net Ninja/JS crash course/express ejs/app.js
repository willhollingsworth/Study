const express = require('express');
const morgan = require('morgan');
const mongoose = require('mongoose');
const fs = require('fs');
const Blog = require('./models/blog');

const app = express();

let credentials = fs.readFileSync('./credentials.json', 'utf8');
credentials = JSON.parse(credentials).uri;
mongoose
    .connect(credentials)
    .then((result) => app.listen(3000))
    .catch((err) => console.log(err));

app.set('view engine', 'ejs');
app.set('views', __dirname + '\\views');

app.use(express.static('public'));
app.use(morgan('dev'));

app.get('/add-blog', (req, res) => {
    const blog = new Blog({
        title: 'new blog',
        snippet: 'about my new blog',
        body: 'more about my new blog',
    });
    blog.save()
        .then((result) => {
            res.send(result);
        })
        .catch((err) => {
            console.log(err);
        });
});

app.get('/all-blogs', (req, res) => {
    Blog.find()
        .then((result) => res.send(result))
        .catch((err) => console.log(err));
});
app.get('/single-blogs', (req, res) => {
    Blog.findById('61dd0bcee484449ba5169f32')
        .then((result) => res.send(result))
        .catch((err) => console.log(err));
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
