

interface hyperlinkProp {
    _width?: string,
    _height?: string,
    _color?: string
}

const Hyperlink = ({ _width, _height, _color }: hyperlinkProp) => {
    return (
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="17" viewBox="0 0 16 17" fill="none">
            <g clip-path="url(#clip0_58_880)">
                <path d="M12.6667 13.1667H3.33333V3.83333H8V2.5H3.33333C2.59667 2.5 2 3.09667 2 3.83333V13.1667C2 13.9033 2.59667 14.5 3.33333 14.5H12.6667C13.4033 14.5 14 13.9033 14 13.1667V8.5H12.6667V13.1667ZM9.33333 2.5V3.83333H11.7233L5.17 10.3867L6.11333 11.33L12.6667 4.77667V7.16667H14V2.5H9.33333Z" fill="#1563FC" />
            </g>
            <defs>
                <clipPath id="clip0_58_880">
                    <rect width="16" height="16" fill="white" transform="translate(0 0.5)" />
                </clipPath>
            </defs>
        </svg>

    )
}


Hyperlink.defaultProps = {
    _width: "1rem",
    _height: "1rem",
    _color: "#1563FC"
}

export default Hyperlink;