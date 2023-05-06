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
