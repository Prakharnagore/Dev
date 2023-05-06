# 01. What is Common JS & ES6 Modules ?

# 02. How does node evaluate our code ?

1. REPL - Read Event Print Loop.
2. CLI Executable - Running our code in node.
   To run CLI

```
node
```

# 03. What is REPL ?

# 04. Create a HTTP server ?

```
const server=http.createServer((req,res)=>{
    if(req.url==='/'){
    res.write('Home');
    res.end();
    }
     if(req.url==='/about'){
    res.end(`<h1>About</h1>`);
    }
})

server.listen(5000);
```

# What is Event Loop ?
