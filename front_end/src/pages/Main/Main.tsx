import { useState } from 'react';
import styled from 'styled-components';
import { PageStyle } from '../../styles/style_modules';
import { cafeteria } from './interface';
import CafeteriaSelector from './components/CafeteriaSelector';

const Main = () => {
    const [selected_cafeteria, setCafeteria] = useState<cafeteria>("student");
    const change_cafeteria = (_where: cafeteria) => {
        setCafeteria(_where);
    }
    return (
        <PageStyle>
            <CafeteriaSelector _change_cafeteria={change_cafeteria} _now_cafeteria={selected_cafeteria} />
        </PageStyle>
    );
};

export default Main;