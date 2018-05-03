#!/usr/bin/python
# -*- coding: utf-8 -*-

#Scraper cars rank

import pandas as pd
from bs4 import BeautifulSoup
import requests

def brands_rank_scraper():
 
    #The 2 links in the catalog
    rank_url_1 = "http://en.classora.com/reports/v46699/ranking-of-the-worlds-most-popular-car-brands?id=466&groupCount=50&startIndex=1"
    rank_url_2 = "http://en.classora.com/reports/v46699/ranking-of-the-worlds-most-popular-car-brands?id=466&groupCount=50&startIndex=51"
    
    rank_urls = [rank_url_1, rank_url_2]
    final_rank_list = []
    
    #Foreach url, que take the brands and their score and we store them in a final list
    for url in rank_urls:
        rank_req = requests.get(url)
        cars_soup = BeautifulSoup(rank_req.text, "html.parser")

        brand_cells = cars_soup.find_all("td", {"class": "rankingEntryCell"})
        points_cells = cars_soup.find_all("td", {"class": "rankingDataCell"})
        
        brand_list = [[brand_cells[index].get_text().lower(), points_cells[index].get_text()] for index, val in enumerate(brand_cells)]   
        final_rank_list += brand_list
     
    #Finally, the information is stored in a csv file
    rank_df = pd.DataFrame(final_rank_list, columns=['brand', 'score'])
    rank_df.to_csv("../data/brands_rank.csv", sep = ';', index = False)
