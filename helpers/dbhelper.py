import pprint

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

def score_rank(id, db):
    sorted_collection = db.find().sort("score", -1)
    rank = 1
    for listing in sorted_collection:
        if id == listing["id"]:
            break
        rank += 1
    return(rank)

def print_top(n, db):
    print('Here are the top ', n, ' results:' )
    sorted_collection = db.find().sort("score", -1)
    cur_rank = 1
    for listing in sorted_collection:
        if cur_rank > n:
            break
        print(cur_rank, ":", listing["url"], "score:", listing["score"])
        cur_rank += 1
