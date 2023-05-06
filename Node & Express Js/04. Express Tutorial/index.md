# Node Js Server

```

const { readFileSync } = require("fs");
const http=require("http");

const homePage=readFileSync(filePath); // html file
const homeStyles=readFileSync(filePath); // style file
const homeImage=readFileSync(filePath); // image file
const homeLogic=readFileSync(filePath); // logic file

const server=http.createServer((req,res)=>{
    console.log(req.url);
    if(req.url==='/'){
        res.writeHead(200,{'content-type':'text/html'});
        res.write(homePage);
        res.end();
    }
    else if(req.url==='/about'){
        res.writeHead(200,{'content-type':'text/html'});
        res.write('<h1>About Page</h1>');
        res.end();
    }
    else if(req.url==='/styles.css'){
        res.writeHead(200,{'content-type':'text/css'});
        res.write(homeStyles);
        res.end();
    }
    else if(req.url==='/logo.svg'){
        res.writeHead(200,{'content-type':'image/svg+xml'});
        res.write(homeImage);
        res.end();
    }
    else if(req.url==='/browser-app.js'){
        res.writeHead(200,{'content-type':'text/javascript'});
        res.write(homeLogic);
        res.end();
    }
    else {
        res.writeHead(404,{'content-type':'text/html'});
        res.write('<h1>Page Not Found</h1>');
        res.end();
    }
})

server.listen(5000);

```