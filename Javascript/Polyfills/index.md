### map() Polyfill

```
Array.prototype.myMap = function (cb) {
  const newArray = [];
  for (let i = 0; i < this.length; i++) {
    newArray.push(cb(this[i],i,this));
  }
  return newArray;
};

const double = [1,2,3,4,5,6,7,8,9,10].myMap((item,index,arr)=>{
    return item*2
});

console.log(double);
```


### filter() Polyfill

```
Array.prototype.myFilter = function (cb) {
  const newArray = [];
  for (let i = 0; i < this.length; i++) {
   if(cb(this[i],i,this)){
    newArray.push(cb(this[i],i,this));
   }
  }
  return newArray;
};

const even = [1,2,3,4,5,6,7,8,9,10].myFilter((item,index,arr)=>{
    return item%2===0 ? item : null;
});

console.log(even);
```

### reduce() Polyfill

```
Array.prototype.myReduce = function (cb, initialValue) {
  let accumulator = initialValue;
  for (let i = 0; i < this.length; i++) {
    accumulator = accumulator ? cb(accumulator, this[i], i, this) : this[i];
  }
  return accumulator;
};

const data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].myReduce(
  (accumulator, current, index, array) => {
    return accumulator + current;
  },
  0
);

console.log(data);
```

### once() func lodash polyfill 

```
function once(func, context) {
  let ran;
  return function () {
    if (func) {
      ran = func.apply(context || this, arguments);
      func = null;
    }
    return ran;
  };
}
const hello = once((a,b)=>console.log("hello",a,b));

hello(1,2);
hello(1,2);
hello(1,2);
hello(1,2);
hello(1,2);
```

### call() polyfill

```
Function.prototype.myCall = function (context = {}, ...args) {
  if (typeof this !== "function") {
    throw new Error(this + " is not a function");
  }
  context.fn = this;
  return context.fn(...args);
};

var obj = { name: "hello world" };
function sayHelloWorld(age) {
  return this.name + " " + age;
}

sayHelloWorld.myCall(obj, 100);
```


### apply() polyfill :

```
Function.prototype.myApply = function (context = {}, args=[]) {
    if (typeof this !== "function") {
      throw new Error(this + " is not a function");
    }
    if(!Array.isArray(args)){
       throw new TypeError("Arguments must be an array");  
    }
    context.fn = this;
    return context.fn(...args);
  };
  
  var obj = { name: "hello world" };
  function sayHelloWorld(age) {
    return this.name + " " + age;
  }
  
  sayHelloWorld.myApply(obj, [100]);
```

### bind() polyfill :

```
Function.prototype.myApply = function (context = {}, ...args) {
  if (typeof this !== "function") {
    throw new Error(this + " is not a function");
  }

  context.fn = this;
  return (...next) => context.fn(...args,..next);
};

var obj = { name: "hello world" };

function sayHelloWorld(age) {
  return this.name + " " + age;
}

const data = sayHelloWorld.bind(obj);
console.log(data(100));

```

### promise() polyfill :

```
function PromisePolyFill(executor) {
  let onResolve,
    onReject,
    isFulFilled = false,
    isRejected = false,
    isCalled = false,
    value;

  function resolve(val) {
    isFulFilled = true;
    value = val;

    if (typeof onResolve === "function") {
      onResolve(val);
      isCalled = true;
    }
  }

  function reject(val) {
    isRejected = true;
    value = val;
    if (typeof onReject === "function") {
      onReject(val);
      isCalled = true;
    }
  }

  this.then = function (callback) {
    onResolve = callback;
    if (isFulFilled && !isCalled) {
      isCalled = true;
      onResolve(value);
    }
    return this;
  };

  this.catch = function (callback) {
    onReject = callback;
    if (isRejected && !isCalled) {
      isCalled = true;
      onReject(value);
    }
    return this;
  };

  try {
    executor(resolve, reject);
  } catch (error) {
    reject(error);
  }
}

const examplePromise = new PromisePolyFill((resolve, reject) => {
  // setTimeout(()=>{
  resolve(2);
  // },1000);
});

console.log(examplePromise);

examplePromise
  .then((res) => {
    console.log("res", res);
  })
  .catch((err) => console.error(err));

PromisePolyFill.resolve=(val)=>{
    return new PromisePolyFill(function executor(resolve,reject){
      resolve(val);
    })
  }

PromisePolyFill.reject=(val)=>{
    return new PromisePolyFill(function executor(resolve,reject){
      reject(val);
    })
  }
```

### Promise.all([]) polyfill : 

```
Promise.allPolyFill = (promises) => {
  return new Promise((resolve, reject) => {
    const results = [];

    if (!promises.length) {
      resolve(results);
      return;
    }
    
    let pending = promises.length;

    promises.forEach((promise, idx) => {
      Promise.resolve(promise).then((res) => {
        results[idx] = res;
        pending--;
        if (pending == 0) {
          resolve(results);
        }
      }, reject);
    });
  });
};

```

### debounce() polyfill

```
const myDebounce = (cb,d)=>{
  let timer;
  return function(...args) {
    if(timer){
      clearTimeout(timer);
    }
    timer = setTimeout(()=>{
      cb(...args);
      timer=null;
    },d);
  }
}
```

### Throttle() polyfill

```
const myThrottle = (cb,d)=>{
  let last = 0;
  return function (...args){
    let now = new Date().getTime();
    if(now - last < d) return;
    last = now;
    return cb(...args);
  }
}
```

