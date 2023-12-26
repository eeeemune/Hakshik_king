import styled from "styled-components";
import { menuJsonArr, menuJson } from "../interface";
import Hyperlink from "../../../icons/Hyperlink";
import i18n from "../../../locales/i18n";
import { useTranslation } from "react-i18next";

interface menuModalProp {
    _menuArr: menuJson[] | undefined,
    _setModal: (_elem: any) => void
}


const MenuModal = ({ _menuArr, _setModal }: menuModalProp) => {
    const { t } = useTranslation();
    const MODAL_ELEMENT = _menuArr!.map((menu: menuJson) => <ModalElement>
        <Title>{i18n.language === "ko" ? menu.name : menu.name_eng}{menu.fork && "🐷"}{menu.beef && "🐮"}{menu.egg && "🥚"}{menu.chicken && "🐔"}{menu.seafood && "🦐"}</Title>
        <Discription>{i18n.language === "ko" ? menu.dscrpt : menu.dscrpt_eng}</Discription>
        <RecipeGo href={menu.url || undefined}>{i18n.language === "ko" ? "레시피 바로가기" : "Go to recipes"}<Hyperlink /></RecipeGo>
    </ModalElement>);
    return (
        <ModalWrapper>
            <TitleElementPack>
                <Category>{t(`main.${_menuArr![0].category}`)}</Category>
                <div>
                    {MODAL_ELEMENT}
                </div>

            </TitleElementPack>
            <CloseModal onClick={() => { _setModal(<div></div>) }}>{i18n.language === "ko" ? "확인" : "Okay"}</CloseModal>
        </ModalWrapper>

    )
}

const ModalWrapper = styled.div`
width: 100vw;
height: 100vh;
background-color: #000000d5;
position: fixed;
top: 0;
left: 0;
display: flex;
align-items: center;
justify-content: center;
flex-direction: column;
row-gap: 1rem;
`

const TitleElementPack = styled.div`
background-color: white;
max-height: 25rem;
overflow-y: scroll;
width: 20rem;
padding: 1.5rem 1rem 1.5rem 1rem;
border-radius: 1rem;
flex-direction: column;
box-sizing: border-box;
`


const Title = styled.div`
    ${({ theme }) => theme.TEXT.default_bold};
`

const Category = styled.div`
    ${({ theme }) => theme.TEXT.large_bold};
`

const Discription = styled.div`
        ${({ theme }) => theme.TEXT.default};
`

const ModalElement = styled.div`
    display: flex;
    flex-direction: column;
    row-gap: 0.5rem;
    border-bottom: 1px solid ${({ theme }) => theme.COLOR.line_gray};
    padding: 1rem 0 1rem 0;
`
const RecipeGo = styled.a`
    color: #1563FC;
    display: flex;
    align-items: center;
    column-gap: 0.2rem;
`

const CloseModal = styled.button`
    background-color: ${({ theme }) => theme.COLOR.orange};
    width: 20rem;
    height: 3rem;
    ${({ theme }) => theme.TEXT.default_bold};
    color: white;
    border-radius: 1rem;
`

export default MenuModal;