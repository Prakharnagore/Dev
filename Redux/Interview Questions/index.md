# Question: Why we use middleware such as redux thunk ?

We cannot use action creator because action creators should return a plan oject.

```
function actionCreatorName() {
    // Action
  return { type: increment };
}

```

The above code works but below code do not work because action the below action creator returns promise.

```
async function getUser() {
  const { data } = await axios.get("http://localhost:3000/accounts/1");
  return {type:init, payload:data.amount}
}
```

# Question: Redux thunk vs Redux Toolkit

# Whats the need of extrareducer in createSlice ?

1. Support you want to change the state of another reducer then this extra reducer will give you state and action. With that state you can change the state of other reducer.

```
const incrementByAmount = createAction('reducerName/actionName');

extraReducers:(builder)=>{
builder.addCase(incrementByAmount,(state,action)=>{
state.points+=1; // state of another reducer
})
}

```
2. creating async functions

```
const fetchUser=createAsyncThunk('user/getUser', async (userId,thunkAPI)=>{
  // api call
  const response = await axios.get("/")
  return response.data
});

extraReducers:(builder)=>{
  builder.addCase(fetchUser.pending,(state, action)=>{

  },
   builder.addCase(fetchUser.fulfilled,(state,action)=>{
    
  },
   builder.addCase(fetchUser.rejected,(state,action)=>{
    
  }
}
```