# yelp-analysis
Yelp Academic Dataset Analysis

## Installation
To run the notebooks, you will need a standard installation of Anaconda with Python 3.x.

Additional libraries needed:
- sklearn
- s2sphere

## Data
Data used in the analysis can be downloaded at https://www.yelp.com/dataset.

# Project Motivation
This project was done as part of Udacity's Data Scientist Nanodegree. A yelp academic dataset was explored and the following questions were answered:
1. Are there differences in the star ratings by major categories (Restaurants, Shopping, Nightlife, ...)? Any differences in Restaurant categories?
2. What affects if a business will close?
3. Does vicinity to other similar business help or hurt ratings?

## File Descriptions
There are four notebooks that contain the analysis of the dataset.
- Yelp Academic Dataset.ipynb: Start here. Contains the introduction, data exploration, and data preparation.
- Question1.ipynb
- Question2.ipynb
- Question3.ipynb

There is also a ProcessData.py file which contains functions for processing data which are needed by the notebooks.

## Results
The results of the analysis are presented in a <a href="https://medium.com/@mei.eisenbach/so-you-want-to-open-a-restaurant-4b305061b8a0">Medium Post</a>.

Main findings:
- Restaurants have the lowest stars ratings compared to other types of businesses. Cafes have the highest average ratings within restaurants.
- The location of the business has the largest effect on whether it will stay open or not.
- You don’t need to be around other restaurants to get a good rating.
