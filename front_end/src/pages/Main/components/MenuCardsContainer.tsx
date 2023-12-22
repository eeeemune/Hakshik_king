import { useEffect, useState } from "react";
import API from "../../../api/api"
import MenuCard from "./MenuCard";
import styled from "styled-components";
import { menuJson, menuJsonArr, menuCardProps } from "../interface"
import MenuModal from "./MenuModal";



const MenuCardsContainer = ({ _date, _when, _where }: menuCardProps) => {
    const api = new API();
    const [menuArr, setMenuArr] = useState<menuJsonArr>();
    const [isLoading, setIsLoading] = useState(true);
    const [modal, setModal] = useState(<div></div>);

    useEffect(() => {
        setIsLoading(true);
        api.getMenu(_date, _when, _where)
            .then((data) => {
                setMenuArr(data);
            })
            .then(() => {
                setIsLoading(false);
            });

    }, [_date, _where, _when]);


    const categories = menuArr
        ? [...new Set(menuArr.map((json: menuJson) => json.category))]
        : [];

    let cards = [];

    const when_to_show = (_when: "breakfast" | "lunch" | "easymeal" | "dinner"): "조식" | "중식" | "석식" | "간편식" | "식사" => {
        if (_when == "breakfast")
            return "조식"
        else if (_when == "lunch")
            return "중식"
        else if (_when == "dinner")
            return "석식"
        else if (_when == "easymeal")
            return "간편식"
        else
            return "식사"
    }

    const show_detail = (_category?: string): void => {
        if (_category == "NULL") setModal(<div></div>);
        else setModal(<MenuModal _setModal={setModal} _menuArr={menuArr?.filter((menu: menuJson) => menu.category == _category)}></MenuModal>);
    }

    for (let i = 0; i < categories.length; i++) {
        let category_menu = menuArr?.filter((target: menuJson) => target.category === categories[i]);
        let menu_name_arr = category_menu?.map((target: menuJson) => {
            let name = target.name;
            if (target.beef) name += '🐮';
            if (target.fork) name += '🐷';
            if (target.egg) name += '🥚';
            if (target.chicken) name += '🐔';
            if (target.seafood) name += '🦐';
            return name;
        }
        );
        cards.push(<MenuCard _category={categories[i]} _menuNameArr={menu_name_arr!} _show_detail={show_detail} />);
    }

    if (cards.length == 0) {
        cards.push(<MenuNoneCard>학식이 제공되지 않는 날이에요.</MenuNoneCard>)
    }

    if (isLoading) {
        return <MenuNoneCard>데이터를 불러오는 중...</MenuNoneCard>;
    }
    else {
        return (<MealWrapper>
            {modal
            }
            <MealTitle>{when_to_show(_when)}</MealTitle>
            {cards}
        </MealWrapper>);
    }
}

const MealWrapper = styled.div`
    display: flex;
    flex-direction: column;
    row-gap: 1rem;
`

const MealTitle = styled.div`
    ${({ theme }) => theme.TEXT.large_bold};
`

const MenuNoneCard = styled.div`
    ${({ theme }) => `${theme.TEXT.default} color:${theme.COLOR.disabled}`};
    padding: 1rem;
    border-radius: 1rem;
    background: #FFF;
    box-shadow: 0px 4px 16px 0px #E0E1E3;
`

const ModalStyle = styled.div`
    
`

export default MenuCardsContainer;