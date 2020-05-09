#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LICENSE

MIT License

Copyright (c) 2020 ihasdapie

Copyright (c) 2020 TheJoin95
Copyright (c) 2018 m-wrzr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from .crawler import get_populartimes_by_place_id
from .crawler import get_populartimes_by_formatted_address
from .crawler import get_places

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

"""

ENTRY POINT

"""



def get_populartimes_by_address(formatted_address, proxy = False):
    """
    retrieves populartimes & other location data for a given place by formatted address
    :param formatted_address: Preferred format: "(*location name*) , *full address*, *city*, *province/state/etc*, *country*"
    :param proxy: A dictionary of proxies of format {
        "http" : "http://10.10.1.10:2138",
        "https" : "http://10.10.1.10:1080",
        }
    :type formatted_address: string
    :return: json-formatted populartimes & current populartimes for a place (if applicable) alongside other scraped data
    :Example:

    detail_json = get_populartimes_by_address("(Costco) 605 Expo Blvd, Vancouver, BC V6B 1V4, Canada", proxy = proxy)

    """

    return get_populartimes_by_formatted_address(formatted_address, proxy)

def get_populartimes_by_PlaceID(api_key, place_id):
    """
    retrieves populartimes & other location data for a given place by placeId
    :param api_key:
    :param place_id:
    :return: json-formatted populartimes & current populartimes for a place (if applicable) alongside other scraped data
    :Example:

    detail_json = get_populartimes_by_PlaceID(APIKEY, "ChIJnS31ep9zhlQR2ns5dwJVvcg")

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

    places = get_places_by_search("pubs open in London")
    """
    return get_places(query)




