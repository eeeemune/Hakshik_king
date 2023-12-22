import styled, { useTheme } from "styled-components";
import ArrowRight from "../../../icons/ArrowRight";

interface menuCardProp {
    _category: string
    _menuNameArr: string[],
    _show_detail: (_category: string) => void
}

const MenuCard = ({ _category, _menuNameArr, _show_detail }: menuCardProp) => {
    const theme = useTheme();
    return (
        <CardWrapper onClick={() => _show_detail(_category)}>
            <Category>{_category}<ArrowRight _width="0.5rem" _height="0.5rem" _weight="3" _color={theme.COLOR.black} /></Category>
            <MenuList>{_menuNameArr.join(", ")}</MenuList>
        </CardWrapper>
    )
}


const CardWrapper = styled.div`
    background-color: white;
    box-shadow: 0px 4px 16px 0px #E0E1E3;
    cursor: pointer;
    border-radius: 1rem;
    padding: 1rem;
`

const Category = styled.div`
    ${({ theme }) => theme.TEXT.default_bold};
    display: flex;
    column-gap: 0.5rem;
    align-items: center;
`

const MenuList = styled.div`
    ${({ theme }) => theme.TEXT.default};
    margin-top: 0.5rem;
`



export default MenuCard;