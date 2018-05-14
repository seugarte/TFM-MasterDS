__author__ = 'Sergio'

import pandas as pd
from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
from recommender import Recommender

data = pd.read_csv('web/resources/cars_information.csv', sep=',', encoding='utf-8')

brands = sorted(data['Brand'].unique())
types = sorted(data['Type'].unique())
years = sorted(data['Year'].unique())
cities = sorted(data['City'].unique())

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def message():
    title = "Cars Recommender"
    subtitle = "Where you can find the best car"
    
    usr_brand = request.form.get("brands")
    usr_city = request.form.get("cities")
    usr_type = request.form.get("types")
    usr_year = request.form.get("years")
    
    if usr_city != None and usr_brand != None and usr_type != None and usr_year != None:
        r = Recommender(usr_city, usr_brand, usr_type, usr_year)
        res = r.recommend().values.tolist()
    else:
        res = []

    return render_template("main.html", res=res, title=title, subtitle=subtitle,
                           brands=brands, types=types,
                           years=years, cities=cities,
                           usr_city=usr_city, usr_brand=usr_brand,
                           usr_type=usr_type, usr_year=usr_year)


if __name__ == '__main__':
    app.run(debug=True)
