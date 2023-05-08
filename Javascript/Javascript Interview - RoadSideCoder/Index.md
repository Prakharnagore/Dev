### Question 1. var vs let vs const ?

```
var
1. global or function scoped
2. Can be declared without initialization
3. hoisted with value of undefined

let
1. block scoped
2. Can be declared without initialization
3. hoisted with value of uninitialized (TDZ)

const
1. block scoped
2. Cannot be declared without initialization
3. hoisted with value of uninitialized (TDZ)
```

```
function abc(){
    console.log(a,b,c);
    var a=10;
    let b=11;
    const c=12;
}
abc();

// caught ReferenceError: Cannot access 'b' before initialization
```

### Question 2. Temporal Dead Zone (TDZ)?

```
A let or const variable is said to be in a "temporal dead zone" (TDZ) from the start of the block until code execution reaches the line where the variable is declared and initialized. let and const are hoisted in temporal dead zone
```

### Question 3. map, filter and reduce Polyfills

```
Map Polyfill :

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

```
Filter Polyfill :

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

```
Reduce Polyfill : The reduce() method returns a single value.

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

### Question 4. map() vs forEach() ?

```
map()
1. return a new array
2. does not modify the original array

forEach()
1. does not return any new array.
2. modifies the original array.
```

### Question 4. funtion statements & function expressions ?

```
fn statements : function abc(){}
fn expresstion : cont abc = function(){}
```

### Question 5. What are first class functions ?

```
where fn can be treated as variable are called first class functions.
```

### Question 6. IIFE ?

```
Immediately Invoked Function Expression.

(function square(num){
  console.log(num)
})();

```

```
(function (x){
  return (function (y){
    console.log(x); // 1
  })(2)
})(1)
```

### Question 7. Lexical Scope

```
Lexical scope is the ability for a function scope to access variables from the parent scope.
```

```
Code optimized using Closure :

function find() {
  let a = [];
  for (let i = 0; i < 10000000; i++) {
    a[i] = i * i;
  }

  return function (index) {
    return a[index];
  };
}

const closure = find();
console.log(closure(6));
console.log(closure(50));
```

### Question 8. What is a Module Pattern ?

```
var Module = (function () {
  function privateMethod() {
    // do something
    console.log("private");
  }
  return {
    publicMethod: function () {
      console.log("public");
    },
  };
})();

Module.publicMethod();
Module.privateMethod();
```

### Question 9. Loadash once() function polyfill?

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

### Question 10. Implementation of caching/memoize function

```
function myMemoize(fn, context) {
  const res = {};
  return function (...args) {
    var argsCache = JSON.stringify(args);
    if (!res[argsCache]) {
      res[argsCache] = fn.call(context || this, ...args);
    }

    return res[argsCache];
  };
}

const clusmySquare = (num1, num2) => {
  for (let i = 0; i <= 10000000000; i++) {
    return num1 * num2;
  }
};

console.time("First Call");
console.log(clusmySquare(9467, 7649));
console.timeEnd("First Call");

console.time("Second Call");
console.log(clusmySquare(9467, 7649));
console.timeEnd("Second Call");
```

### Question 11. Closure vs Scope

```
Closure : Rhen ever we create a function between another function, the inner function is the closure.
Global Scope
Outer Scope
Local Scope

Scope : Refers to visibility of variables or what variable you have access to.
Global Scope
Local Scope
```

### Question 12. Currying

```
Function that take one argument at a time and return a function expecting the next argument.
```

```
Infinite Currying :

function add(a) {
  return function (b) {
    if (b) return add(a + b);
    return a;
  };
}

console.log(add(5)());
```

### Question 13. Currying vs Partial Application

```
Partial Application:

function sum(a){
  return function(b,c){
    return a + b + c;
  }
}

const x =sum(10);
console.log(x(5,6));
console.log(x(3,2));
```

```
Currying:

function sum(a){
  return function(b){
    return function(c){
      return a + b + c;
    }
  }
}

const x =sum(10);
console.log(x(5)(6));
```

```
Real World use of currying : Manipulating DOM

function updateElementText(id){
  return function(content){
    document.querySelector("#"+id).textContent=content;
  }
}

const updateHeader = updateElementText("heading");
updateHeader("Subscribed");
```

```
Convert f(a,b,c) to f(a)(b)(c) :

