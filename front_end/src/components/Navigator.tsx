import styled from "styled-components";
import LOGO_CI from "../icons/LOGO_CI";
import i18n from "../locales/i18n";
import { useTranslation } from "react-i18next";

const Navigator = () => {
    const change_language = (_target_lang: "ko" | "en") => {
        i18n.changeLanguage(_target_lang);
    }
    const { t } = useTranslation();

    return (<StyleNavigator><LOGO_CI _height={"1.5rem"} />
        <StyledTranslator onClick={() => { change_language(i18n.language === 'en' ? 'ko' : 'en') }}>{t(`nav.lng`)}</StyledTranslator></StyleNavigator>)
}

const StyleNavigator = styled.div`
    background-color: ${({ theme }) => theme.COLOR.orange};
    height: ${({ theme }) => theme.STYLE_VARIABLES.TOP_NAV_HEIGHT};
    width: 100%;
    padding: 0 ${({ theme }) => theme.STYLE_VARIABLES.PAGE_PADDING} 0 ${({ theme }) => theme.STYLE_VARIABLES.PAGE_PADDING};
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: fixed;
`
const StyledTranslator = styled.button`
    color: white;
    border: 1px solid white;
    padding: 0.25rem 1rem;
    border-radius: 100rem;
`

export default Navigator;