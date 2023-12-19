import styled from "styled-components";
import { TODAY, tomorrow, yesterday } from './getToday';

interface daySelectorProp {
    _today: string;
    _changeDay: (_day: string) => void;
}

const DaySelector = ({ _today, _changeDay }: daySelectorProp) => {
    return (<DayWrapper>
        <Yesterday />
        <Today>
            {_today}
        </Today>
        <Tomorrow />
    </DayWrapper>)

}

const Today = styled.div`
    
`

export default DaySelector;