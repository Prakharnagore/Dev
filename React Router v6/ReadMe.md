1. BrowserRouter
   ```
   <BrowserRouter>
   </BrowserRouter>
   ```
2. Routes

```
 <BrowserRouter>
  <Routes>
  </Routes>
 </BrowserRouter>
```

3. Route

```
 <BrowserRouter>
  <Routes>
   <Route to="" element={</>}/>
  </Routes>
 </BrowserRouter>
```

4. Link

```
<Link to="">
</Link>
```

5. Route Params

```
 <BrowserRouter>
  <Routes>
   <Route path="/:id" element={</>}/>
  </Routes>
 </BrowserRouter>
```

6.  useParams()

```
import { useParams } from "react-router-dom"

function funName(){
const params = useParams();
return <></>
}
```

7. Nested Routes

```
/* Inside Routes Component */

<BrowserRouter>
  <Routes>
   <Route element={/* Layout Component */}>
      <Route path="" element={} />
      <Route path="" element={} />
      <Route path="" element={} />
   </Route>
</BrowserRouter>


 /* Inside Layout Component */

import { Outlet } from "react-router-dom"
<>
   /* Some Component Here */
   <Outlet />
</>
```

8. Index Route

```
<BrowserRouter>
  <Routes>
   <Route path="/" element={/* Layout Component */}>
      <Route index element={} /> /** I N D E X   R O U T E  **/
      <Route path="pathName" element={} />

      <Route path="pathName" element={/* Layout Component */}>
      <Route index element={} /> /** I N D E X   R O U T E  **/
      <Route path="pathName" element={} />
   </Route>
   </Route>
</BrowserRouter>
```

9. Nest Route dynamically

```
<BrowserRouter>
  <Routes>
   <Route path="pathName">
      <Route index element={} />
      <Route path=":id" element={} />
   </Route>
  </Route>
</BrowserRouter>
```

10. Navlink

```
<NavLink to="path" className={({active})=>active ? "" :""} >
...
</NavLink>

<NavLink to="path" style={({active})=>active ? "" :""} >
...
</NavLink>
```

11. End Matching Route

```
<NavLink to="path" end={true} className={({active})=>active ? "" :""} >
...
</NavLink>
```

12. Relative Path (for routing back back)

Examplse: vans/:id -> vans

```
<Link to=".." relative="path">Back</Link>
```

13.
