from app.search import search_bp
import json
from flask import render_template, redirect, url_for
from flask import request
from app.api import movie_search, web_scraper


@search_bp.route('/search_page', methods=["GET", "POST"])
def search_page():
    error = None
    data = None
    if request.method == "POST":
        search_criteria = request.form.get('search_criteria', False)

        info = {
            "search": search_criteria
        }

        data = movie_search.search_movie(json.dumps(info))

        if(data == {}):
            error = "No movies of that title exist!"
            state = {
                "status": error
            }
            return json.dumps(state)
        else:
            #return data


            return redirect(url_for("search.search_results_page", data=data))
    return render_template("search_results.html", data=data)

@search_bp.route('/search_results_page', methods=["GET", "POST"])
def search_results_page():
    data = request.values.get('data')
    loaded_data = json.loads(data)
    return render_template("search_results.html", data=loaded_data)

@search_bp.route('/movie_details_page', methods=["GET", "POST"])
def movie_details_page():
    movie_title = request.values.get('title')
    is_adult = request.values.get('isAdult')
    start_year = request.values.get('startYear')
    runtime = request.values.get('runtime')
    genres = request.values.get('genres')
    movieID = request.values.get('id')

    info = {
        "titleID": movieID
    }

    scraped_data = web_scraper.get_movie_info(json.dumps(info))
    loaded_scraped_data = json.loads(scraped_data)

    crew_data = movie_search.get_cast(json.dumps(info))
    loaded_crew_data = json.loads(crew_data)



    poster_link = loaded_scraped_data["posterLink"]
    plot_text = loaded_scraped_data["plotText"]

    cast = {}
    for i in loaded_crew_data:
        cast[loaded_crew_data[i]["name"]] = {
            "name": loaded_crew_data[i]["name"],
            "category": loaded_crew_data[i]["category"],
            "job": loaded_crew_data[i]["job"],
            "characters": loaded_crew_data[i]["characters"]
        }


    return render_template('movie_details.html', movie_title=movie_title, start_year=start_year,
                           runtime=runtime, genres=genres, poster_link=poster_link, plot_text=plot_text, cast=cast)



