import styled from 'styled-components';


export const PageStyle = styled.div`
    width: calc(100vw - ${({theme})=>theme.STYLE_VARIABLES.PAGE_PADDING});
    margin: auto;
    padding: 1rem 0rem 3rem 0rem;

`
