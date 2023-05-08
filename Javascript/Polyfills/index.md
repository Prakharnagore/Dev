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