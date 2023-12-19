const _makeup_date = (_y: number, _m: number, _d: number, _w: number) => {
    const week_list = ["일", "월", "화", "수", "목", "금", "토"];
    return `${_y}-${_m}-${_d} (${week_list[_w]})`;
}

const date = new Date();
export const TODAY = _makeup_date(date.getFullYear(), date.getMonth(), date.getDate(), date.getDay());

export const tomorrow = (_today: string) => {
    const day_str = _today.split(" (")[0];
    const today = new Date(day_str);
    const tomorrow = new Date(today);
    tomorrow.setDate(today.getDate()+1);
    return _makeup_date(tomorrow.getFullYear(), tomorrow.getMonth(), tomorrow.getDate(), tomorrow.getDay());
}

export const yesterday = (_today: string) => {
    const day_str = _today.split(" (")[0];
    const today = new Date(day_str);
    const yesterday = new Date(today);
    yesterday.setDate(today.getDate()-1);
    return _makeup_date(yesterday.getFullYear(), yesterday.getMonth(), yesterday.getDate(), yesterday.getDay());
}