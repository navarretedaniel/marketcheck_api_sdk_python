# coding: utf-8

"""
    Marketcheck Cars API

    <b>Access the New, Used and Certified cars inventories for all Car Dealers in US.</b> <br/>The data is sourced from online listings by over 44,000 Car dealers in US. At any time, there are about 6.2M searchable listings (about 1.9M unique VINs) for Used & Certified cars and about 6.6M (about 3.9M unique VINs) New Car listings from all over US. We use this API at the back for our website <a href='https://www.marketcheck.com' target='_blank'>www.marketcheck.com</a> and our Android and iOS mobile apps too.<br/><h5> Few useful links : </h5><ul><li>A quick view of the API and the use cases is depicated <a href='https://portals.marketcheck.com/mcapi/' target='_blank'>here</a></li><li>The Postman collection with various usages of the API is shared here https://www.getpostman.com/collections/2752684ff636cdd7bac2</li></ul>  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import
from pprint import pprint
import unittest
import pdb
import marketcheck_api_sdk
from marketcheck_api_sdk.api.dealer_api import DealerApi  # noqa: E501
from marketcheck_api_sdk.rest import ApiException


class TestDealerApi(unittest.TestCase):
    """DealerApi unit test stubs"""

    def setUp(self):
        self.api = marketcheck_api_sdk.api.dealer_api.DealerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dealer_search(self):
        """Test case for dealer_search

        Find car dealers around  # noqa: E501
        """
        api_instance = marketcheck_api_sdk.DealerApi(marketcheck_api_sdk.ApiClient())
        lat_lan = [[35, -90], [40, -80], [45, -90]]
        radius = ["20","30","50"]
        properties = [
            {
                "latitude" : 35,
                "longitude": -90,
                "radius" : { 20 : 126,30 : 228,50 : 255 }
            },
            {
                "latitude" : 40,
                "longitude": -80,
                "radius" : { 20 : 25, 30 : 97, 50 : 359 }
            },
            {
                "latitude" : 45,
                "longitude": -90,
                "radius" : { 20 : 3, 30 : 34,50 : 74 }
            },

        ]
        for values in properties:
            latitude = 39.73 # float | Latitude component of location
            longitude = -104.99 # float | Longitude component of location
            radius = 100 # int | Radius around the search location
            api_key = 'YOUR API KEY' # str | The API Authentication Key. Mandatory with all API calls. (optional)
            rows = 20 # float | Number of results to return. Default is 10. Max is 50 (optional)
            start = 0 # float | Offset for the search results. Default is 1. (optional)
            try:
                for radius,dealer_cnt in values["radius"].items():
                    api_response = api_instance.dealer_search(values["latitude"], values["longitude"], radius, api_key=api_key)  #, rows=rows, start=start)
                    #pprint(api_response)
                    #dealers = api_response.dealers
                    limit = 10
                    lower_limit = dealer_cnt - ((limit * dealer_cnt)/100)
                    upper_limit = dealer_cnt + ((limit * dealer_cnt)/100)
                    apis_daeler_cnt = api_response.num_found
                    assert apis_daeler_cnt >= lower_limit
                    assert apis_daeler_cnt <= upper_limit
            except ApiException as e:
                pprint("Exception when calling DealerApi->dealer_search: %s\n" % e)
        pass

    def test_get_dealer(self):
        """Test case for get_dealer

        Dealer by id  # noqa: E501
        """
        api_instance = marketcheck_api_sdk.DealerApi(marketcheck_api_sdk.ApiClient())
        dealer_id = ["1016810","1016017","1016710","1017138","1016732"]
        try:
            for dealer in dealer_id:
                api_response = api_instance.get_dealer(dealer, api_key="YOUR API KEY")
                assert api_response.id == dealer
        except ApiException as e:
            pprint("Exception when calling DealerApi->get_dealer: %s\n" % e)

        pass

    def test_get_dealer_active_inventory(self):
        """Test case for get_dealer_active_inventory

        Dealer inventory  # noqa: E501
        """
        pass

    def test_get_dealer_historical_inventory(self):
        """Test case for get_dealer_historical_inventory

        Dealer's historical inventory  # noqa: E501
        """
        pass

    def test_get_dealer_landing_page(self):
        """Test case for get_dealer_landing_page

        Experimental: Get cached version of dealer landing page by dealer id  # noqa: E501
        """
        pass

    def test_get_dealer_ratings(self):
        """Test case for get_dealer_ratings

        Dealer's Rating  # noqa: E501
        """
        pass

    def test_get_dealer_reviews(self):
        """Test case for get_dealer_reviews

        Dealer's Review  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
