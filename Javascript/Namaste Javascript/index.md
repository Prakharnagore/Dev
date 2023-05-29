# Execution Context

1. Memory Component (Variable Environment) - Javascript allocate memory to all the variable and function. And are stored in form of key value pairs.
2. Code Component (Thread of Execution) - Code is executed one line at a time.

return keyword tells the function to return the whole control back to execution context where the function was envoked.

# undefined vs no defined

1. undefined - taking memory
2. notdefined - not taking memory

# Erros in code execution

1. UnCaught SyntaxError - Missing Initializer in const declaration. / Identifier has been already declared
2. TypeError - Assignment to constant variable
3. Uncaught ReferenceError - cannot access a before initialization / not defined

# Scope

var -
let & const - Block Scoped. let and const variables are stored in separate memory space which is reserved for block.
