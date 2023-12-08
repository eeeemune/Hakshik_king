import requests
import json
from bs4 import BeautifulSoup

man_recipe_url = 'https://www.10000recipe.com'


def recipe(food):
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
    url = man_recipe_url + f"/recipe/list.html?q={food}&accracy=date"
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
    url_of_item = f'{man_recipe_url}/recipe/{item_id}'
    item_doc = requests.get(url_of_item)
    item_soup = BeautifulSoup(item_doc.text, "html.parser")
    item_json = json.loads(item_soup.find(
        attrs={'type': 'application/ld+json'}).text)

    '''
    recipe: indegrants of the food. array form. ex)["돼지고기", "양파"]
    '''
    recipe = item_json['recipeIngredient']

    '''
    allergy: true when the recipe includes xxx
    '''
    allergy_json = {"fork": False, "egg": False,
                    "beef": False, "chicken": False}
    recipe_str = "".join(recipe)
    if (-1 < recipe_str.find("돼지") or -1 < recipe_str.find("돈육") or -1 < recipe_str.find("겹살") or -1 < recipe_str.find("목살") or -1 < recipe_str.find("항정살") or -1 < recipe_str.find("소세지") or -1 < recipe_str.find("소시지") or -1 < recipe_str.find("비엔나") or -1 < recipe_str.find("스팸") or -1 < recipe_str.find("햄") or -1 < recipe_str.find("미니족") or -1 < recipe_str.find("장족")):
        allergy_json["fork"] = True
    if (-1 < recipe_str.find("계란") or -1 < recipe_str.find("메추리알") or -1 < recipe_str.find("닭알") or -1 < recipe_str.find("수란")):
        allergy_json["egg"] = True
    if (-1 < recipe_str.find("닭") or -1 < recipe_str.find("치킨")):
        allergy_json["chicken"] = True
    if (-1 < recipe_str.find("소고기") or -1 < recipe_str.find("차돌박이") or -1 < recipe_str.find("사골") or -1 < recipe_str.find("우족") or -1 < recipe_str.find("곰탕") or -1 < recipe_str.find("한우") or -1 < recipe_str.find("와규") or -1 < recipe_str.find("갈비") or -1 < recipe_str.find("다시다")):
        allergy_json["beef"] = True
    if (-1 < recipe_str.find("새우") or -1 < recipe_str.find("게")):
        allergy_json["seafood"] = True

    res = {"recipe": recipe, "url": url_of_item, "allergy_json": allergy_json}

    return res
