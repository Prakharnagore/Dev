# Two forms of Pre-rendering

1. Static generation - All the page are pre-generated at the build time.
2. Server-side rendering - Pages are generated on the server just at time.

Next js pre-render page that have no dynamic data.

# Static generation (pre-generate page)

Pre-generate a page (with data prepared on the server) during build time. Pages are prepared ahead to time and can be cached by the server / CDN serving app.

```
export async function getStaticProps(context){...}
```

```
export async function getStaticProps(context){

    const filePath = path.join(process.cwd(),'data','dummy.json');
    const jsonData = await fs.readFile(filePath);
    const data = JSON.parse(jsonData);

    return {
        props: {
            products:data.products,
        }
    }
}
```

``` 
export async function getStaticProps(context){

    const {params}=context;
    const productId = params.pid;
    const filePath = path.join(process.cwd(),'data','dummy.json');
    const jsonData = await fs.readFile(filePath);
    const data = JSON.parse(jsonData);
    const product = data.product.find(product => product.id === productId);

    return {
        props: {
            products:product,
        }
    }
}
```

Above code does not work for dynamic pages ex [id].js. Dynamic pages [id].js don't just need data. You also need to know which [id] value will be available. Multiple concrete [id] page instances (e.g. id=1,id=2 etc.) are pre-generated.

This issue can be solved using <em><b>Pre-generated routes</b></em>
Pre-fetches data. (as route_name.json in network inspect)

```
export async function getStaticProps(context){...}
```

```
export async function getStaticProps(context){

    const {params}=context;
    const productId = params.pid;
    const filePath = path.join(process.cwd(),'data','dummy.json');
    const jsonData = await fs.readFile(filePath);
    const data = JSON.parse(jsonData);
    const product = data.product.find(product => product.id === productId);

    return {
        props: {
            products:product,
        }
    }
}

export async function getStaticPaths(context){
return {
    paths:[
        params : {id: 'p1'},
        params : {id: 'p2'},
        params : {id: 'p3'}
        ],
    fallback: false,
    }
}
```

With fallback set to true we tell next js that even if the page in not listed in path can be valid value that should be loaded when they are visited but they are not pre-generated but they are generated just in time the request reaches the server.

```
export async function getStaticProps(context){
return {
    paths:[
        params : {id: 'p1'},
        ],
    fallback: true,
    }
}
```

With fallback set to 'blocking' next js will wait for the page to be fully be re-generated on the server before it serve client.

```
export async function getStaticProps(context){
return {
    paths:[
        params : {id: 'p1'},
        ],
    fallback: 'blocking',
    }
}
```

Suppose if someone put wrong [id] any there is no data for for that [id], we will get error. In such case returning {notFound:true} will solve the problem.

```
export async function getStaticProps(context){

    const {params}=context;
    const productId = params.pid;
    const filePath = path.join(process.cwd(),'data','dummy.json');
    const jsonData = await fs.readFile(filePath);
    const data = JSON.parse(jsonData);
    const product = data.product.find(product => product.id === productId);

    if(!product){
        return {
            notFound:true,
        }
    }

    return {
        props: {
            products:product,
        }
    }
}

export async function getStaticProps(context){
return {
    paths:[
        params : {id: 'p1'},
        ],
    fallback: true,
    }
}
```

# Incremental static generation

It means that you don't just generate your page statically once at build time but there's continuously updated even after deployment without re-deploy it.

Pre-generate a page > Re-generate it on every request, at most very X seconds.

```
export async function getStaticProps(context){

    const filePath = path.join(process.cwd(),'data','dummy.json');
    const jsonData = await fs.readFile(filePath);
    const data = JSON.parse(jsonData);

    return {
        props: {
            products:data.products,
        },
        revalidate : 10
    }
}
```

If somehow we fail to load data or if there is not data we can use re-direct or notFound as :

```
export async function getStaticProps(context){

    const filePath = path.join(process.cwd(),'data','dummy.json');
    const jsonData = await fs.readFile(filePath);
    const data = JSON.parse(jsonData);

    if(!data){
        return {
            redirect :{
                destinations:'/no-data',
            }
        }
    }

    if(data.products.length==0){
        return {
            notFound: true,
        }
    }

    return {
        props: {
            products:data.products,
        },
        revalidate : 10
    }
}
```


# Server-side page generation (generate page just in time on server)

Sometime you need to pre-render for every request or you need access to the request object ex cookies.

```
export async function getServerSideProps(context){...}
```

```
export async function getServerSideProps(context){
    const {params,req,res} = context;
return {
    props:{}
    }
}
```

# Static generation vs Server-side page generation

SSG - pre-generate page during build time.
SSR - generate page just in time on server

# Client-side data fetching

```
useSWR(<request-url>, (url) => fetch(url).then(res => res.json()))
```

# Note

1. SSR(λ) - Server-side rendering (uses getInitialProps & getServerSideProps)
2. Static(○) - automatically rendered as static HTML (uses no initial props)
3. SSG(●) - Static site generation (uses getStaticProps)
4. ISR(●) - Incremental static re-generation (uses getStaticProps)