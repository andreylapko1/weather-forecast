from app.models import *


def track(visitor, city_name):
    '''
    `   Function for recording search city into db

    :param visitor: Visitor instance
    :param city_name: Name of the search city
    '''

    search_inst = VisitorSearch(visitor=visitor, search_city=city_name)
    search_inst.save()
