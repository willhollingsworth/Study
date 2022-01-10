const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/html');
    let file_path = __dirname + '\\views\\';
    let url = req.url;
    if (url == '/') {
        file_path += 'index.html';
        res.statusCode = 200;
    } else if (url == '/about') {
        file_path += 'about.html';
        res.statusCode = 200;
    } else if (url == '/about-me') {
        res.statusCode = 301;
        res.setHeader('Location', '/about');
        res.end();
    } else {
        file_path += '404.html';
        res.statusCode = 404;
    }
    file_path_split = file_path.split('\\');
    console.log(
        req.method,
        req.url,
        file_path_split[file_path_split.length - 1]
    );
    // console.log('reading from', file_path);
    fs.readFile(file_path, (err, data) => {
        if (err) {
            console.log(err);
            res.end();
        } else {
            res.end(data);
        }
    });
});

server.listen(3000, 'localhost', () => {
    console.log('server started on 127.0.0.1:3000');
});
