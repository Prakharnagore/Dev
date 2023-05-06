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
