
import bs4
import datetime
import json
import tabula
import pandas as pd
import re
from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import boto3
from boto3.dynamodb.conditions import Key, Attr
import deepl


url = {
    'student': 'https://www.inha.ac.kr/kr/1072/subview.do',
    'professor': 'https://www.inha.ac.kr/kr/1073/subview.do'
}


class Shik_thisweek:
    data = {}
    where = ""

    def __init__(self) -> None:
        self.update_me()

    def update_me(self):
        pass

    def save_my_data(self):
        # with open(f'./meal_data/{self.where}.json', 'w', encoding='UTF-8') as f:
        #     json.dump(self.data, f, ensure_ascii=False)
        print("don't save")

    def set_shik(self, data):
        self.data = data

    def get_shik(self, when="all"):
        if (when == "all"):
            return self.data
        else:
            return self.data[when]

    def get_html_doc(self, where):
        target_url = url[where]
        res_html = requests.request(url=target_url, method='GET').content

        return res_html

    def get_hakshik_json_of_this_week(self):
        # returns weekly hakshik menu as a json file
        html_doc = self.get_html_doc(self.where)
        this_week_json_dict = {"Monday": {"breakfast": [], "lunch": [], "dinner": []}, "Tuesday": {"breakfast": [], "lunch": [], "dinner": []}, "Wednesday": {"breakfast": [], "lunch": [], "dinner": []},
                               "Thursday": {"breakfast": [], "lunch": [], "dinner": []}, "Friday": {"breakfast": [], "lunch": [], "dinner": []}, "Saturday": {"breakfast": [], "lunch": [], "dinner": []}, "Sunday": {"breakfast": [], "lunch": [], "dinner": []}}
        for today in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            today_json = self.parse_meal_json_today(html_doc, weekday=today)
            this_week_json_dict[today] = today_json

        return this_week_json_dict


