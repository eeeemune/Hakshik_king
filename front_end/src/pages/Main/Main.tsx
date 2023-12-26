import { useState, useEffect, useTransition } from 'react';
import styled from 'styled-components';
import { PageStyle } from '../../styles/style_modules';
import { cafeteria } from './interface';
import CafeteriaSelector from './components/CafeteriaSelector';
import DaySelector from './components/DaySelector';
import { today } from './components/getToday';
import MenuCardsContainer from './components/MenuCardsContainer';
import i18n from "../../locales/i18n";
import Review from './components/Review';

const Main = () => {
    const change_language = (_target_lang: "ko" | "en") => {
        i18n.changeLanguage(_target_lang);
    }

    const [selected_cafeteria, setCafeteria] = useState<cafeteria>("dormitory");
    const change_cafeteria = (_where: cafeteria) => {
        setCafeteria(_where);
    }
    const [selected_day, setToday] = useState<string>(today(i18n.language));
    const changeDay = (_d: string) => {
        setToday(_d);
    }



    const [menu_to_show, setMenuToShow] = useState<JSX.Element[]>([]);

    const when_arr = (_where: "student" | "professor" | "dormitory"): ("breakfast" | "lunch" | "dinner" | "easymeal")[] => {
        if (_where == 'student' || _where == 'professor') return ["breakfast", "lunch", "dinner"];
        else return ["breakfast", "lunch", "dinner", "easymeal"]
    }

    useEffect(() => {
        setMenuToShow(when_arr(selected_cafeteria).map((when) => <MenuCardsContainer _date={selected_day.split(' (')[0]} _when={when} _where={selected_cafeteria} />));
    }, [selected_cafeteria, selected_day]);

    return (
        <PageStyle>
            <ColGap>
                <CafeteriaSelector _change_cafeteria={change_cafeteria} _now_cafeteria={selected_cafeteria} />
                <DaySelector _today={selected_day} _changeDay={changeDay} />
                {menu_to_show}
            </ColGap>
            <Review></Review>


        </PageStyle>
    );
};

export default Main;

const ColGap = styled.div`
    display: flex;
    row-gap: 0.5rem;
    flex-direction: column;
`
