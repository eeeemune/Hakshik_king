import styled from "styled-components";
import { DefaultTheme } from 'styled-components';
import { cafeteria } from "../interface";
import i18n from "../../../locales/i18n";
import { useTransition } from "react";
import { useTranslation } from "react-i18next";

interface CafeteriaSelectorProps {
    _change_cafeteria: (_where: cafeteria) => void;
    _now_cafeteria: cafeteria;
}

interface CafeteriaProps {
    _selected: boolean;
}

const CafeteriaSelector = ({ _change_cafeteria, _now_cafeteria }: CafeteriaSelectorProps) => {
    const { t } = useTranslation();
    return (
        <CafeteriaWrapper>
            <CafeteriaStyled onClick={() => _change_cafeteria("dormitory")} _selected={_now_cafeteria === "dormitory"}>{t(`main.cafeteria3`)}</CafeteriaStyled>
            <CafeteriaStyled onClick={() => _change_cafeteria("student")} _selected={_now_cafeteria === "student"}>{t(`main.cafeteria1`)}</CafeteriaStyled>
            <CafeteriaStyled onClick={() => _change_cafeteria("professor")} _selected={_now_cafeteria === "professor"}>{t(`main.cafeteria2`)}</CafeteriaStyled>

        </CafeteriaWrapper>
    );
};

const CafeteriaWrapper = styled.div`
background-color: ${({ theme }) => theme.COLOR.background};
  width: 100vw;
  height: 2.5rem;
  position: fixed;
  top: ${({ theme }) => theme.STYLE_VARIABLES.TOP_NAV_HEIGHT};
  left: 0;
  display: flex;
  padding: 0 ${({ theme }) => theme.STYLE_VARIABLES.PAGE_PADDING} 0 ${({ theme }) => theme.STYLE_VARIABLES.PAGE_PADDING};
  border-bottom: 1px solid ${({ theme }) => theme.COLOR.line_gray};
  column-gap: 1rem;
`;


const CafeteriaStyled = styled.div<CafeteriaProps>`
${({ theme }) => theme.TEXT.default_bold};
${({ theme }) => theme.COLOR.black};

display: flex;
align-items: center;
height: 100%;
line-height: 100%;
${(props) => props._selected ? `border-bottom: 2px solid ${props.theme.COLOR.black}` : `color:#C9C9C9`};
cursor: pointer;
`;

export default CafeteriaSelector;
