import requests
from bs4 import BeautifulSoup
import json
from app.api import api, movie_search

@api.route('/get_movie_info' , methods=["GET"])
def get_movie_info(titleID):

    data = json.loads(titleID)

    title_ID = data["titleID"]

    target_url = 'https://www.imdb.com/title/' + title_ID

    page = requests.get(target_url).text

    soup = BeautifulSoup(page, 'html.parser')

    poster_box = soup.find('div', {'class': 'poster'})

    poster_img = list(poster_box.children)[1]

    poster_tag = list(poster_img.children)[1]

    poster_link = poster_tag['src']

    plot_box = soup.find('div', {'class': 'summary_text'})

    plot_text = list(plot_box.children)[0]

    plot_text = plot_text.lstrip()

    info = {
        "posterLink": poster_link,
        "plotText": plot_text
    }

    return json.dumps(info)

