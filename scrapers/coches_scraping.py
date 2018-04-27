#!/usr/bin/python
# -*- coding: utf-8 -*-

#Scraper cars catalog

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

def scraper():
    
    #==========================================================================
    # Obtention of the advertisements url
    #==========================================================================
    
    # webpage url
    url = "https://www.coches.com/coches-segunda-mano/coches-ocasion.htm"
    
    # Obtention of the data
    req = requests.get(url)
    cars_soup = BeautifulSoup(req.text, "html.parser")
    
    # We obtain the number of ads in the catalog
    total_number_ads_block = str(cars_soup.findChild("div", {"class": "informacion"})\
                                 .find("strong").contents[0])
    total_number_ads = int(total_number_ads_block.replace('.', ''))
    
    # Now we find the number of pages
    ads_per_page = len(cars_soup.find_all("div", {"class": "oferta"}))
    number_of_pages = round(total_number_ads / ads_per_page)
    
    #==========================================================================
    # Creation of the csv file
    #==========================================================================
    
    # Declaration of the variables
            
    ## General variables declaration
    title, brand, city, price, year, km, fuel, type_gears, seller, guarantee, colour = \
            "", "", "", "", "", "", "", "", "", "", ""

    ## Technical variables declaration
        
    ### Measurements and weights
    boot_cap, length, height, width, doors, vacancies, tank, weight, max_weight, car_body = \
            "", "", "", "", "", "", "", "", "", ""
        
    ### Use and features
    max_speed, comb_fuel, urb_use, extraurb_use, acel, autonomy, c02_emissions = "", "", "", "", "", "", ""
        
    ### Engine and transmission
    output, cubic_cap, cylinders, max_par, gears, transm, tract = "", "", "", "", "", "", ""
            
    ## Variables to build the table
    header = ['Title', 'Brand', 'City', 'Price', 'Year', 'Kms', 'Fuel', 'Type of Gears', 'Seller', 'Guarantee', 
                'Colour', 'Boot Capacity', 'Length', 'Height', 'Width', 'Doors', 'Vacancies', 'Tank', 'Weight', 
                'Max Weight', 'Car Body', 'Max Speed', 'Comb Fuel', 'Urban Use', 'Extraurban Use', 'Aceleration', 
                'Autonomy', 'CO2 Emissions', 'Output', 'Cubic Capacity', 'Cylinders', 'Max Par', 'Gears', 'Transmission',
                'Traction', 'Url']
    body = []
    
    # Creation of the table using the information of each page
    for i in range(1, number_of_pages):
        url_with_page = 'https://www.coches.com/coches-segunda-mano/coches-ocasion.htm?page=%d' %i
        sub_req = requests.get(url_with_page, allow_redirects = False)

        # If the status code is 200, the resource has been found
        if sub_req.status_code == 200:
            info_soup = BeautifulSoup(sub_req.text, "html.parser")
            # Obtention of the url of each car
            offers = info_soup.findChildren("div", {"class": "oferta"})

            for o in offers:
                
                #Obtention of the information  
                link = o.find("a", href=True)["href"]
                link_req = requests.get(link)
                link_soup = BeautifulSoup(link_req.text, "html.parser") 

                ## 'div' where the general information is located
                div_car_info = link_soup.find_all("div", {"class": "col-lg-12 hidden-md hidden-sm hidden-xs"}) 
                
                 ## 'div' where the measures information is located
                div_measures_info = link_soup.find_all("div", {"class": "col-lg-12 col-md-12 col-sm-12 col-xs-12 hidden-xs hidden-sm"}) 

                ## 'div' where the performance information is located
                div_performance = link_soup.find_all("div", {"class": "row hidd"})
                
                 ## 'div' where the engine information is located
                div_engine = link_soup.find_all("div", {"class": "col-lg-12 col-md-12 col-sm-12 col-xs-12 hidden-xs hidden-sm"})
                
                ## Now we obtain the features
                if link_soup.findChild("ol", {"class": "breadcrumb"}) != None:
                    title = link_soup.findChild("ol", {"class": "breadcrumb"}).find("span").get_text()
                    brand = title.split(" ")[0]
                if link_soup.findChild("h1", {"class": "cc_model_price"}) != None:
                    city = link_soup.findChild("h1", {"class": "cc_model_price"}).find_all("small")[1].get_text()       
                if len(div_car_info) > 0:
                    for div in div_car_info:
                        divs = div.find_all("div", {"class": "cc_car_data"})
                        for i in divs:
                            if i.find("small").get_text() == "Precio":
                                price = i.find("strong").get_text()
                            if i.find("small").get_text() == "Año":
                                year = i.find("strong").get_text()
                            if i.find("small").get_text() == "Kilómetros":
                                km = i.find("strong").get_text()
                            if i.find("small").get_text() == "Combustible":
                                fuel = i.find("strong").get_text()
                            if i.find("small").get_text() == "Cambio":
                                type_gears = i.find("strong").get_text()
                            if i.find("small").get_text() == "Vendedor":
                                seller = i.find("strong").get_text()
                            if i.find("small").get_text() == "Garantía":
                                guarantee = i.find("strong").get_text()
                            if i.find("small").get_text() == "Color exterior":
                                colour = i.find("strong").get_text()
                if len(div_measures_info) > 0:
                    for div in div_measures_info:
                        divs = div.find_all("div", {"class": "cc_car_data"})
                        for i in divs:
                            if i.find("small").get_text() == "Capacidad maletero":
                                boot_cap = i.find("strong").get_text()
                            if i.find("small").get_text() == "Longitud":
                                length = i.find("strong").get_text()
                            if i.find("small").get_text() == "Altura":
                                height = i.find("strong").get_text()
                            if i.find("small").get_text() == "Anchura":
                                width = i.find("strong").get_text()
                            if i.find("small").get_text() == "Núm. puertas":
                                doors = i.find("strong").get_text()
                            if i.find("small").get_text() == "Núm. plazas":
                                vacancies = i.find("strong").get_text()
                            if i.find("small").get_text() == "Capacidad depósito":
                                tank = i.find("strong").get_text()
                            if i.find("small").get_text() == "Peso":
                                weight = i.find("strong").get_text()
                            if i.find("small").get_text() == "Peso máx autorizado":
                                max_weight = i.find("strong").get_text()
                            if i.find("small").get_text() == "Carrocería":
                                car_body = i.find("strong").get_text()
                if len(div_performance) > 0:
                    for div in div_performance:
                        divs = div.find_all("div", {"class": "cc_car_data"}) 
                        for i in divs:
                            if i.find("small").get_text() == "Velocidad máxima":
                                max_speed = i.find("strong").get_text()
                            if i.find("small").get_text() == "Consumo combinado":
                                comb_fuel = i.find("strong").get_text()
                            if i.find("small").get_text() == "Consumo urbano":
                                urb_use = i.find("strong").get_text()
                            if i.find("small").get_text() == "Consumo extraurbano":
                                extraurb_use = i.find("strong").get_text()
                            if i.find("small").get_text() == "Aceleración 0-100":
                                acel = i.find("strong").get_text()
                            if i.find("small").get_text() == "Autonomía":
                                autonomy = i.find("strong").get_text()
                            if i.find("small").get_text() == "Emisión co2":
                                c02_emissions = i.find("strong").get_text()
                if len(div_engine) > 0:
                    for div in div_engine:
                        divs = div.find_all("div", {"class": "cc_car_data"})
                        for i in divs:
                            if i.find("small").get_text() == "Potencia":
                                output = i.find("strong").get_text()
                            if i.find("small").get_text() == "Cilindrada":
                                cubic_cap = i.find("strong").get_text()
                            if i.find("small").get_text() == "Número cilindros":
                                cylinders = i.find("strong").get_text()
                            if i.find("small").get_text() == "Par máximo":
                                max_par = i.find("strong").get_text()
                            if i.find("small").get_text() == "Núm. marchas":
                                gears = i.find("strong").get_text()
                            if i.find("small").get_text() == "Transmisión":
                                transm = i.find("strong").get_text()
                            if i.find("small").get_text() == "Tracción":
                                tract = i.find("strong").get_text()
                            
                ## We append all the features to the body
                body.append([title, brand, city, price, year, km, fuel, type_gears, seller, guarantee, colour, boot_cap, length,
                            height, width, doors, vacancies, tank, weight, max_weight, car_body, max_speed, comb_fuel, urb_use,
                            extraurb_use, acel, autonomy, c02_emissions, output, cubic_cap, cylinders, max_par, gears, transm,
                            tract, link])
     
    ## CSV file building
    cars_df = pd.DataFrame(body, columns=header)
    cars_df.to_csv('../data/cars_data.csv', sep = ';', index = False, encoding = 'utf-8')
