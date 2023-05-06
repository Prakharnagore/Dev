# File base Routing

```
import { useRouter } form 'next/router';

const router = useRouter()
```

# Link 

```
import Link form 'next/link';

<Link href="/about"></Link> // About is a page that we want to navigate to.
```

# Routes

```
page/static_route.js
page/[dynamicRouteId].js
page/[...catchAllRoutes].js
```