import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`

@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.min.css");
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
*{
    font-family: 'Pretendard';
margin: 0;
padding: 0;
font-family: -apple-system,"Noto Sans KR", "Segoe UI", "Malgun Gothic", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif;
font-display: swap;

}
button{
    background: none;
    outline: none;
    border: none;
    cursor: pointer;
}
html{
    font-size: 16px;
}
body{
    background-color: ${({ theme }) => theme.COLOR.background};
}
*::-webkit-scrollbar {
    width: 0.5rem;
  }
  *::-webkit-scrollbar-thumb {
    background-color: #b6b3b0;
    border-radius:1rem;
  }
  *::-webkit-scrollbar-track {
    background-color: none;
  }
a{
    text-decoration: none;
}
`

export default GlobalStyle;