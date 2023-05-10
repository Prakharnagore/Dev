# What is Redux ?

- A Pattern
- A Library
- Independent of Frameworks
- State management for js

# Why Redux ?

To make transer of state variable easy (global store). Neglect prop drilling.


# when to use Redux ?

- Big Application
- High frequency of state changes

# Redux Pattern

Action(type,payload) > dispatch > Reducer (new state) > state > store

# Middlewares

```
dispatch > middleware > reducer
```
Redux middleware extends the store's abilities and lets you write asynchronous logic that can interact with the store. 
Redux middleware provides a third-party extension point between dispatching an action, and the moment it reaches the reducer
