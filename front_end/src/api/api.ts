// import axios, { AxiosInstance } from 'axios';
// import { promises } from 'dns';

export interface getMenuParams{
    _date:string,
    _when:"breakfast"|"lunch"|"dinner"|"easymeal",
    _where:"student"|"professor"|"dormitory"
}

export default class API{
    async getMenu(_date:string, _when:"breakfast"|"lunch"|"dinner"|"easymeal", _where:"student"|"dormitory"|"professor"){
        const res = await fetch(`/get_menu?date=${_date}&when=${_when}&where=${_where}`);
        const data = await res.json();
        return data;
    }
}