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

### Question 3. Map, Filter and Reduce

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
