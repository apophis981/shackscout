from geopy.distance import great_circle

def in_price_rage(min, max, price):
    if price >= min and price <= max:
        return True
    return False

def distance(target, coords):
     distance = great_circle(target.geo, coords).miles
     if target.distance >= distance:
         return True
     return False


def matches_search(content, target):
    if (in_price_rage(target.pricemin, target.pricemax, content['price']) and
            distance(target, content['geo'])):
        return True
    return False
