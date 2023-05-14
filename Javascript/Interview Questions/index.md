# JavaScript Interview Quetions

```
console.log(typeof NaN); // number
```

```
const value = 10 - - 10
console.log(value); // 20
```

```
let value = {name:"abc"}
console.log(delete value.name); // true
console.log(value); // {}
```

```
let value = {name:"abc"}
console.log(delete value); // false 
```

```
let data={name:"abc"};
let info={city:"def"};
data={data,...info};
console.log(data); // { data: { name: 'abc' }, city: 'def' }
```

```
console.log(Promise.resolve(5)); // {<fullfilled> : 5}
```

```
console.log(`${(x=>x)('I love')} to program`);
```

```
const data=[1,2,3,4];
delete data[1];
console.log(data); // [1,<empty>,3,4];
```

```
let a=1;
let c=2;
console.log(--c === a); // true
```

```
let a=1;
let b=1;
let c=2;
console.log(a === b === --c); // false
```

```
console.log(3***3); // error
```

```
let for = 100; // error - for is reserved keyword
```

```
console.log(+true); // 1
```

```
let a =3;
let b=new Number(3);

console.log(a==b); // true
console.log(a===b); // false
console.log(typeof b); // 'object'
```

```
let number = 0;
console.log(number++); // 0
console.log(++number); // 2
console.log(number); // 2
```

```
const obj = {1:'a'};
console.log(obj.hasOwnProperty('1')); // true
console.log(obj.hasOwnProperty(1)); //true
```

```
console.log(typeof typeof 1); // string
```

```
const data=[1,2,3,4,5,6,7,8,9];
data[100]=100;
console.log(data.length); // [ 1, 2, 3, 4, 5, 6, 7, 8, 9, <91 empty items>, 100 ];
```

```
console.log(setInterval(()=>console.log("HI),1000)); // 1
console.log(setInterval(()=>console.log("HI),1000)); // 2
console.log(setInterval(()=>console.log("HI),1000)); // 3
```

```
const first = new Promise((res,rej)=>{
    setTimeout(res,500,'one');
});

const second = new Promise((res,rej)=>{
    setTimeout(res,100,'two');
})

Promise.race([firstPromise,secondPromise]).then(res=>console.log(res)); // two
```

```
let person = {name: 'John'};
const numbers = [person];
person = null;
console.log(numbers); // [{name: 'John'}];
```

```
(()=>{
    var x = (y = 10);
})();
console.log(x); // error
console.log(y); // 10 -> y is global variable
```
