// import axios, { AxiosInstance } from 'axios';
// import { promises } from 'dns';

export interface getMenuParams{
    _date:string,
    _when:"breakfast"|"lunch"|"dinner"|"easymeal",
    _where:"student"|"professor"|"dormitory"
}

// export default class API{
//     async getMenu(_date:string, _when:"breakfast"|"lunch"|"dinner"|"easymeal", _where:"student"|"dormitory"|"professor"){
//         const res = await fetch(`/get_menu?date=${_date}&when=${_when}&where=${_where}`);
//         const data = await res.json();
//         return data;
//     }
// }

export default class API{
    async getMenu(_date:string, _when:"breakfast"|"lunch"|"dinner"|"easymeal", _where:"student"|"dormitory"|"professor"){
 
        const res = await fetch(`${process.env.REACT_APP_API_BASE_URL}`, {
            method: "POST",
            mode:"cors",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "statusCode":200,
                "API":"get_menu",
                "date": _date,
                "when": _when,
                "where": _where
              }),
          });
          if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        } else {
            const data = await res.json();
            return data;
        }
    }

    async saveReview(_type:string, _content:string){
        const res = await fetch("/", {
            method: "POST",
            mode:"no-cors",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
                "API":"save_review",
                "type": _type,
                "content": _content
              }),
          });
          if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        } else {
            const data = await res.json();
            return res;
        }
    }
}