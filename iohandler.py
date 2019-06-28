import argparse

def get_input(input_args):
    parser = argparse.ArgumentParser(description='Get user search specifics')

    # Mandatory arguements
    parser.add_argument('distance', type=int,
        help='Max number of miles away from desired location')
    parser.add_argument('geo', type=float, nargs=2,
        help='Lattitude then longitude ex: geo 37.557516 -122.287266')
    parser.add_argument('pricemin', type=int,
        help='minimum price for listing')
    parser.add_argument('pricemax', type=int,
        help='maximum price for listing')

    # Optional arguements
    parser.add_argument('--bedrooms', type=int, metavar='#',
                        help='Minimum number of bedrooms')
    parser.add_argument('--spacemin', type=int, metavar='###',
                        help='Minimum square footage')
    parser.add_argument('--spacemax', type=int, metavar='####',
                        help='Maximum square footage')
    parser.add_argument('--cats', help='Add if you want cats allowed',
                        action='store_true')
    parser.add_argument('--dogs', help='Add if you want dogs allowed',
                        action='store_true')
    parser.add_argument('--wd', help='Add if you want washer and dryer',
                        action='store_true')


    args = parser.parse_args(input_args)
    return args
