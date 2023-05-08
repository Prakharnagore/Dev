Function.prototype.myApply = function (context = {}, ...args) {
  if (typeof this !== "function") {
    throw new Error(this + " is not a function");
  }

  context.fn = this;
  return () => context.fn(...args);
};

var obj = { name: "hello world" };

function sayHelloWorld(age) {
  return this.name + " " + age;
}

const data = sayHelloWorld.bind(obj, 100);
console.log(data);
