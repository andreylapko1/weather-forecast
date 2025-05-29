from app.models import *


def track(visitor, city_name):
    search_inst = VisitorSearch(visitor=visitor, search_city=city_name)
    search_inst.save()
