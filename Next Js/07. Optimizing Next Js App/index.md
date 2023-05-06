# head tag

```
import Head from 'next/head'

<Head>
    <title>Title</title>
    <meta name='description' content='hello world' />
</Head>
```

# _document.js

```
import Document,{Html,Head,Main,NextScript} from 'next/document';

class MyDocument extends Document{
    render(){
        return <Html lang='en'>
            <Head/>
            <body>
            <Main/>
            <NextScript/>
            // extra element div for portals
            <div class='root'></div>
            </body>
        </Html>
    }
}
```

# image

Images are lazy loaded that is next js, image is loaded when it is needed.

```
import Image from 'next/image'

<Image src="" alt="" />
```
