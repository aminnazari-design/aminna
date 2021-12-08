import requests
from flask import redirect, render_template, request, session
from functools import wraps
import json
from requests import api





def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code



def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
def test(data):
    params = {
   'api_key': '65F9C680714F423087E6559D2471A9F3',
   'type': 'search',
   'amazon_domain': 'amazon.com',
   'search_term': data
    }
    api_result = requests.get('https://api.rainforestapi.com/request', params)
    datas = api_result.json()
    # datas = (json.dumps(api_result.json()))
    try:
        datas = api_result.json()
        api_info = datas["search_results"]
        return api_info
    except (KeyError, TypeError, ValueError):
        return None
    # datas = response.json()
    # print(datas)
    # print(datas['product'])
    # api_info = datas["search_results"]
    # api_info = {
    # "product_name":datas["search_results"]["title"] ,
    # "brand": datas["product"]["brand"] ,
    # "rating": datas["product"]["rating"]  ,
    # "images" : datas["product"]["images"] 
    # }
    # print(api_info)
    
    # return api_info
# print the JSON response from Rainforest API
    # print((api_result.json()))
def datad_collector(key):
    url = "https://amazon-price1.p.rapidapi.com/search"

    querystring = {"marketplace":"ES","keywords":key}

    headers = {
    'x-rapidapi-host': "amazon-price1.p.rapidapi.com",
    'x-rapidapi-key': "1ad3f1d255mshb88f6dab823d53ep1171f3jsn68b359b167c4"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
