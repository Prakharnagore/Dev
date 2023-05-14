# API routes

API - Application Programming Interface.
REST - Representational state transfer.

1. Create folder "pages/api" for creating api routes.

```
pages/api/feedback.js

function handler(req,res){
    if(req.method==='POST'){...}
    else{
        res.status(200).json({});
    }
}
export default handler;
```

2. Create dynamic route using 'pages/api/[id].js'

3. Create catch all dynamic route using 'pages/api/[...id].js'