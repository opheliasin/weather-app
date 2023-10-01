from flask import render_template, request, flash, redirect, url_for
from app.forms import SearchForm
from app import app
import requests


@app.route('/', methods = ['GET', 'POST'])
def search():
    form = SearchForm()
    query = form.query.data
    if request.method == "POST" and query == "":
        flash('City/Zipcode is required.', category = "error")
        return render_template("index.html", form = form) 
    elif request.method == "POST" and form.validate_on_submit():
        return redirect((url_for('search_results', query=query, form = form)))
    else:
        return render_template("index.html",form = form) 

@app.route('/search_results/<query>')
def search_results(query):
    form = SearchForm()
    api_key = '7984d743b5094cd6e05a6650b8585015'
    params = {"q": query, "appid" : api_key,"units": "metric"}
    weather_response = requests.get('https://api.openweathermap.org/data/2.5/weather', params = params)
    data = weather_response.json()

    #icon
    icon_url = "https://openweathermap.org/img/wn/" + data['weather'][0]['icon'] + "@2x.png"
    print(data)
    print(data['main']['temp'])
    print(data['weather'][0]['description'])
    return render_template("search_results.html", data = data, city = query, form = form, icon_url = icon_url)