__author__ = 'Sergio'

import pandas as pd
from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
from recommender_class import Recommender

data = pd.read_csv('resources/cars_information.csv', sep=';', encoding='utf-8')

brands = sorted(data['Brand'].unique())
types = sorted(data['Type'].unique())
years = sorted(data['Year'].unique())
cities = sorted(data['City'].unique())

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def message():
    title = "Cars Recommender"
    subtitle = "Where you can find your best car"
    
    usr_city = request.form.get("cities")
    usr_brand = request.form.get("brands")
    usr_type = request.form.get("types")
    usr_year = request.form.get("years")

    if usr_city != None and usr_brand != None and usr_type != None and usr_year != None:
        r = Recommender(usr_city, usr_brand, usr_type, usr_year)
        res = r.recommend().values.tolist()
    else:
        res = []

    return render_template("main.html", res=res, title=title, subtitle=subtitle,
                           brands_list=brands, types_list=types,
                           years_list=years, cities_list=cities,
                           query_city=usr_city, query_brand=usr_brand,
                           query_type=usr_type, query_year=usr_year)


if __name__ == '__main__':
    app.run()
