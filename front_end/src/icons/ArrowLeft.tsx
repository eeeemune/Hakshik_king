import { DefaultTheme, useTheme } from "styled-components"

interface arrow_left_prop {
    _width?: string,
    _height?: string,
    _color?: string
}

const ArrowLeft = ({ _width, _height, _color }: arrow_left_prop) => {
    const theme = useTheme();
    return (
        <svg width={_width} height={_height} viewBox="0 0 8 13" fill="none" xmlns="http://www.w3.org/2000/svg" >
            <path d="M6.65685 0.843146L1 6.5L6.65685 12.1569" stroke={_color || theme.COLOR.black} stroke-linecap="round" stroke-linejoin="round" />
        </svg >

    )
}

ArrowLeft.defaultProps = {
    _width: "1rem",
    _height: "1rem",
}

export default ArrowLeft;

