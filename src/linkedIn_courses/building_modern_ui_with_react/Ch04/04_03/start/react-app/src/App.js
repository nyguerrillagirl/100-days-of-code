import "./App.css";

const [firstCity, second] = ["Toronto", "New York", "Los Angeles", "Chicago", "Houston"];
console.log(second);

function App({library}) {
  return (
    <div className="App">
      <h1>Hello from {library}</h1>
    </div>
  );
}

export default App;
