const _makeup_date = (_y: number, _m: number, _d: number, _w: number, _lan:string) => {
    let week_list;
    _lan === "ko"?  week_list = ["일", "월", "화", "수", "목", "금", "토"]:  week_list = ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"];
    const month = (_m < 10 ? '0' : '') + _m;
    const day = (_d < 10 ? '0' : '') + _d;
    return `${_y}-${month}-${day}`;
}

const date = new Date();
// export const TODAY = _makeup_date(date.getFullYear(), date.getMonth()+1, date.getDate(), date.getDay());

export const today = (_lan:string) =>_makeup_date(date.getFullYear(), date.getMonth()+1, date.getDate(), date.getDay(), _lan);

export const tomorrow = (_today: string, _lan:string) => {
    const day_str = _today.split(" (")[0];
    const today = new Date(day_str);
    const tomorrow = new Date(today);
    tomorrow.setDate(today.getDate()+1);
    return _makeup_date(tomorrow.getFullYear(), tomorrow.getMonth()+1, tomorrow.getDate(), tomorrow.getDay(), _lan);
}

export const yesterday = (_today: string, _lan:string) => {
    const day_str = _today.split(" (")[0];
    const today = new Date(day_str);
    const yesterday = new Date(today);
    yesterday.setDate(today.getDate()-1);
    return _makeup_date(yesterday.getFullYear(), yesterday.getMonth()+1, yesterday.getDate(), yesterday.getDay(), _lan);
}