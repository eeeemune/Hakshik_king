import { DefaultTheme, useTheme } from "styled-components"

interface arrow_right_prop {
    _width?: string,
    _height?: string,
    _color?: string
    _weight?: string
}

const ArrowRight = ({ _width, _height, _color, _weight }: arrow_right_prop) => {
    const theme = useTheme();
    return (
        <svg width={_width} height={_height} viewBox="0 0 8 13" fill="none" xmlns="http://www.w3.org/2000/svg" >
            <path d="M0.97056 0.843146L6.62741 6.5L0.97056 12.1569" stroke={_color || theme.COLOR.black} stroke-width={_weight} stroke-linecap="round" stroke-linejoin="round" />
        </svg >

    )
}


ArrowRight.defaultProps = {
    _width: "1rem",
    _height: "1rem",
    _weight: "1"
}

export default ArrowRight;