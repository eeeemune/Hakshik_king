import { useState } from 'react';
import styled from 'styled-components';
import { PageStyle } from '../../styles/style_modules';
import { cafeteria } from './interface';
import CafeteriaSelector from './components/CafeteriaSelector';
import DaySelector from './components/DaySelector';
import {TODAY} from './components/getToday';

const Main = () => {
    const [selected_cafeteria, setCafeteria] = useState<cafeteria>("student");
    const change_cafeteria = (_where: cafeteria) => {
        setCafeteria(_where);
    }
    const [today, setToday] = useState<string>(TODAY);
    const changeDay = (_d:string) =>{
        setToday(_d);
    }
    return (
        <PageStyle>
            <CafeteriaSelector _change_cafeteria={change_cafeteria} _now_cafeteria={selected_cafeteria} />
            <DaySelector _today={today} _changeDay={changeDay}/>
        </PageStyle>
    );
};

export default Main;