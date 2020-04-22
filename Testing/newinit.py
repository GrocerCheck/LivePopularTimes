
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawler import run
from crawler import get_populartimes
from crawler import get_info_from_geocode
from crawler import get_places_by_search

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

"""

ENTRY POINT

"""

def get_address_from_geocode(lat, lng):
    """
    retrieve information from geo coordinates
    """

def get(api_key, types, p1, p2, n_threads=20, radius=180, all_places=False):
    """
    :param api_key: str; api key from google places web service
    :param types: [str]; placetypes
    :param p1: (float, float); lat/lng of the south-west delimiting point
    :param p2: (float, float); lat/lng of the north-east delimiting point
    :param n_threads: int; number of threads to use
    :param radius: int; meters;
    :param all_places: bool; include/exclude places without populartimes
    :return: see readme
    """
    params = {
        "API_key": api_key,
        "radius": radius,
        "type": types,
        "n_threads": n_threads,
        "all_places": all_places,
        "bounds": {
            "lower": {
                "lat": min(p1[0], p2[0]),
                "lng": min(p1[1], p2[1])
            },
            "upper": {
                "lat": max(p1[0], p2[0]),
                "lng": max(p1[1], p2[1])
            }
        }
    }

    return run(params)

def get_by_place_id(api_key, place_id):
    """
    retrieves the current popularity for a given place
    :param api_key:
    :param place_id:
    :return: see readme
    """
    return get_populartimes_by_place_id(api_key, place_id)

def get_address_from_geocode(lat, lng):
    """
    retrieve information from geo coordinates
    """

    return get_info_from_geocode(lat, lng)

def get_places_from_google(query):
    """
    retrieve a list of places
    query: string
    "supermarket campi bisenzio open now"
    """

    return crawler.get_places_by_search(query)


def get_by_fulldetail(place_detail, get_detail=False):
    """
    retrieves the current popularity for a given place
    :param place_detail
    {
        "place_id": "",
        "formatted_address": "",
        "name": "",
        "types": "Supermarket",
        "geometry": {
            "location": {
                "lat": 0,
                "lng": 0
            }
        }
    }
    :return: see readme
    """
    return get_by_detail(place_detail, get_detail)
