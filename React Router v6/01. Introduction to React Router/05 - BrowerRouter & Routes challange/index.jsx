import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Router } from "react-router-dom";

function App() {
  return <h1>Hello world!</h1>;
}

const rootElement = document.getElementById("root");
const root = ReactDOM.createRoot(rootElement);
root.render(
  <BrowserRouter>
    <Router>
      <App />
    </Router>
  </BrowserRouter>
);