class Gishik_thisweek(Shik_thisweek):
    where = "inha_dimitory_banghak"

    def __init__(self):
        super().__init__()

    def update_me(self):
        # Update "data" of slef as hakshik(meal) of this week.

        # Get data of this week dimitory hakshik as a json.
        self.data = self.get_gishik_json_of_this_week(where=self.where)

        # Save data in "meal/inha_dimitory.json".
        # self.save_my_data()

    def get_gishik_json_of_this_week(self, where):
        # Download hakshik pdf and parse to json
        # (input) where: where wanna know hakshik. "inha" or "inha_banghak"
        # (output) json data of week hakshik(Monday:..., Tuesday:...)

        pdf_path = self.get_gishik_pdf()
        # pdf_path = './gogo.pdf'
        this_week_json = self.parse_this_week_json(
            pdf_path, _for_where=where)
        return this_week_json

    def get_gishik_pdf(self):
        # Downloads hakshik pdf and save in local.

        def download_pdf(url, path):
            response = requests.get(url)
            with open(path, 'wb') as file:
                file.write(response.content)

        html = self.get_html_doc('dormitory')
        soup = bs4.BeautifulSoup(html, "html.parser", from_encoding='utf-8')
        this_week_page = soup.find('a', class_='artclLinkView')
        query = this_week_page['href']
        url = f'https://dorm.inha.ac.kr/{query}'

        pdfpage_html = requests.request(url=url, method='GET').content
        soup = bs4.BeautifulSoup(pdfpage_html,  "html.parser",
                                 from_encoding='utf-8')
        pdf_url = soup.select_one(
            "body > div > div.artclItem.viewForm > dl > dd > ul > li:nth-child(1) > a")['href']
        url = f'https://dorm.inha.ac.kr/{pdf_url}'

        path_to_save_pdf = f'./gishiks/{
            datetime.date.today().strftime("gishik_%Y-%m-%S")}.pdf'
        download_pdf(url, path_to_save_pdf)

        return path_to_save_pdf

    def parse_this_week_json(self, pdf_path, _for_where="inha"):
        # parse pdf as a json format.
        # (input) pdf_path: local path of where pdf file is, _for_where: parse pdf for where. it defines how to parse the pdf. default value is "inha."
        # (output) (output) json data of week hakshik(Monday:..., Tuesday:...)

        def parse_arr_from_df_col(df_col):
            # convert column of dataframe to array.
            # (input) df_col: column of pandas data frame
            # (output) array of rows parsed from df_col exept "none"
            data_list = df_col.tolist()
            filtered_list = [str(word) for word in data_list if type(
                word) != type(0.0) or type(word) != type("0")]
            return filtered_list

        def makeup_string_for_inha_gishik(target_str, seperator):
            # make up target_str to be pretty before gotta be a array.
            # replace to 'seperator' if the character is separate of array
            # repace S to "소스" and D to "드레싱" except "DAY"
            # repace 일품식 and 한식 to "CATEGORY일품식, CATEGORY한식", and the CATEGORY will be seperator of category
            # remove "nan", "요청"(sticker), "NEW"(sticker), number more than 3 digits(caloires), "self 라면", "라면/쌀밥/김치", "<메인 선택>", "<특식>", "<뚝}>", "미운영"(for vacation of inha)

            target_str = target_str.replace('\r', seperator)

            target_str = target_str.replace('\n', seperator)
            target_str = target_str.replace('nan', "")
            target_str = target_str.replace('일품식', f"CATEGORY일품식")
            target_str = target_str.replace('요청', "")
            target_str = target_str.replace('NEW', "")
            target_str = target_str.replace("r'(?<=\D)(?=\d{3}\b)'", "")
            target_str = target_str.replace("self 라면", "")
            target_str = target_str.replace("라면/ 쌀밥/ 김치", "")
            target_str = target_str.replace("한  식", f"CATEGORY한식")
            target_str = target_str.replace("<메인 선택>", "")
            target_str = target_str.replace("< 특식>", "")
            target_str = target_str.replace("뚝)", "")
            target_str = target_str.replace("S", " 소스")
            target_str = target_str.replace("D", " 드레싱")
            target_str = target_str.replace(" 드레싱AY", "DAY")
            target_str = target_str.replace("미 운 영", "")
            return target_str

        def package_meal(_target_string, _seperator, _is_easymeal):
            # get a string and split it in json.
            # (input) _seperator: a string to be a seperator, _is_easymeal: True of False.
            # (output) array of meals. [{category: "한식", meal_arr: ["김치", "쌀밥"]}, {category: "한식", meal_arr: ["김치", "쌀밥"]}...]
            arr = _target_string.split("CATEGORY")
            meal_node_container = []
            for string in arr:
                meal_arr = string.split(_seperator)

                meal_arr = [target for target in meal_arr if target != '']
                if (meal_arr == []):
                    pass
                else:
                    if (_is_easymeal):
                        meal_node_container.append(
                            {"category": "간편식", "meal_arr": meal_arr})
                        break
                    else:
                        meal_node_container.append(
                            {"category": meal_arr[0], "meal_arr": meal_arr[1:]})
            return meal_node_container

        def correct_arr(array_to_splite):
            # Male clean the target array
            # (input) an array which includes noise
            # (output) ["breakfast string...", "lunch string..."]

            seperator = r'\d{2,}'
            text = '\n'.join(array_to_splite)
            sublists = re.sub(seperator, "|", text)
            sublists = sublists.replace("\nnan\nnan\nnan\nnan\nnan", "|")
            sublists = sublists.replace("\nnan\nnan", "|")
            sublists = sublists.replace("nan\n", "|")
            sublists = sublists.split("|")
            sublists = [item for item in sublists if item != ""]
            sublists = [item for item in sublists if 5 < len(item)]
            return sublists

        def is_easy_meal_nono(target_array):
            # Check whether the target aray is an array of easymeal.
            # (input) target_array: target array to check which is easymeal
            # (output) True/False
            indicator = target_array[-4]
            if (target_array[-4] == "nan" or target_array[-4] == r'\d{2,}'):
                return True
            else:
                return False

        def parse_meal_json_of_today(today_array, _for_where="inha"):
            # Convert meal array of a day to json
            # (input) today_array: array of a day meal, _for_where: method to parse pdf
            # (output) {breakfast: [{category: "", "menu":[]}, {category: "", "menu":[]}...], lunch:[], dinner:[], easy_meal:[]}
            today_arr = today_array
            seperator = "||||||||||||||||||||"
            if (_for_where == "inha"):
                meal_json = {
                    "breakfast": "", "lunch": "", "dinner": "", "easy_meal": ""
                }
                is_easy_meal_nono_flag = is_easy_meal_nono(today_arr)
                corrected_arr = correct_arr(today_arr)
                if (len(corrected_arr) == 0 or corrected_arr == None):
                    return "데이터 없음"

                easy_meal = ""
                if (is_easy_meal_nono_flag == True):
                    meal_json['easy_meal'] = []

                else:
                    easy_meal = corrected_arr[-1]
                    corrected_arr = corrected_arr[:-1]
                    pretty_string = makeup_string_for_inha_gishik(
                        easy_meal, seperator)
                    meal_node = package_meal(
                        pretty_string, seperator, _is_easymeal=True)
                    meal_json['easy_meal'] = meal_node

                breakfast = corrected_arr[0]
                corrected_arr = corrected_arr[1:]
                meal_node = package_meal(makeup_string_for_inha_gishik(
                    breakfast, seperator), seperator, _is_easymeal=False)
                meal_json['breakfast'] = meal_node

                dinner = corrected_arr[-1]
                corrected_arr = corrected_arr[:-1]

                meal_node = package_meal(makeup_string_for_inha_gishik(
                    dinner, seperator), seperator, _is_easymeal=False)
                meal_json['dinner'] = meal_node

                lunch = '\n\n'.join(corrected_arr)

                pretty_string = makeup_string_for_inha_gishik(lunch, seperator)
                meal_node = package_meal(
                    pretty_string, seperator, _is_easymeal=False)
                meal_json['lunch'] = meal_node

                return meal_json
            elif (_for_where == "inha_dimitory_banghak"):
                meal_json = {
                    "breakfast": [], "lunch": "", "dinner": "", "easy_meal": []
                }
                corrected_arr = correct_arr(today_arr)

                meal_node = package_meal(makeup_string_for_inha_gishik(
                    corrected_arr[0], seperator), seperator, _is_easymeal=False)
                meal_json['lunch'] = meal_node

                meal_node = package_meal(makeup_string_for_inha_gishik(
                    corrected_arr[1], seperator), seperator, _is_easymeal=False)
                meal_json['dinner'] = meal_node
                return meal_json

        def pdf_to_df(pdf_path):
            # parse dataframe from pdf
            # (input) pdf_path: local path where the pdf file is saved
            # (output) dataframe of pdf
            dfs = tabula.read_pdf(pdf_path,
                                  pages="all", encoding='utf-8', lattice=True)
            dataframes = [pd.DataFrame(table) for table in dfs]
            merged_df = pd.concat(dataframes, axis=1)
            return merged_df

        this_week_json_dict = {"Monday": "", "Tuesday": "", "Wednesday": "",
                               "Thursday": "", "Friday": "", "Saturday": "", "Sunday": ""}
        df = pdf_to_df(pdf_path)
        for idx, today in enumerate(["-1", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]):
            if (idx != 0):
                column_name = df.columns[idx]
                column_data = df[column_name]
                today_arr = parse_arr_from_df_col(column_data)
                today_meal_json = parse_meal_json_of_today(
                    today_arr, _for_where=_for_where)

                this_week_json_dict[today] = today_meal_json
        return this_week_json_dict


