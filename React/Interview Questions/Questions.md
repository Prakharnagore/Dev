# Interview Questions

#### 1. What is react component ?

A React component is javascipt function that encapsulates logic and rendering. It returns JSX to describe what should be rendered on the screen

#### 2. What is JSX ?

JSX stands for JavaScript XML. SX is a syntax extension for JavaScript that allows us to write HTML-like code in their JavaScript files. It' not a valid JavaScript. Jsx code must be compiled to JavaScript. The traspile babel is popular tool for this process.

#### 3. Why never define a component inside another component!

### 4. Why do multiple JSX tags need to be wrapped?

JSX is transformed into plain JavaScript objects. You can’t return two objects from a function without wrapping them into an array. This explains why you also can’t return two JSX tags without wrapping them into another tag or a Fragment.

### 5. Why does React need keys?

Keys tell React which array item each component corresponds to, so that it can match them up later. This becomes important if your array items can move (e.g. due to sorting), get inserted, or get deleted. A well-chosen key helps React infer what exactly has happened, and make the correct updates to the DOM tree.

### 06. Why not to use item’s index in the array as its key ?

The reason for this is that using the index as the key can cause issues when the list of items is updated. If an item is added or removed from the list, the indexes of the remaining items may change, causing React to re-render more items than necessary. This can lead to performance issues, particularly in large lists.

### 07. What is event bubbling ?

### 08. What are Hooks ?

Hooks are functions that allow you to use state.

### 09. How does React know which state to return?

## 10. Is setState Async or sync ?

## 11. Build a stop watch

```
import { useState, useRef } from 'react';

export default function Stopwatch() {
  const [startTime, setStartTime] = useState(null);
  const [now, setNow] = useState(null);
  const intervalRef = useRef(null);

  function handleStart() {
    setStartTime(Date.now());
    setNow(Date.now());

    clearInterval(intervalRef.current);
    intervalRef.current = setInterval(() => {
      setNow(Date.now());
    }, 10);
  }

  function handleStop() {
    clearInterval(intervalRef.current);
  }

  let secondsPassed = 0;
  if (startTime != null && now != null) {
    secondsPassed = (now - startTime) / 1000;
  }

  return (
    <>
      <h1>Time passed: {secondsPassed.toFixed(3)}</h1>
      <button onClick={handleStart}>
        Start
      </button>
      <button onClick={handleStop}>
        Stop
      </button>
    </>
  );
}
```

## 12.Suspense VS useTransition

## 13. Explain apply, bind

## 14. What is bundling and code-splitting

Bundling - Bundling is the process of following imported files and merging them into a single file: a “bundle”.

Code Splitting - As your app grow bundle will grow too. Code-Splitting create multiple bundles that can be dynamically loaded at runtime. Code-splitting lazy load things that are currently needed by the user and avoid loading code that the user may never need.

## 15. Error boundaries using class and function components

https://gist.github.com/andywer/800f3f25ce3698e8f8b5f1e79fed5c9c

we dont have any method in functional component that compete with statis getDerivedStateFrom error and componentDidCatch. so we cannot create error boundries with functional component. 

```
class Error extends React.Component {
  constructor(props){
    super(props);
    this.state={
      hasError:false
    };
  }

 static getDerivedStateFromError(error){
     return { hasError: true };
  }

  componentDidCatch(error,errorInfo){
    logErrorToMyService(error,errorInfo);
  }

render(){
 if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
      }
}

```

## 16. What is reconciliation ?

## 17. What is virtual dom ?

The virtual DOM (VDOM) is a programming concept where an ideal, or “virtual”, representation of a UI is kept in memory and synced with the “real” DOM by a library such as ReactDOM. This process is called reconciliation.
