import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`

@font-face {
    font-family: 'Pretendard';
    src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard.woff') format('woff');
    font-style: normal;
}
*{
    font-family: 'Pretendard';
font-weight: 400;
margin: 0;
padding: 0;
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
body::-webkit-scrollbar {
    width: 8px;
    background: #217af4;
    border-radius: 10px;
}
a{
    text-decoration: none;
}
`

export default GlobalStyle;