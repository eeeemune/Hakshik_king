import styled, { useTheme } from "styled-components";
import { today, tomorrow, yesterday } from './getToday';
import ArrowRight from '../../../icons/ArrowRight';
import ArrowLeft from '../../../icons/ArrowLeft';
import i18n from "../../../locales/i18n";

interface daySelectorProp {
    _today: string;
    _changeDay: (_day: string) => void;
}

const DaySelector = ({ _today, _changeDay }: daySelectorProp) => {
    const theme = useTheme();
    return (<DayWrapper>
        <ElementPack>
            <Yesterday onClick={_today.split(' (')[0] == "2023-12-04" ? () => { } : () => { _changeDay(yesterday(_today = _today, i18n.language)) }}><ArrowLeft _color={_today.split(' (')[0] == "2023-12-04" ? theme.COLOR.disabled : theme.COLOR.black} /></Yesterday>
            <Today>
                {_today}
            </Today>
            <Tomorrow onClick={_today == today(i18n.language) ? () => { } : () => { _changeDay(tomorrow(_today, i18n.language)) }}><ArrowRight _color={_today == today(i18n.language) ? theme.COLOR.disabled : theme.COLOR.black} /></Tomorrow>
        </ElementPack>
    </DayWrapper>)
}

const Today = styled.div`
    ${({ theme }) => theme.TEXT.default};
`

const DayWrapper = styled.div`
    display: flex;
    justify-content: center;
`

const ElementPack = styled.div`
        margin: auto;
    margin-top: 6rem;
    background-color: ${({ theme }) => theme.COLOR.background_gray};
    display: inline-flex;
    align-items: center;
    column-gap: 0.5rem;
    padding: 0.25rem 1rem;
    border-radius: 100rem;
`

const Yesterday = styled.div`
        cursor: pointer;
    display: flex;
    align-items: center;
`

const Tomorrow = styled.span`
    cursor: pointer;
    display: flex;
    align-items: center;
`



export default DaySelector;