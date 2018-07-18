# coding: utf-8

"""
    Marketcheck Cars API

    <b>Access the New, Used and Certified cars inventories for all Car Dealers in US.</b> <br/>The data is sourced from online listings by over 44,000 Car dealers in US. At any time, there are about 6.2M searchable listings (about 1.9M unique VINs) for Used & Certified cars and about 6.6M (about 3.9M unique VINs) New Car listings from all over US. We use this API at the back for our website <a href='https://www.marketcheck.com' target='_blank'>www.marketcheck.com</a> and our Android and iOS mobile apps too.<br/><h5> Few useful links : </h5><ul><li>A quick view of the API and the use cases is depicated <a href='https://portals.marketcheck.com/mcapi/' target='_blank'>here</a></li><li>The Postman collection with various usages of the API is shared here https://www.getpostman.com/collections/2752684ff636cdd7bac2</li></ul>  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import marketcheck_api_sdk
from marketcheck_api_sdk.models.plot_point import PlotPoint  # noqa: E501
from marketcheck_api_sdk.rest import ApiException


class TestPlotPoint(unittest.TestCase):
    """PlotPoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlotPoint(self):
        """Test PlotPoint"""
        # FIXME: construct object with mandatory attributes with example values
        # model = marketcheck_api_sdk.models.plot_point.PlotPoint()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
