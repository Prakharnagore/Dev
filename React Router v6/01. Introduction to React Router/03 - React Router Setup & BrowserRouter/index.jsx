import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Router, Route } from "react-router-dom";

function App() {
  return <h1>Hello world!</h1>;
}

const rootElement = document.getElementById("root");
const root = ReactDOM.createRoot(rootElement);
root.render(
  // browser router act as a context provider
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
