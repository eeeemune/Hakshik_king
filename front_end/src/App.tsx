import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import GlobalStyle from './styles/GlobalStyle';
import { ThemeProvider } from 'styled-components';
import theme from './styles/theme';
import Navigator from './components/Navigator';

const Main = React.lazy(()=>import('./pages/Main/Main'));

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
      <GlobalStyle/>
      <Navigator/>
      <Router>
        <Routes>
          <Route path='/' element={<Main/>}></Route>
        </Routes>
      </Router>
      </ThemeProvider>
      
    </div>
  );
}

export default App;