class Hakshik_thisweek(Shik_thisweek):
    # class for hakshik.
    where = "student"

    def __init__(self):
        super().__init__()

    def update_me(self):
        # Update "data" of slef as hakshik(meal) of this week.

        # Get data of this week student hakshik as a json.
        self.data = self.get_hakshik_json_of_this_week()

        # save json of this week in local
        self.save_my_data()

    def parse_meal_json_today(self, html_doc, weekday):
        def meal_list(weekday, when_idx, soup):
            day_of_week_idx = -1

            if (weekday == "Monday"):
                day_of_week_idx = 0
            if (weekday == "Tuesday"):
                day_of_week_idx = 1
            if (weekday == "Wednesday"):
                day_of_week_idx = 2
            if (weekday == "Thursday"):
                day_of_week_idx = 3
            if (weekday == "Friday"):
                day_of_week_idx = 4

            index_to_parse = 2*day_of_week_idx + when_idx

            menu_html = soup.find_all("table")[index_to_parse].find_all('tr')

            menu_list = []
            for i in range(len(menu_html)):
                if (i != 0):
                    menu = {"category": menu_html[i].find_all("th")[0].text.strip(), "meal_arr": menu_html[i].find_all(
                        "td")[0].text.strip().split('\r')}
                    menu_list.append(menu)

            return menu_list

        html_soup = bs4.BeautifulSoup(html_doc, "html.parser",
                                      from_encoding='utf-8')
        today_meal = {"breakfast": [], "lunch": [], "dinner": []}
        for idx, when in enumerate(["lunch", "self"]):
            meal_node = meal_list(weekday, idx, html_soup)
            today_meal[when] = meal_node
        return today_meal


