# coding: utf-8

"""
    Marketcheck Cars API

    <b>Access the New, Used and Certified cars inventories for all Car Dealers in US.</b> <br/>The data is sourced from online listings by over 44,000 Car dealers in US. At any time, there are about 6.2M searchable listings (about 1.9M unique VINs) for Used & Certified cars and about 6.6M (about 3.9M unique VINs) New Car listings from all over US. We use this API at the back for our website <a href='https://www.marketcheck.com' target='_blank'>www.marketcheck.com</a> and our Android and iOS mobile apps too.<br/><h5> Few useful links : </h5><ul><li>A quick view of the API and the use cases is depicated <a href='https://portals.marketcheck.com/mcapi/' target='_blank'>here</a></li><li>The Postman collection with various usages of the API is shared here https://www.getpostman.com/collections/2752684ff636cdd7bac2</li></ul>  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from marketcheck_api_sdk.models.build import Build  # noqa: F401,E501
from marketcheck_api_sdk.models.listing_finance import ListingFinance  # noqa: F401,E501
from marketcheck_api_sdk.models.listing_lease import ListingLease  # noqa: F401,E501
from marketcheck_api_sdk.models.listing_nest_media import ListingNestMedia  # noqa: F401,E501
from marketcheck_api_sdk.models.nest_dealer import NestDealer  # noqa: F401,E501


class BaseListing(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'vin': 'str',
        'heading': 'str',
        'price': 'int',
        'miles': 'int',
        'msrp': 'int',
        'data_source': 'str',
        'is_certified': 'int',
        'vdp_url': 'str',
        'carfax_1_owner': 'bool',
        'carfax_clean_title': 'bool',
        'exterior_color': 'str',
        'interior_color': 'str',
        'dom': 'int',
        'dom_180': 'int',
        'dom_active': 'int',
        'seller_type': 'str',
        'inventory_type': 'str',
        'stock_no': 'str',
        'last_seen_at': 'int',
        'last_seen_at_date': 'str',
        'scraped_at': 'float',
        'scraped_at_date': 'str',
        'first_seen_at': 'int',
        'first_seen_at_date': 'str',
        'ref_price': 'str',
        'ref_price_dt': 'int',
        'ref_miles': 'str',
        'ref_miles_dt': 'int',
        'source': 'str',
        'financing_options': 'list[ListingFinance]',
        'leasing_options': 'list[ListingLease]',
        'media': 'ListingNestMedia',
        'dealer': 'NestDealer',
        'build': 'Build',
        'distance': 'float'
    }

    attribute_map = {
        'id': 'id',
        'vin': 'vin',
        'heading': 'heading',
        'price': 'price',
        'miles': 'miles',
        'msrp': 'msrp',
        'data_source': 'data_source',
        'is_certified': 'is_certified',
        'vdp_url': 'vdp_url',
        'carfax_1_owner': 'carfax_1_owner',
        'carfax_clean_title': 'carfax_clean_title',
        'exterior_color': 'exterior_color',
        'interior_color': 'interior_color',
        'dom': 'dom',
        'dom_180': 'dom_180',
        'dom_active': 'dom_active',
        'seller_type': 'seller_type',
        'inventory_type': 'inventory_type',
        'stock_no': 'stock_no',
        'last_seen_at': 'last_seen_at',
        'last_seen_at_date': 'last_seen_at_date',
        'scraped_at': 'scraped_at',
        'scraped_at_date': 'scraped_at_date',
        'first_seen_at': 'first_seen_at',
        'first_seen_at_date': 'first_seen_at_date',
        'ref_price': 'ref_price',
        'ref_price_dt': 'ref_price_dt',
        'ref_miles': 'ref_miles',
        'ref_miles_dt': 'ref_miles_dt',
        'source': 'source',
        'financing_options': 'financing_options',
        'leasing_options': 'leasing_options',
        'media': 'media',
        'dealer': 'dealer',
        'build': 'build',
        'distance': 'distance'
    }

    def __init__(self, id=None, vin=None, heading=None, price=None, miles=None, msrp=None, data_source=None, is_certified=None, vdp_url=None, carfax_1_owner=None, carfax_clean_title=None, exterior_color=None, interior_color=None, dom=None, dom_180=None, dom_active=None, seller_type=None, inventory_type=None, stock_no=None, last_seen_at=None, last_seen_at_date=None, scraped_at=None, scraped_at_date=None, first_seen_at=None, first_seen_at_date=None, ref_price=None, ref_price_dt=None, ref_miles=None, ref_miles_dt=None, source=None, financing_options=None, leasing_options=None, media=None, dealer=None, build=None, distance=None):  # noqa: E501
        """BaseListing - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._vin = None
        self._heading = None
        self._price = None
        self._miles = None
        self._msrp = None
        self._data_source = None
        self._is_certified = None
        self._vdp_url = None
        self._carfax_1_owner = None
        self._carfax_clean_title = None
        self._exterior_color = None
        self._interior_color = None
        self._dom = None
        self._dom_180 = None
        self._dom_active = None
        self._seller_type = None
        self._inventory_type = None
        self._stock_no = None
        self._last_seen_at = None
        self._last_seen_at_date = None
        self._scraped_at = None
        self._scraped_at_date = None
        self._first_seen_at = None
        self._first_seen_at_date = None
        self._ref_price = None
        self._ref_price_dt = None
        self._ref_miles = None
        self._ref_miles_dt = None
        self._source = None
        self._financing_options = None
        self._leasing_options = None
        self._media = None
        self._dealer = None
        self._build = None
        self._distance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vin is not None:
            self.vin = vin
        if heading is not None:
            self.heading = heading
        if price is not None:
            self.price = price
        if miles is not None:
            self.miles = miles
        if msrp is not None:
            self.msrp = msrp
        if data_source is not None:
            self.data_source = data_source
        if is_certified is not None:
            self.is_certified = is_certified
        if vdp_url is not None:
            self.vdp_url = vdp_url
        if carfax_1_owner is not None:
            self.carfax_1_owner = carfax_1_owner
        if carfax_clean_title is not None:
            self.carfax_clean_title = carfax_clean_title
        if exterior_color is not None:
            self.exterior_color = exterior_color
        if interior_color is not None:
            self.interior_color = interior_color
        if dom is not None:
            self.dom = dom
        if dom_180 is not None:
            self.dom_180 = dom_180
        if dom_active is not None:
            self.dom_active = dom_active
        if seller_type is not None:
            self.seller_type = seller_type
        if inventory_type is not None:
            self.inventory_type = inventory_type
        if stock_no is not None:
            self.stock_no = stock_no
        if last_seen_at is not None:
            self.last_seen_at = last_seen_at
        if last_seen_at_date is not None:
            self.last_seen_at_date = last_seen_at_date
        if scraped_at is not None:
            self.scraped_at = scraped_at
        if scraped_at_date is not None:
            self.scraped_at_date = scraped_at_date
        if first_seen_at is not None:
            self.first_seen_at = first_seen_at
        if first_seen_at_date is not None:
            self.first_seen_at_date = first_seen_at_date
        if ref_price is not None:
            self.ref_price = ref_price
        if ref_price_dt is not None:
            self.ref_price_dt = ref_price_dt
        if ref_miles is not None:
            self.ref_miles = ref_miles
        if ref_miles_dt is not None:
            self.ref_miles_dt = ref_miles_dt
        if source is not None:
            self.source = source
        if financing_options is not None:
            self.financing_options = financing_options
        if leasing_options is not None:
            self.leasing_options = leasing_options
        if media is not None:
            self.media = media
        if dealer is not None:
            self.dealer = dealer
        if build is not None:
            self.build = build
        if distance is not None:
            self.distance = distance

    @property
    def id(self):
        """Gets the id of this BaseListing.  # noqa: E501

        Unique identifier representing a specific listing from the Marketcheck database  # noqa: E501

        :return: The id of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseListing.

        Unique identifier representing a specific listing from the Marketcheck database  # noqa: E501

        :param id: The id of this BaseListing.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def vin(self):
        """Gets the vin of this BaseListing.  # noqa: E501

        VIN for the car  # noqa: E501

        :return: The vin of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this BaseListing.

        VIN for the car  # noqa: E501

        :param vin: The vin of this BaseListing.  # noqa: E501
        :type: str
        """

        self._vin = vin

    @property
    def heading(self):
        """Gets the heading of this BaseListing.  # noqa: E501

        Listing title as displayed on the source website  # noqa: E501

        :return: The heading of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._heading

    @heading.setter
    def heading(self, heading):
        """Sets the heading of this BaseListing.

        Listing title as displayed on the source website  # noqa: E501

        :param heading: The heading of this BaseListing.  # noqa: E501
        :type: str
        """

        self._heading = heading

    @property
    def price(self):
        """Gets the price of this BaseListing.  # noqa: E501

        Asking price for the car  # noqa: E501

        :return: The price of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BaseListing.

        Asking price for the car  # noqa: E501

        :param price: The price of this BaseListing.  # noqa: E501
        :type: int
        """

        self._price = price

    @property
    def miles(self):
        """Gets the miles of this BaseListing.  # noqa: E501

        Odometer reading / reported miles usage for the car  # noqa: E501

        :return: The miles of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._miles

    @miles.setter
    def miles(self, miles):
        """Sets the miles of this BaseListing.

        Odometer reading / reported miles usage for the car  # noqa: E501

        :param miles: The miles of this BaseListing.  # noqa: E501
        :type: int
        """

        self._miles = miles

    @property
    def msrp(self):
        """Gets the msrp of this BaseListing.  # noqa: E501

        MSRP for the car  # noqa: E501

        :return: The msrp of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._msrp

    @msrp.setter
    def msrp(self, msrp):
        """Sets the msrp of this BaseListing.

        MSRP for the car  # noqa: E501

        :param msrp: The msrp of this BaseListing.  # noqa: E501
        :type: int
        """

        self._msrp = msrp

    @property
    def data_source(self):
        """Gets the data_source of this BaseListing.  # noqa: E501

        Data source of the listing  # noqa: E501

        :return: The data_source of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this BaseListing.

        Data source of the listing  # noqa: E501

        :param data_source: The data_source of this BaseListing.  # noqa: E501
        :type: str
        """

        self._data_source = data_source

    @property
    def is_certified(self):
        """Gets the is_certified of this BaseListing.  # noqa: E501

        Certified car  # noqa: E501

        :return: The is_certified of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._is_certified

    @is_certified.setter
    def is_certified(self, is_certified):
        """Sets the is_certified of this BaseListing.

        Certified car  # noqa: E501

        :param is_certified: The is_certified of this BaseListing.  # noqa: E501
        :type: int
        """

        self._is_certified = is_certified

    @property
    def vdp_url(self):
        """Gets the vdp_url of this BaseListing.  # noqa: E501

        Vehicle Details Page url of the specific car  # noqa: E501

        :return: The vdp_url of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._vdp_url

    @vdp_url.setter
    def vdp_url(self, vdp_url):
        """Sets the vdp_url of this BaseListing.

        Vehicle Details Page url of the specific car  # noqa: E501

        :param vdp_url: The vdp_url of this BaseListing.  # noqa: E501
        :type: str
        """

        self._vdp_url = vdp_url

    @property
    def carfax_1_owner(self):
        """Gets the carfax_1_owner of this BaseListing.  # noqa: E501

        Flag to indicate whether listing is carfax_1_owner  # noqa: E501

        :return: The carfax_1_owner of this BaseListing.  # noqa: E501
        :rtype: bool
        """
        return self._carfax_1_owner

    @carfax_1_owner.setter
    def carfax_1_owner(self, carfax_1_owner):
        """Sets the carfax_1_owner of this BaseListing.

        Flag to indicate whether listing is carfax_1_owner  # noqa: E501

        :param carfax_1_owner: The carfax_1_owner of this BaseListing.  # noqa: E501
        :type: bool
        """

        self._carfax_1_owner = carfax_1_owner

    @property
    def carfax_clean_title(self):
        """Gets the carfax_clean_title of this BaseListing.  # noqa: E501

        Flag to indicate whether listing is carfax_clean_title  # noqa: E501

        :return: The carfax_clean_title of this BaseListing.  # noqa: E501
        :rtype: bool
        """
        return self._carfax_clean_title

    @carfax_clean_title.setter
    def carfax_clean_title(self, carfax_clean_title):
        """Sets the carfax_clean_title of this BaseListing.

        Flag to indicate whether listing is carfax_clean_title  # noqa: E501

        :param carfax_clean_title: The carfax_clean_title of this BaseListing.  # noqa: E501
        :type: bool
        """

        self._carfax_clean_title = carfax_clean_title

    @property
    def exterior_color(self):
        """Gets the exterior_color of this BaseListing.  # noqa: E501

        Exterior color of the car  # noqa: E501

        :return: The exterior_color of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._exterior_color

    @exterior_color.setter
    def exterior_color(self, exterior_color):
        """Sets the exterior_color of this BaseListing.

        Exterior color of the car  # noqa: E501

        :param exterior_color: The exterior_color of this BaseListing.  # noqa: E501
        :type: str
        """

        self._exterior_color = exterior_color

    @property
    def interior_color(self):
        """Gets the interior_color of this BaseListing.  # noqa: E501

        Interior color of the car  # noqa: E501

        :return: The interior_color of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._interior_color

    @interior_color.setter
    def interior_color(self, interior_color):
        """Sets the interior_color of this BaseListing.

        Interior color of the car  # noqa: E501

        :param interior_color: The interior_color of this BaseListing.  # noqa: E501
        :type: str
        """

        self._interior_color = interior_color

    @property
    def dom(self):
        """Gets the dom of this BaseListing.  # noqa: E501

        Days on Market value for the car based on current and historical listings found in the Marketcheck database for this car  # noqa: E501

        :return: The dom of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._dom

    @dom.setter
    def dom(self, dom):
        """Sets the dom of this BaseListing.

        Days on Market value for the car based on current and historical listings found in the Marketcheck database for this car  # noqa: E501

        :param dom: The dom of this BaseListing.  # noqa: E501
        :type: int
        """

        self._dom = dom

    @property
    def dom_180(self):
        """Gets the dom_180 of this BaseListing.  # noqa: E501

        Days on Market value for the car based on current and last 6 month listings found in the Marketcheck database for this car  # noqa: E501

        :return: The dom_180 of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._dom_180

    @dom_180.setter
    def dom_180(self, dom_180):
        """Sets the dom_180 of this BaseListing.

        Days on Market value for the car based on current and last 6 month listings found in the Marketcheck database for this car  # noqa: E501

        :param dom_180: The dom_180 of this BaseListing.  # noqa: E501
        :type: int
        """

        self._dom_180 = dom_180

    @property
    def dom_active(self):
        """Gets the dom_active of this BaseListing.  # noqa: E501

        Days on Market value for the car based on current and last 30 days listings found in the Marketcheck database for this car  # noqa: E501

        :return: The dom_active of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._dom_active

    @dom_active.setter
    def dom_active(self, dom_active):
        """Sets the dom_active of this BaseListing.

        Days on Market value for the car based on current and last 30 days listings found in the Marketcheck database for this car  # noqa: E501

        :param dom_active: The dom_active of this BaseListing.  # noqa: E501
        :type: int
        """

        self._dom_active = dom_active

    @property
    def seller_type(self):
        """Gets the seller_type of this BaseListing.  # noqa: E501

        Seller type for the car  # noqa: E501

        :return: The seller_type of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._seller_type

    @seller_type.setter
    def seller_type(self, seller_type):
        """Sets the seller_type of this BaseListing.

        Seller type for the car  # noqa: E501

        :param seller_type: The seller_type of this BaseListing.  # noqa: E501
        :type: str
        """

        self._seller_type = seller_type

    @property
    def inventory_type(self):
        """Gets the inventory_type of this BaseListing.  # noqa: E501

        Inventory type of car  # noqa: E501

        :return: The inventory_type of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._inventory_type

    @inventory_type.setter
    def inventory_type(self, inventory_type):
        """Sets the inventory_type of this BaseListing.

        Inventory type of car  # noqa: E501

        :param inventory_type: The inventory_type of this BaseListing.  # noqa: E501
        :type: str
        """

        self._inventory_type = inventory_type

    @property
    def stock_no(self):
        """Gets the stock_no of this BaseListing.  # noqa: E501

        Stock number of car in dealers inventory  # noqa: E501

        :return: The stock_no of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._stock_no

    @stock_no.setter
    def stock_no(self, stock_no):
        """Sets the stock_no of this BaseListing.

        Stock number of car in dealers inventory  # noqa: E501

        :param stock_no: The stock_no of this BaseListing.  # noqa: E501
        :type: str
        """

        self._stock_no = stock_no

    @property
    def last_seen_at(self):
        """Gets the last_seen_at of this BaseListing.  # noqa: E501

        Listing last seen at (most recent) timestamp  # noqa: E501

        :return: The last_seen_at of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._last_seen_at

    @last_seen_at.setter
    def last_seen_at(self, last_seen_at):
        """Sets the last_seen_at of this BaseListing.

        Listing last seen at (most recent) timestamp  # noqa: E501

        :param last_seen_at: The last_seen_at of this BaseListing.  # noqa: E501
        :type: int
        """

        self._last_seen_at = last_seen_at

    @property
    def last_seen_at_date(self):
        """Gets the last_seen_at_date of this BaseListing.  # noqa: E501

        Listing last seen at (most recent) date  # noqa: E501

        :return: The last_seen_at_date of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._last_seen_at_date

    @last_seen_at_date.setter
    def last_seen_at_date(self, last_seen_at_date):
        """Sets the last_seen_at_date of this BaseListing.

        Listing last seen at (most recent) date  # noqa: E501

        :param last_seen_at_date: The last_seen_at_date of this BaseListing.  # noqa: E501
        :type: str
        """

        self._last_seen_at_date = last_seen_at_date

    @property
    def scraped_at(self):
        """Gets the scraped_at of this BaseListing.  # noqa: E501

        Listing last seen at date timestamp  # noqa: E501

        :return: The scraped_at of this BaseListing.  # noqa: E501
        :rtype: float
        """
        return self._scraped_at

    @scraped_at.setter
    def scraped_at(self, scraped_at):
        """Sets the scraped_at of this BaseListing.

        Listing last seen at date timestamp  # noqa: E501

        :param scraped_at: The scraped_at of this BaseListing.  # noqa: E501
        :type: float
        """

        self._scraped_at = scraped_at

    @property
    def scraped_at_date(self):
        """Gets the scraped_at_date of this BaseListing.  # noqa: E501

        Listing last seen at date  # noqa: E501

        :return: The scraped_at_date of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._scraped_at_date

    @scraped_at_date.setter
    def scraped_at_date(self, scraped_at_date):
        """Sets the scraped_at_date of this BaseListing.

        Listing last seen at date  # noqa: E501

        :param scraped_at_date: The scraped_at_date of this BaseListing.  # noqa: E501
        :type: str
        """

        self._scraped_at_date = scraped_at_date

    @property
    def first_seen_at(self):
        """Gets the first_seen_at of this BaseListing.  # noqa: E501

        Listing first seen at first scraped timestamp  # noqa: E501

        :return: The first_seen_at of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._first_seen_at

    @first_seen_at.setter
    def first_seen_at(self, first_seen_at):
        """Sets the first_seen_at of this BaseListing.

        Listing first seen at first scraped timestamp  # noqa: E501

        :param first_seen_at: The first_seen_at of this BaseListing.  # noqa: E501
        :type: int
        """

        self._first_seen_at = first_seen_at

    @property
    def first_seen_at_date(self):
        """Gets the first_seen_at_date of this BaseListing.  # noqa: E501

        Listing first seen at first scraped date  # noqa: E501

        :return: The first_seen_at_date of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._first_seen_at_date

    @first_seen_at_date.setter
    def first_seen_at_date(self, first_seen_at_date):
        """Sets the first_seen_at_date of this BaseListing.

        Listing first seen at first scraped date  # noqa: E501

        :param first_seen_at_date: The first_seen_at_date of this BaseListing.  # noqa: E501
        :type: str
        """

        self._first_seen_at_date = first_seen_at_date

    @property
    def ref_price(self):
        """Gets the ref_price of this BaseListing.  # noqa: E501

        Last reported price for the car. If the asking price value is not or is available then the last_price could perhaps be used. last_price is the price for the car listed on the source website as of last_price_dt date  # noqa: E501

        :return: The ref_price of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._ref_price

    @ref_price.setter
    def ref_price(self, ref_price):
        """Sets the ref_price of this BaseListing.

        Last reported price for the car. If the asking price value is not or is available then the last_price could perhaps be used. last_price is the price for the car listed on the source website as of last_price_dt date  # noqa: E501

        :param ref_price: The ref_price of this BaseListing.  # noqa: E501
        :type: str
        """

        self._ref_price = ref_price

    @property
    def ref_price_dt(self):
        """Gets the ref_price_dt of this BaseListing.  # noqa: E501

        The date at which the last price was reported online. This is earlier to last_seen_date  # noqa: E501

        :return: The ref_price_dt of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._ref_price_dt

    @ref_price_dt.setter
    def ref_price_dt(self, ref_price_dt):
        """Sets the ref_price_dt of this BaseListing.

        The date at which the last price was reported online. This is earlier to last_seen_date  # noqa: E501

        :param ref_price_dt: The ref_price_dt of this BaseListing.  # noqa: E501
        :type: int
        """

        self._ref_price_dt = ref_price_dt

    @property
    def ref_miles(self):
        """Gets the ref_miles of this BaseListing.  # noqa: E501

        Last Odometer reading / reported miles usage for the car. If the asking miles value is not or is available then the last_miles could perhaps be used. last_miles is the miles for the car listed on the source website as of last_miles_dt date  # noqa: E501

        :return: The ref_miles of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._ref_miles

    @ref_miles.setter
    def ref_miles(self, ref_miles):
        """Sets the ref_miles of this BaseListing.

        Last Odometer reading / reported miles usage for the car. If the asking miles value is not or is available then the last_miles could perhaps be used. last_miles is the miles for the car listed on the source website as of last_miles_dt date  # noqa: E501

        :param ref_miles: The ref_miles of this BaseListing.  # noqa: E501
        :type: str
        """

        self._ref_miles = ref_miles

    @property
    def ref_miles_dt(self):
        """Gets the ref_miles_dt of this BaseListing.  # noqa: E501

        The date at which the last miles was reported online. This is earlier to last_seen_date  # noqa: E501

        :return: The ref_miles_dt of this BaseListing.  # noqa: E501
        :rtype: int
        """
        return self._ref_miles_dt

    @ref_miles_dt.setter
    def ref_miles_dt(self, ref_miles_dt):
        """Sets the ref_miles_dt of this BaseListing.

        The date at which the last miles was reported online. This is earlier to last_seen_date  # noqa: E501

        :param ref_miles_dt: The ref_miles_dt of this BaseListing.  # noqa: E501
        :type: int
        """

        self._ref_miles_dt = ref_miles_dt

    @property
    def source(self):
        """Gets the source of this BaseListing.  # noqa: E501

        Source domain of the listing  # noqa: E501

        :return: The source of this BaseListing.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BaseListing.

        Source domain of the listing  # noqa: E501

        :param source: The source of this BaseListing.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def financing_options(self):
        """Gets the financing_options of this BaseListing.  # noqa: E501

        Array of all finance offers for this listing  # noqa: E501

        :return: The financing_options of this BaseListing.  # noqa: E501
        :rtype: list[ListingFinance]
        """
        return self._financing_options

    @financing_options.setter
    def financing_options(self, financing_options):
        """Sets the financing_options of this BaseListing.

        Array of all finance offers for this listing  # noqa: E501

        :param financing_options: The financing_options of this BaseListing.  # noqa: E501
        :type: list[ListingFinance]
        """

        self._financing_options = financing_options

    @property
    def leasing_options(self):
        """Gets the leasing_options of this BaseListing.  # noqa: E501

        Array of all finance offers for this listing  # noqa: E501

        :return: The leasing_options of this BaseListing.  # noqa: E501
        :rtype: list[ListingLease]
        """
        return self._leasing_options

    @leasing_options.setter
    def leasing_options(self, leasing_options):
        """Sets the leasing_options of this BaseListing.

        Array of all finance offers for this listing  # noqa: E501

        :param leasing_options: The leasing_options of this BaseListing.  # noqa: E501
        :type: list[ListingLease]
        """

        self._leasing_options = leasing_options

    @property
    def media(self):
        """Gets the media of this BaseListing.  # noqa: E501

        Car Media Attributes - main photo link/url and photo links  # noqa: E501

        :return: The media of this BaseListing.  # noqa: E501
        :rtype: ListingNestMedia
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this BaseListing.

        Car Media Attributes - main photo link/url and photo links  # noqa: E501

        :param media: The media of this BaseListing.  # noqa: E501
        :type: ListingNestMedia
        """

        self._media = media

    @property
    def dealer(self):
        """Gets the dealer of this BaseListing.  # noqa: E501

        Dealer details of listing  # noqa: E501

        :return: The dealer of this BaseListing.  # noqa: E501
        :rtype: NestDealer
        """
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        """Sets the dealer of this BaseListing.

        Dealer details of listing  # noqa: E501

        :param dealer: The dealer of this BaseListing.  # noqa: E501
        :type: NestDealer
        """

        self._dealer = dealer

    @property
    def build(self):
        """Gets the build of this BaseListing.  # noqa: E501


        :return: The build of this BaseListing.  # noqa: E501
        :rtype: Build
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this BaseListing.


        :param build: The build of this BaseListing.  # noqa: E501
        :type: Build
        """

        self._build = build

    @property
    def distance(self):
        """Gets the distance of this BaseListing.  # noqa: E501

        Distance of the car's location from the specified user lcoation  # noqa: E501

        :return: The distance of this BaseListing.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this BaseListing.

        Distance of the car's location from the specified user lcoation  # noqa: E501

        :param distance: The distance of this BaseListing.  # noqa: E501
        :type: float
        """

        self._distance = distance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BaseListing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
