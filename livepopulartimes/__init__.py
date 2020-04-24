#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .crawler import get_populartimes_by_place_id
from .crawler import get_populartimes_by_formatted_address
from .crawler import get_places_by_search
from .crawler import make_google_search_request

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

"""

ENTRY POINT

"""



def get_populartimes_by_address(formatted_address):
    """
    takes formatted address and 
    
    """
    
    
    return get_populartimes_by_formatted_address(formatted_address)


def get_populartimes_by_PlaceID(api_key, place_id):
    """
    retrieves the current popularity for a given place by placeId
    :param api_key:
    :param place_id:
    :return: json-formatted populartimes & current populartimes for a place (if applicable) alongside other scraped data
    
    :Example:
    
    detail_json = get_by_PlaceID(APIKEY, "ChIJnS31ep9zhlQR2ns5dwJVvcg")
    
    .. warning:: Makes API call
    
    """
    return get_populartimes_by_place_id(api_key, place_id)

def get_places_by_search(query):
    """
    Retrieve a list of places via google search
    :param query:
    :type query: string
    :return: list of places with scraped details (refer to readme for complete list)
    :Example:
    
    place_detail = get_places_by_search("supermarket campi bisenzio open now")
    
    """
    return get_places_by_search(query)




