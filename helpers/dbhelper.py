
def not_in(id, db):
    """
    Returns True or False of if listing exists already in database

    Parameters:
    id: craigslist id of listings
    db: pointer to database
    Returns boolean
    """
    exists = db.find_one({'id': id})
    return not exists

def post(content, db):
    """
    Inserts new listing into database

    Parameters:
    content: dictionary containing listing info
    db: pointer to database
    """
    result = db.insert_one(content)
    print('One post: ', content["url"])
