import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/department');
        const json = await response.json();

        setData(json);
        return json;
      } catch (error) {
        console.log(error);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {data?.map((item, idx) => (
          <div key={idx}>{item?.DepartmentName}</div>
        ))}
      </header>
    </div>
  );
}

export default App;
