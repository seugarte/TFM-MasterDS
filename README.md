# Final Project of Data Science - Kschool
## Sergio Ugarte Salvador

### Introduction

This project consist on a second-hand cars recommender system. During the project development, I had to complete many phases:

- **Web scraping:** In this phase we obtain the dataset by scrapping an online catalogue of second hand cars. In addtion, we repeat this process one more time to obtain a ranking of brands in a website.
- **Data processing:** Once we have obtained the datasets, the next step is cleaning the dataset and changing the type of some columns.
- **Creation of a Flask web application:** Finally, we create a web application with Flask to visualizate the results.


### Motivation

I decided to develop this project because of the lack of second hand cars recommenders and it is a pretty complex topic. Furthermore, many friends suggested me it and I thought that it was a good moment to develop it.


### Technologies

The technologies that I had to use to develop this recommender system are:

- **Python:** I have applied this programming language to do the *web scraping process*, the *data processing* and the files of the web application.
- **Flask:** It has been applied to create the web application.
- **Jinja2:** It has been emplyed in the web application to integrate python code into HTML.
- **Bootstrap:** It contains some HTML templates and it has been used to create the web application.
- **HTML:** It has been used in the web application.
- **Github:** As a repository.


### Data obtention

The first phase of the project is the data obtention to create our dataset. I created a python notebook where this process is explained, and where I had to develop two functions:

- **brands_rank_scraper():** This method extracts many car brands with its rating by accessing to a webiste.
- **cars_scraper():** This method extract the information of all the second hand cars of an online catalogue.

We can access to this file in the next url: https://github.com/seugarte/TFM-MasterDS/blob/master/web_scraping/Scraping_process.ipynb


### Data processing

The next phase is the data processing. Once we have obtained the previous datasets we must clean the main dataset. Concretely, we must follow the next process:

- **Data Analysis:** Here, I was analyzing both datasets to watch their appearance.
- **Data cleaning:** In this process I cleaned the dataset of null values, I deleted the duplicated values. Then, I changed the type of many columns and I added two extra columns with the latitude and the longitude of each province.
- **Brands score processing:** Here, we joined the brands ranking dataset with the main dataset to obtain the score of each brand.
- **Types score processing:** Finally, as in the previous process, I joined the types ranking with the main dataset to obtain the score of each type of vehicle.

Url of the information: https://github.com/seugarte/TFM-MasterDS/blob/master/data_processing/Data_processing.ipynb


### Visualization of the results

When I finished the previous procedures, I had to create a Flask application to visualizate the results obtained.

Concretely, I created two python files:

- **recommender.py:** This file contains the class 'Recommender' with its constructor and its methods. Here, we will create the method which recommend us the cars.
- **init.py:** This file manage the information that the user introduce in the form of the web page, and then the 'recommend' method is applied to obtained the cars and show it to the user in the 'main.html' file.

After those files, we had to create a template called 'main.html' which shows the results and allows the user introducing the data that he or she wants.

Url of the repository: https://github.com/seugarte/TFM-MasterDS/tree/master/web


### How to run the web application

If we want to run the Flask application, firstly we must download the 'web' directory. Afther that, in our terminal of linux we have to change the work directory to the 'web' directory, and then we must execute the next command: *python init.py*

Now we must write this url in our web browser: http://127.0.0.1:5000/
