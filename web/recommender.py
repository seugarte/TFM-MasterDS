import pandas as pd
import numpy as np
import geopy
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

class Recommender:

    def __init__(self, user_province, user_brand, user_type, user_year):
        """
        :param user_province: the province selected by the user in his request
        :param user_brand: the car brand selected by the user in his request
        :param user_type: The car type selected by the user in his request
        :param user_year: The year selected by the user in his request
        """

        self.data = pd.read_csv('web/resources/cars_information.csv', sep=',', encoding='utf-8')
        self.brands_df = pd.read_csv('web/resources/brands_rank.csv', sep=';', encoding='utf-8')
        self.types_df = pd.read_csv('web/resources/type_car_score.csv', sep=';', encoding='utf-8')

        self.province = province_city
        self.brand = user_brand
        self.type = user_type
        self.year = int(user_year)
        self.lat = self.user_location_coords()[0]
        self.lon = self.user_location_coords()[1]

        if self.brands_df[self.brands_df['brand'] == self.brand].score.empty:
            self.brand_score = 0
        else:
            self.brand_score = int(self.brands_df[self.brands_df['brand'] == self.brand].score)
            
        self.type_score = int(self.types_df[self.types_df['Type'] == self.type].score)
        self.scores = [self.brand_score, self.type_score, self.year]

        # Weights of the characteristics that the user can choose
        self.weight_brand = 30
        self.weight_type = 40
        self.weight_year = 40
        self.weight_province = 10
        self.total_weight = self.weight_brand + self.weight_type + self.weight_year + self.weight_city

    def user_location_coords(self):
        """
        This function calculates the coordinates of the city entered by the user
        """

        geolocator = Nominatim()
        location = geolocator.geocode(self.province)

        return [location.latitude, location.longitude]

    def cities_distance(self, province_lat, province_lon):
        """
        :param province_lat: the value in the dataset's lat column to the corresponding province
        :param province_lon: the value in the dataset's lon column to the corresponding province
        :param user_lat: The corresponding lat value in the location dataset of the province selected by the user
        :param user_lon: The corresponding lon value in the location dataset of the province selected by the user

        :return: The value in kilometers of the distance between the two provinces.

        Usage of the Vincenty distance
        """

        column_province = [province_lat, province_lon]
        user_province = [self.lat, self.lon]

        return vincenty(column_province, user_province).km

    def weighted_sum(self, province_row, brand_row, type_row, year_row):
        """
        :param province_row: value of correcponding register in the the province_metric field
        :param brand_row: value of correcponding register in the the brand_metric field
        :param type_row: value of correcponding register in the the type_metric field
        :param year_row: value of correcponding register in the the year_metric field
        :return: the weighted sum of the input parameters
        """

        params = np.array([province_row, brand_row, type_row, year_row])
        weights = np.array([self.weight_province, self.weight_brand, self.weight_type, self.weight_year])

        num = sum(params * weights) * 1.0
        return num / self.total_weight
    
    def recommend(self):
        """
        The function which recommends us the cars
        :return: the k registers closest to the user's selection
        """

        score_columns = ['Brand Score', 'Type Score', 'Year']

        self.data['Province Metric'] = self.data.apply(lambda row: self.cities_distance(row['Latitude'], row['Longitude']), axis=1)

        for i, element in enumerate(['Brand', 'Type', 'Year']):
            new_column = element + ' Metric'
            print(new_column)
            try:
                self.data[new_column] = self.data.apply(lambda row: abs(int(row[score_columns[i]]) - self.scores[i]), axis=1)
            except TypeError:
                print(new_column)

        self.data['Total Metric'] = self.data.apply(lambda row: self.weighted_sum(row['Province Metric'], row['Brand Metric'], row['Type Metric'], row['Year Metric']), axis=1)

        result_columns = ['Title', 'Brand', 'Province', 'Year', 'Kms', 'Price (€)', 'Url', 'Total Metric']

        res = self.data[result_columns].sort_values(by=['Total Metric'], ascending=True).head(10)


        return res