class Gyoshik_thisweek(Hakshik_thisweek):
    where = "professor"

    def __init__(self):
        super().__init__()
        self.data = self.get_hakshik_json_of_this_week()

    def parse_meal_json_today(self, html_doc, weekday):
        def meal_list(weekday, when_idx, soup):
            day_of_week_idx = -1

            if (weekday == "Monday"):
                day_of_week_idx = 0
            if (weekday == "Tuesday"):
                day_of_week_idx = 1
            if (weekday == "Wednesday"):
                day_of_week_idx = 2
            if (weekday == "Thursday"):
                day_of_week_idx = 3
            if (weekday == "Friday"):
                day_of_week_idx = 4

            index_to_parse = day_of_week_idx

            menu_html = soup.find_all("table")[index_to_parse].find_all('tr')

            menu_list = []
            for i in range(len(menu_html)):
                if (i != 0):
                    menu = {"category": menu_html[i].find_all("th")[0].text.strip(), "meal_arr": menu_html[i].find_all(
                        "td")[0].text.strip().replace("\r", "").split('\t\t')}
                    menu_list.append(menu)

            return menu_list

        html_soup = bs4.BeautifulSoup(html_doc, "html.parser",
                                      from_encoding='utf-8')
        today_meal = {"breakfast": [], "lunch": [], "dinner": []}
        meal_node = meal_list(weekday, 0, html_soup)

        today_meal["breakfast"] = [meal_node[0]]
        today_meal["lunch"] = meal_node[1:3]
        today_meal["dinner"] = [meal_node[3]]
        return today_meal


class Dscrpt:
    client = None

    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv('chatgpt_token'))

    def of(self, foodname):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "Make some discription of the food upto 100 letters in Korean."},
                {"role": "user", "content": ", " .join(foodname)}
            ]
        )
        return completion.choices[0].message.content


