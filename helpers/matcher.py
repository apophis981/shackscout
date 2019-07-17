from geopy.distance import great_circle

def price_value(min, max, price):
    if price >= min and price <= max:
        half_range = (max-min)/2
        normalized_price = price - min
        return (2 - (normalized_price/half_range))
    return 0

def distance_value(target_geo, target_distance, coords):
     distance = great_circle(target_geo, coords).miles
     if target_distance >= distance:
         half_range = target_distance/2
         return(2 - (distance/half_range))
     return 0

def calculate_score(content, target):
    price = price_value(target.pricemin, target.pricemax, content['price'])
    distance = distance_value(target.geo, target.distance, content['geo'])
    date = date_value(target.date, content["date"])
    return(price * distance * date)

def matches_search(content, target):
    score = calculate_score(content, target)
    if score != 0:
        return True
    return False
