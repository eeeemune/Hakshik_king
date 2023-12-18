import { DefaultTheme } from 'styled-components';

type color_config = {
    orange: string,
    black: string,
    line_gray: string,
    disabled: string,
    background: string
}

type text_config = {
    default: string,
    default_bold: string, 
    large_bold: string
}

type style_variables_config = {
    PAGE_PADDING: string,
    TOP_NAV_HEIGHT:string,
}

const STYLE_VARIABLES:style_variables_config = {
    PAGE_PADDING: "1.5rem",
    TOP_NAV_HEIGHT:"3rem"
}

const COLOR: color_config = {
    orange: "#FF5C38",
    black: "#342D2C",
    line_gray: "#ECF0F2",
    disabled: "#DEDEDE",
    background: "#F5F6F8"
}

const TEXT: text_config = {
    default: `
    font-family: 'Pretendard';
    font-size: 1rem;
    font-weight: 400;
    line-height: 151.336%;
`,
    default_bold: `
            font-family: 'Pretendard';
            font-size: 1rem;
            font-weight: 700;
            line-height: 151.336%;
    `,
    large_bold:`
    font-family: 'Pretendard';
    font-size: 1.5rem;
    font-weight: 700;
    `
}


const theme: DefaultTheme = {
    COLOR, TEXT, STYLE_VARIABLES
}

export default theme;