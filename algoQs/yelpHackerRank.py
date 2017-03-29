def sort_businesses_by_rating(businesses):
    """
    List of bussinesses info where each element is a dictionary containing
    id and rating. Sort the businesses by their rating in decreasing order.
    Preserve the original ordering if two businesses have same rating
    Args:
        businesses: List of bussinesses info where business info is
        a dictionary containing id and rating.
    Return:
        List of businesses info sorted by rating in decreasing order

    Example input:
    [
        {'id': 101, rating: 5.0},
        {'id': 102, rating: 2.0},
        {'id': 103, rating: 3.0},
        {'id': 104, rating: 5.0},
        {'id': 105, rating: 5.0},
    ]
    Expected output:
    [
        {'id': 101, rating: 5.0},
        {'id': 104, rating: 5.0},
        {'id': 105, rating: 5.0},
        {'id': 103, rating: 3.0},
        {'id': 102, rating: 2.0},
    ]    
    """
    