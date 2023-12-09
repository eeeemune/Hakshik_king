from datetime import datetime, timedelta
import models

dscrpt = models.Dscrpt()
recipe = models.Recipe()
db = models.DB()
translator = models.Translator()

gi = models.Gishik_thisweek()
week_node_gi = gi.get_shik()

hak = models.Hakshik_thisweek()
week_node_hak = hak.get_shik()

gyo = models.Gyoshik_thisweek()
week_node_gyo = gyo.get_shik()


def setup_data_of(food_name):
    recipe_node = recipe.of(food_name)
    if (recipe_node == None):
        recipe_node = {"recipe": [], "url": None, "allergy_json": {
            "fork": None, "egg": None, "beef": None, "chicken": None, "seafood": None}}

    name = food_name
    eng_name = translator.eng(food_name)
    dsc = dscrpt.of(food_name)
    dsc_eng = translator.eng(dsc)
    recipe_string = str(recipe_node["recipe"])
    url = recipe_node["url"]

    chicken = recipe_node["allergy_json"]["chicken"]
    fork = recipe_node["allergy_json"]["fork"]
    beef = recipe_node["allergy_json"]["beef"]
    egg = recipe_node["allergy_json"]["egg"]
    seafood = recipe_node["allergy_json"]["seafood"]

    return {"name": name, "eng_name": eng_name, "dsc": dsc, "dsc_eng": dsc_eng, "recipe": recipe_string, "url": url, "chicken": chicken, "beef": beef, "fork": fork, "seafood": seafood, "egg": egg}


def update_db(target_node, date, where, when):
    '''
    target_node: {"category":"", "meal_arr":["", "", ...]}
    '''
    for item in target_node['meal_arr']:
        item_node = db.find(item)
        '''
        Save the item to database if there is no exists same name
        '''
        if (len(item_node) == 0):
            item_info = setup_data_of(item)
            db.save(name=item_info['name'], date=date, location=where, when=when, category=target_node.get("category"), name_eng=item_info.get('eng_name'), recipe=item_info.get('recipe_string'), url=item_info.get('url'), chicken=item_info.get('chicken'),
                    beef=item_info.get('beef'), fork=item_info.get('fork'), egg=item_info.get('egg'), seafood=item_info.get('seafood'), dscrpt=item_info.get('dsc'), dscrpt_eng=item_info.get("dsc_eng"))
        else:
            '''
            Update menu db
            '''

            db.save(name=item_node[0]['name'], date=date, location=where, when=when, category=target_node.get("category"), name_eng=item_node[0].get('name_eng'), recipe=item_node[0].get('recipe_string'), url=item_node[0].get('url'), chicken=item_node[0].get('chicken'),
                    beef=item_node[0].get('beef'), fork=item_node[0].get('fork'), egg=item_node[0].get('egg'), seafood=item_node[0].get('seafood'), dscrpt=item_node[0].get('dscrpt'), dscrpt_eng=item_node[0].get("dscrpt_eng"))


def date_of(weekday):
    today = datetime.today()
    today_weekday = today.weekday()
    monday_date = today - timedelta(days=today_weekday)
    res_date = monday_date + timedelta(days=weekday)
    return res_date.strftime("%Y-%m-%d")


def update(when_list, where, week_node):
    week_arr = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    if (where == "gyo" or where == "hak"):
        week_arr = week_arr[:4]
    for weekday_idx, weekday in enumerate(week_arr):
        today_node = week_node[weekday]
        for when in when_list:
            for category_node in today_node[when]:
                update_db(category_node, date_of(weekday_idx), where, when)


update(["breakfast", "lunch", "easy_meal", "dinner"], "gi", week_node_gi)
update(["lunch"], "hak", week_node_hak)
update(["breakfast", "lunch", "dinner"], "gyo", week_node_gyo)