function curry(func) {
  return function curriedFunc(...args) {
    if (args.length >= func.length) {
      return func(...args);
    } else {
      return function (...next) {
        return curriedFunc(...args, ...next);
      };
    }
  };
}

const sum = (a, b, c) => a + b + c;

const totalSum = curry(sum);

console.log(totalSum(1)(2)(3));
```

### Question 14. Objects Interview Questions

```
const a ={};
const b ={key:"b"};
const c ={key:"c"};

a[b]=123; // a["[object object]"]=123;
a[c]=456; // a["[object object]"]=456;

console.log(a[b]); // 456
```

```
function abcd(a,b,...args,d){
}

abcd(1,2,3,4); // error - the rest parameter must be in the last
```

### Question 15. Shallow copy vs deep copy

```

```

### Question 16. this

```
Types of Object binding
1. Implicit binding (using dot notation)
2. Explicit binding (using call, apply, binding, etc)
```

```
this inside normal function and arrow function

Normal function : this referes to the object that is executing the current function.

Arrow Function : this refers to the parent function.
```

```
Doubt ?????

function makeUser(){
  return {
    name:"John",
    ref:this,
  }
}
let user = makeUser();
console.log(user.ref.name); // empty string
console.log(typeof user.ref.name); // string
console.log(user.ref.name.length); // 0
```

```
const user={
  name:"abc",
  logMessage(){
    console.log(this.name);
  }
}
setTimeout(user.logMessage,1000); // undefined

const user={
  name:"abc",
  logMessage(){
    console.log(this.name);
  }
}
setTimeout(function(){
  user.logMessage()
},1000); // abc
```

```
const info = {
  firstName: "hello",
  lastName: "world",
  fullName(){
    const details = () => {
        return this.firstName + " " + this.lastName;
    };
   return details();
  },
};

const user = info.fullName();
console.log(user); // hello worlds
```

```
doubt ????

var length = 4;

function callback(){
    console.log(this.length);
}

const object = {
    length:5,
    method(fn){
        fn()
    }
}

console.log(object.method(callback)); // 4
```

```
doubt ????

var length = 4;

function callback(){
    console.log(this.length);
}

const object = {
    length:5,
    method(){
        arguments[0]();
    }
}

object.method(callback,2,3); // 3

Explanation : argument = [callback,2,3]. The length of array(array=object) is 3.
```

```
Implement calc : const result = calc.add(10).multiply(5).substract(30).add(10);
console.log(result.total);

const calc = {
  total: 0,
  add(value) {
    this.total = this.total + value;
    return this;
  },
  multiply(value) {
    this.total = this.total * value;
    return this;
  },
  substract(value) {
    this.total = this.total - value;
    return this;
  },
};

const result = calc.add(10).multiply(5).substract(30).add(10);
console.log(result.total);
```

### Question 17. call(), apply(), bind() polyfills

```
call() :

var obj ={name:"hello world"};
function sayHelloWorld(age){
    return this.name + " " + age
}
console.log(sayHelloWorld.call(obj,100));

apply() :

var obj ={name:"hello world"};
function sayHelloWorld(age){
    return this.name + " " + age
}
console.log(sayHelloWorld.appply(obj,[100]));

bind() :

var obj ={name:"hello world"};
function sayHelloWorld(age){
    return this.name + " " + age
}
let result = sayHelloWorld.bind(obj,100)
console.log(result());
```

```
const array =[1,2,3,4,5];
const elements = [6,7,8];

array.push.apply(array,elements);

console.log(array);
```

```
const numbers=[5,6,2,3,7];

console.log(Math.max.apply(null,numbers))
```

```
function f(){
    console.log(this);
}
let user = {
    g : f.bind(null)
}
user.g(); // window {}
```


```
const age = 10; // doubt ????

var person = {
    name:"Piyush",
    age:20,
    getAgeArrow:()=>console.log(this.age),
    getAge:function(){
        console.log(this.age);
    }
}

var person2 = { age : 24 };

person.getAgeArrow.call(person2); // undefined
person.getAge.call(person2); // 24
```

```
var age = 10; // doubt ????

var person = {
    name:"Piyush",
    age:20,
    getAgeArrow:()=>console.log(this.age),
    getAge:function(){
        console.log(this.age);
    }
}

var person2 = { age : 24 };

person.getAgeArrow.call(person2); // 10
person.getAge.call(person2); // 24
```

```
call polyfill :

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

```
apply() polyfill :

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

```
bind() polyfill :

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
 