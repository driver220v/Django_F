import requests
from bs4 import BeautifulSoup
#
from scrapper.forms import FilmForm
from scrapper.log_module import logger
from scrapper.management.scrape_utils import model_film

from scrapper.management.scrape_utils.scrapper_gather import main_gather as get_links

# Парсинг и попытка сохранить в БД
from scrapper.models import Film


def get_content_attrs(r):
    soup = BeautifulSoup(r.content, 'lxml')
    title_raw_header_below = soup.find('h1', class_='mop-ratings-wrap__title mop-ratings-wrap__title--top')
    title_raw_under_header = soup.find('span', class_='mop-ratings-wrap__title--small')

    tomatores = soup.find('div', class_='mop-ratings-wrap__half critic-score')
    auidience = soup.find('div', class_='mop-ratings-wrap__half audience-score')

    title = None
    tomatores_score = None
    auidience_score = None
    premier = None
    genre_type = None

    if len(title_raw_under_header.text) == 0:
        title = title_raw_header_below.text.strip()
    else:
        title = title_raw_under_header.text.strip()

    try:
        genre_raw = soup.find(text="Genre:")
        genre_type = genre_raw.find_next().text.strip()
    except AttributeError:
        genre_type = 'Null'
    try:
        premier_raw = soup.find(text="Premiere Date:")
        premier = premier_raw.find_next().text.strip()
    except AttributeError:
        premier = 'Null'

    try:
        tomatores_score = tomatores.find('span', class_='mop-ratings-wrap__percentage').text.strip()
    except AttributeError:
        tomatores_score = 'Null'
    try:
        auidience_score = auidience.find('span', class_='mop-ratings-wrap__percentage').text.strip()
    except AttributeError:
        auidience_score = 'Null'

    return title, tomatores_score, auidience_score, premier, genre_type


def get_url_content(url):
    r = requests.get(url)
    if r.status_code == 200:
        title, tomatores_score, auidience_score, premier, genre_type = get_content_attrs(r)
        if len(title) != 0 and len(tomatores_score) != 0 and len(auidience_score) != 0 and len(genre_type) != 0 and len(
                premier) != 0:

            if Film.objects.filter(title=title,
                                   avg_tomatometer=tomatores_score,
                                   avg_audience_score=auidience_score,
                                   genre=genre_type,
                                   premier=premier).exists():
                pass
            else:
                f = FilmForm(dict(title=title,
                                  avg_tomatometer=tomatores_score,
                                  avg_audience_score=auidience_score,
                                  genre=genre_type,
                                  premier=premier))
                print(f)
                model_film.append(f)
                if f.is_valid():
                    model_film.append(f)
                else:
                    logger.warning(f.errors)


def main_parse(lst_links):
    for url in lst_links:
        get_url_content(url)


main_parse(get_links())
