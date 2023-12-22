export type cafeteria = "student"|"professor"|"dormitory";

export interface menuCardProps {
    _date: string,
    _when: "breakfast" | "lunch" | "easymeal" | "dinner",
    _where: "student" | "professor" | "dormitory"
}

export interface menuJson {
    category: string,
    beef: boolean | null,
    fork: boolean | null,
    chicken: boolean | null,
    date: string,
    dscrpt: string,
    dscrpt_eng: string,
    egg: boolean | null,
    // location: "gi" | "gyo" | "hak",
    location: any,
    name: string,
    name_eng: string,
    recipe: null | string[],
    seafood: boolean | null,
    url: string | null
}

export type menuJsonArr = menuJson[];