from geopy.distance import great_circle
import re

def price_value(min, max, price):
    if price >= min and price <= max:
        half_range = (max-min)/2
        normalized_price = price - min
        return (2 - (normalized_price/half_range))
    return 0

def distance_value(target_geo, target_distance, coords):
    if None not in (target_geo, target_distance, coords):
        distance = great_circle(target_geo, coords).miles
        if target_distance >= distance:
            half_range = target_distance/2
            return(2 - (distance/half_range))
    return 0

def date_value(target_date, page_date):
    if target_date == None or page_date == None:
        return  1
    if page_date > target_date:
        return 0
    return 1

def bedrooms_value(target_bedrooms, bedrooms):
    if target_bedrooms == None or bedrooms == None:
        return 1
    if target_bedrooms == bedrooms:
        return 1
    if target_bedrooms < bedrooms:
        return 1 + (1-1/(bedrooms - target_bedrooms))
    return 0

def sqft_value(target_sqft, sqft):
    if target_sqft == None or sqft == None:
        return 1
    if target_sqft == sqft:
        return 1
    if target_sqft < sqft:
        return 1 + (1-1/(sqft/target_sqft))
    return 0

def dogs_value(target_dogs, dogs):
    if target_dogs and dogs != None:
        if 'dogs' not in dogs:
            return 0
    return 1

def cats_value(target_cats, cats):
    if target_cats and cats != None:
        if 'cats' not in cats:
            return 0
    return 1

def calculate_score(content, target):
    price = price_value(target.pricemin, target.pricemax, content['price'])
    distance = distance_value(target.geo, target.distance, content['geo'])
    date = date_value(target.date, content["date"])
    bedrooms = bedrooms_value(target.bedrooms, content['bedrooms'])
    sqft = sqft_value(target.sqft, content['sqft'])
    dogs = dogs_value(target.dogs, content['attributes'])
    cats = cats_value(target.cats, content['attributes'])
    #wd = wd_value(target.wd, content['attributes'])
    #print(price, distance, date, bedrooms, sqft, dogs, cats)
    return(price * distance * date * bedrooms * sqft * dogs * cats)

def matches_search(content, target):
    score = calculate_score(content, target)
    if score != 0:
        return True
    return False