class Recipe:
    def __init__(self):
        load_dotenv()
        self.man_recipe_url = os.getenv('man_recipe_url')

    def of(self, food):
        '''
        This is function gives recipe of the food recieved and information whether allergy trigger is included

        (input)
        food: name of food, in a word

        (output)
        {"recipe":["A", "B"...], "url":https://www.10000recipe.com/recipe/xxxxxx,  "allergy":{fork:"true", "egg":false, "beef":True, "chicken":true, "seafood":true}}
        '''

        '''
        item_id: id of the first item(the highest accuracy)
        '''
        url = self.man_recipe_url + f"/recipe/list.html?q={food}&accracy=date"
        page_doc = requests.get(url)
        page_soup = BeautifulSoup(page_doc.text, "html.parser")
        item_url = page_soup.select_one(".common_sp_link")
        item_id = None
        if (item_url == None):
            return None
        else:
            item_id = item_url.attrs.get("href").split('/')[-1]

        '''
        item_json: json parsed from document, includes noise
        '''
        url_of_item = f'{self.man_recipe_url}/recipe/{item_id}'
        item_doc = requests.get(url_of_item)
        item_soup = BeautifulSoup(item_doc.text, "html.parser")
        item_json = json.loads(item_soup.find(
            attrs={'type': 'application/ld+json'}).text)

        '''
        recipe: indegrants of the food. array form. ex)["돼지고기", "양파"]
        '''
        recipe = item_json.get('recipeIngredient')
        if (recipe == None):
            recipe = []

        '''
        allergy: true when the recipe includes xxx
        '''
        allergy_json = {"fork": False, "egg": False,
                        "beef": False, "chicken": False, "seafood": False}
        recipe_str = "".join(recipe)
        if (-1 < recipe_str.find("돼지") or -1 < recipe_str.find("돈육") or -1 < recipe_str.find("겹살") or -1 < recipe_str.find("목살") or -1 < recipe_str.find("항정살") or -1 < recipe_str.find("소세지") or -1 < recipe_str.find("소시지") or -1 < recipe_str.find("비엔나") or -1 < recipe_str.find("스팸") or -1 < recipe_str.find("햄") or -1 < recipe_str.find("미니족") or -1 < recipe_str.find("장족") or -1 < recipe_str.find("베이컨")):
            allergy_json["fork"] = True
        if (-1 < recipe_str.find("계란") or -1 < recipe_str.find("메추리알") or -1 < recipe_str.find("닭알") or -1 < recipe_str.find("수란")):
            allergy_json["egg"] = True
        if (-1 < recipe_str.find("닭") or -1 < recipe_str.find("치킨")):
            allergy_json["chicken"] = True
        if (-1 < recipe_str.find("소고기") or -1 < recipe_str.find("차돌박이") or -1 < recipe_str.find("사골") or -1 < recipe_str.find("우족") or -1 < recipe_str.find("곰탕") or -1 < recipe_str.find("한우") or -1 < recipe_str.find("와규") or -1 < recipe_str.find("갈비") or -1 < recipe_str.find("다시다")):
            allergy_json["beef"] = True
        if (-1 < recipe_str.find("새우") or -1 < recipe_str.find("게")):
            allergy_json["seafood"] = True

        res = {"recipe": recipe, "url": url_of_item,
               "allergy_json": allergy_json}

        return res


class DB:
    def __init__(self):
        aws_access_key = os.getenv('aws_access_key')
        aws_access_private = os.getenv('aws_access_key_private')

        dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1',
                                  aws_access_key_id=aws_access_key, aws_secret_access_key=aws_access_private)
        self.table = dynamodb.Table('hakshikking')

    def save(self, name, date,  location, when, category="", name_eng="", recipe="", url="", chicken="", beef="", fork="", egg="", seafood="", dscrpt="", dscrpt_eng=""):
        res = self.table.put_item(
            Item={
                "name": name, "date": f"{date}#{when}", "category": category, "location": location, "category": category, "name_eng": str(name_eng), "recipe": recipe, "url": url, "chicken": chicken, "beef": beef, "fork": fork, "egg": egg, "seafood": seafood, "dscrpt": str(dscrpt), "dscrpt_eng": str(dscrpt_eng)
            }
        )
        return res

    def find(self, name):
        res = self.table.query(
            KeyConditionExpression=Key('name').eq(
                name)
        )
        return res.get('Items')


class Translator:
    def __init__(self):
        self.deepl_token = os.getenv('deepl_token')

    def eng(self, korean_word):
        translator = deepl.Translator(self.deepl_token)
        return str(translator.translate_text(korean_word, source_lang="KO", target_lang="EN-US", context="food name/romanize"))
