import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { TweetComponent } from './tweets'

const appEl = document.getElementById('twitter_clone')
if (appEl) {
  ReactDOM.render(
    <React.StrictMode>
      <TweetComponent />,
     </React.StrictMode>,
    appEl
  );
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
