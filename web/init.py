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
provinces = sorted(data['Province'].unique())

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def message():
    title = "Cars Recommender"
    subtitle = "Where you can find the best car"
    
    user_brand = request.form.get("brands")
    user_province = request.form.get("provinces")
    user_type = request.form.get("types")
    user_year = request.form.get("years")
    
    if user_province != None and user_brand != None and user_type != None and user_year != None:
        # This is for the select of the form
        user_year = int(user_year)
        r = Recommender(user_province, user_brand, user_type, user_year)
        res = r.recommend().values.tolist()
    else:
        res = []

    return render_template("main.html", res=res, title=title, subtitle=subtitle,
                           brands=brands, types=types,
                           years=years, provinces=provinces,
                           user_province=user_province, user_brand=user_brand,
                           user_type=user_type, user_year=user_year)


if __name__ == '__main__':
    app.run(debug=True)
