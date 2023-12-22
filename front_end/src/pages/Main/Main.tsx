import { useState, useEffect } from 'react';
import styled from 'styled-components';
import { PageStyle } from '../../styles/style_modules';
import { cafeteria } from './interface';
import CafeteriaSelector from './components/CafeteriaSelector';
import DaySelector from './components/DaySelector';
import { TODAY } from './components/getToday';
import MenuCardsContainer from './components/MenuCardsContainer';

const Main = () => {
    const [selected_cafeteria, setCafeteria] = useState<cafeteria>("student");
    const change_cafeteria = (_where: cafeteria) => {
        setCafeteria(_where);
    }
    const [selected_day, setToday] = useState<string>(TODAY);
    const changeDay = (_d: string) => {
        setToday(_d);
    }

    const [menu_to_show, setMenuToShow] = useState<JSX.Element[]>([]);

    const when_arr = (_where: "student" | "professor" | "dormitory"): ("breakfast" | "lunch" | "dinner" | "easymeal")[] => {
        if (_where == 'student' || _where == 'professor') return ["breakfast", "lunch", "dinner"];
        else return ["breakfast", "lunch", "dinner", "easymeal"]
    }

    // const menu_to_show = when_arr(selected_cafeteria).map((when) => <MenuCardsContainer _date={"2023-12-04"} _when={when} _where={selected_cafeteria} />);
    useEffect(() => {
        setMenuToShow(when_arr(selected_cafeteria).map((when) => <MenuCardsContainer _date={selected_day.split(' (')[0]} _when={when} _where={selected_cafeteria} />));
    }, [selected_cafeteria, selected_day]);

    return (
        <PageStyle>
            <ColGap>
                <CafeteriaSelector _change_cafeteria={change_cafeteria} _now_cafeteria={selected_cafeteria} />
                <DaySelector _today={selected_day} _changeDay={changeDay} />
                {/* <MenuCardsContainer _date={today.split(' (')[0]} _when='lunch' _where='dormitory' /> */}
                {menu_to_show}

            </ColGap>


        </PageStyle>
    );
};

export default Main;

const ColGap = styled.div`
    display: flex;
    row-gap: 0.5rem;
    flex-direction: column;
`
