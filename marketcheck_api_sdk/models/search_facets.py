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

from marketcheck_api_sdk.models.facet_item import FacetItem  # noqa: F401,E501


class SearchFacets(object):
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
        'year': 'list[FacetItem]',
        'make': 'list[FacetItem]',
        'model': 'list[FacetItem]',
        'trim': 'list[FacetItem]',
        'trim_o': 'list[FacetItem]',
        'trim_r': 'list[FacetItem]',
        'body_type': 'list[FacetItem]',
        'body_subtype': 'list[FacetItem]',
        'vehicle_type': 'list[FacetItem]',
        'car_type': 'list[FacetItem]',
        'drivetrain': 'list[FacetItem]',
        'transmission': 'list[FacetItem]',
        'cylinders': 'list[FacetItem]',
        'fuel_type': 'list[FacetItem]',
        'exterior_color': 'list[FacetItem]',
        'interior_color': 'list[FacetItem]',
        'city': 'list[FacetItem]',
        'state': 'list[FacetItem]',
        'seller_type': 'list[FacetItem]',
        'doors': 'list[FacetItem]',
        'engine': 'list[FacetItem]',
        'engine_size': 'list[FacetItem]',
        'engine_aspiration': 'list[FacetItem]',
        'engine_block': 'list[FacetItem]',
        'source': 'list[FacetItem]',
        'seller_name_o': 'list[FacetItem]',
        'seller_name': 'list[FacetItem]',
        'dealer_id': 'list[FacetItem]',
        'data_source': 'list[FacetItem]',
        'carfax_1_owner': 'list[FacetItem]',
        'carfax_clean_title': 'list[FacetItem]'
    }

    attribute_map = {
        'year': 'year',
        'make': 'make',
        'model': 'model',
        'trim': 'trim',
        'trim_o': 'trim_o',
        'trim_r': 'trim_r',
        'body_type': 'body_type',
        'body_subtype': 'body_subtype',
        'vehicle_type': 'vehicle_type',
        'car_type': 'car_type',
        'drivetrain': 'drivetrain',
        'transmission': 'transmission',
        'cylinders': 'cylinders',
        'fuel_type': 'fuel_type',
        'exterior_color': 'exterior_color',
        'interior_color': 'interior_color',
        'city': 'city',
        'state': 'state',
        'seller_type': 'seller_type',
        'doors': 'doors',
        'engine': 'engine',
        'engine_size': 'engine_size',
        'engine_aspiration': 'engine_aspiration',
        'engine_block': 'engine_block',
        'source': 'source',
        'seller_name_o': 'seller_name_o',
        'seller_name': 'seller_name',
        'dealer_id': 'dealer_id',
        'data_source': 'data_source',
        'carfax_1_owner': 'carfax_1_owner',
        'carfax_clean_title': 'carfax_clean_title'
    }

    def __init__(self, year=None, make=None, model=None, trim=None, trim_o=None, trim_r=None, body_type=None, body_subtype=None, vehicle_type=None, car_type=None, drivetrain=None, transmission=None, cylinders=None, fuel_type=None, exterior_color=None, interior_color=None, city=None, state=None, seller_type=None, doors=None, engine=None, engine_size=None, engine_aspiration=None, engine_block=None, source=None, seller_name_o=None, seller_name=None, dealer_id=None, data_source=None, carfax_1_owner=None, carfax_clean_title=None):  # noqa: E501
        """SearchFacets - a model defined in Swagger"""  # noqa: E501

        self._year = None
        self._make = None
        self._model = None
        self._trim = None
        self._trim_o = None
        self._trim_r = None
        self._body_type = None
        self._body_subtype = None
        self._vehicle_type = None
        self._car_type = None
        self._drivetrain = None
        self._transmission = None
        self._cylinders = None
        self._fuel_type = None
        self._exterior_color = None
        self._interior_color = None
        self._city = None
        self._state = None
        self._seller_type = None
        self._doors = None
        self._engine = None
        self._engine_size = None
        self._engine_aspiration = None
        self._engine_block = None
        self._source = None
        self._seller_name_o = None
        self._seller_name = None
        self._dealer_id = None
        self._data_source = None
        self._carfax_1_owner = None
        self._carfax_clean_title = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if make is not None:
            self.make = make
        if model is not None:
            self.model = model
        if trim is not None:
            self.trim = trim
        if trim_o is not None:
            self.trim_o = trim_o
        if trim_r is not None:
            self.trim_r = trim_r
        if body_type is not None:
            self.body_type = body_type
        if body_subtype is not None:
            self.body_subtype = body_subtype
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if car_type is not None:
            self.car_type = car_type
        if drivetrain is not None:
            self.drivetrain = drivetrain
        if transmission is not None:
            self.transmission = transmission
        if cylinders is not None:
            self.cylinders = cylinders
        if fuel_type is not None:
            self.fuel_type = fuel_type
        if exterior_color is not None:
            self.exterior_color = exterior_color
        if interior_color is not None:
            self.interior_color = interior_color
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if seller_type is not None:
            self.seller_type = seller_type
        if doors is not None:
            self.doors = doors
        if engine is not None:
            self.engine = engine
        if engine_size is not None:
            self.engine_size = engine_size
        if engine_aspiration is not None:
            self.engine_aspiration = engine_aspiration
        if engine_block is not None:
            self.engine_block = engine_block
        if source is not None:
            self.source = source
        if seller_name_o is not None:
            self.seller_name_o = seller_name_o
        if seller_name is not None:
            self.seller_name = seller_name
        if dealer_id is not None:
            self.dealer_id = dealer_id
        if data_source is not None:
            self.data_source = data_source
        if carfax_1_owner is not None:
            self.carfax_1_owner = carfax_1_owner
        if carfax_clean_title is not None:
            self.carfax_clean_title = carfax_clean_title

    @property
    def year(self):
        """Gets the year of this SearchFacets.  # noqa: E501


        :return: The year of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this SearchFacets.


        :param year: The year of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._year = year

    @property
    def make(self):
        """Gets the make of this SearchFacets.  # noqa: E501


        :return: The make of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this SearchFacets.


        :param make: The make of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._make = make

    @property
    def model(self):
        """Gets the model of this SearchFacets.  # noqa: E501


        :return: The model of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this SearchFacets.


        :param model: The model of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._model = model

    @property
    def trim(self):
        """Gets the trim of this SearchFacets.  # noqa: E501


        :return: The trim of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._trim

    @trim.setter
    def trim(self, trim):
        """Sets the trim of this SearchFacets.


        :param trim: The trim of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._trim = trim

    @property
    def trim_o(self):
        """Gets the trim_o of this SearchFacets.  # noqa: E501


        :return: The trim_o of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._trim_o

    @trim_o.setter
    def trim_o(self, trim_o):
        """Sets the trim_o of this SearchFacets.


        :param trim_o: The trim_o of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._trim_o = trim_o

    @property
    def trim_r(self):
        """Gets the trim_r of this SearchFacets.  # noqa: E501


        :return: The trim_r of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._trim_r

    @trim_r.setter
    def trim_r(self, trim_r):
        """Sets the trim_r of this SearchFacets.


        :param trim_r: The trim_r of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._trim_r = trim_r

    @property
    def body_type(self):
        """Gets the body_type of this SearchFacets.  # noqa: E501


        :return: The body_type of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this SearchFacets.


        :param body_type: The body_type of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._body_type = body_type

    @property
    def body_subtype(self):
        """Gets the body_subtype of this SearchFacets.  # noqa: E501


        :return: The body_subtype of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._body_subtype

    @body_subtype.setter
    def body_subtype(self, body_subtype):
        """Sets the body_subtype of this SearchFacets.


        :param body_subtype: The body_subtype of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._body_subtype = body_subtype

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this SearchFacets.  # noqa: E501


        :return: The vehicle_type of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this SearchFacets.


        :param vehicle_type: The vehicle_type of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._vehicle_type = vehicle_type

    @property
    def car_type(self):
        """Gets the car_type of this SearchFacets.  # noqa: E501


        :return: The car_type of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._car_type

    @car_type.setter
    def car_type(self, car_type):
        """Sets the car_type of this SearchFacets.


        :param car_type: The car_type of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._car_type = car_type

    @property
    def drivetrain(self):
        """Gets the drivetrain of this SearchFacets.  # noqa: E501


        :return: The drivetrain of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._drivetrain

    @drivetrain.setter
    def drivetrain(self, drivetrain):
        """Sets the drivetrain of this SearchFacets.


        :param drivetrain: The drivetrain of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._drivetrain = drivetrain

    @property
    def transmission(self):
        """Gets the transmission of this SearchFacets.  # noqa: E501


        :return: The transmission of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._transmission

    @transmission.setter
    def transmission(self, transmission):
        """Sets the transmission of this SearchFacets.


        :param transmission: The transmission of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._transmission = transmission

    @property
    def cylinders(self):
        """Gets the cylinders of this SearchFacets.  # noqa: E501


        :return: The cylinders of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._cylinders

    @cylinders.setter
    def cylinders(self, cylinders):
        """Sets the cylinders of this SearchFacets.


        :param cylinders: The cylinders of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._cylinders = cylinders

    @property
    def fuel_type(self):
        """Gets the fuel_type of this SearchFacets.  # noqa: E501


        :return: The fuel_type of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        """Sets the fuel_type of this SearchFacets.


        :param fuel_type: The fuel_type of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._fuel_type = fuel_type

    @property
    def exterior_color(self):
        """Gets the exterior_color of this SearchFacets.  # noqa: E501


        :return: The exterior_color of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._exterior_color

    @exterior_color.setter
    def exterior_color(self, exterior_color):
        """Sets the exterior_color of this SearchFacets.


        :param exterior_color: The exterior_color of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._exterior_color = exterior_color

    @property
    def interior_color(self):
        """Gets the interior_color of this SearchFacets.  # noqa: E501


        :return: The interior_color of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._interior_color

    @interior_color.setter
    def interior_color(self, interior_color):
        """Sets the interior_color of this SearchFacets.


        :param interior_color: The interior_color of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._interior_color = interior_color

    @property
    def city(self):
        """Gets the city of this SearchFacets.  # noqa: E501


        :return: The city of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SearchFacets.


        :param city: The city of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this SearchFacets.  # noqa: E501


        :return: The state of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SearchFacets.


        :param state: The state of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._state = state

    @property
    def seller_type(self):
        """Gets the seller_type of this SearchFacets.  # noqa: E501


        :return: The seller_type of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._seller_type

    @seller_type.setter
    def seller_type(self, seller_type):
        """Sets the seller_type of this SearchFacets.


        :param seller_type: The seller_type of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._seller_type = seller_type

    @property
    def doors(self):
        """Gets the doors of this SearchFacets.  # noqa: E501


        :return: The doors of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._doors

    @doors.setter
    def doors(self, doors):
        """Sets the doors of this SearchFacets.


        :param doors: The doors of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._doors = doors

    @property
    def engine(self):
        """Gets the engine of this SearchFacets.  # noqa: E501


        :return: The engine of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this SearchFacets.


        :param engine: The engine of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._engine = engine

    @property
    def engine_size(self):
        """Gets the engine_size of this SearchFacets.  # noqa: E501


        :return: The engine_size of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._engine_size

    @engine_size.setter
    def engine_size(self, engine_size):
        """Sets the engine_size of this SearchFacets.


        :param engine_size: The engine_size of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._engine_size = engine_size

    @property
    def engine_aspiration(self):
        """Gets the engine_aspiration of this SearchFacets.  # noqa: E501


        :return: The engine_aspiration of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._engine_aspiration

    @engine_aspiration.setter
    def engine_aspiration(self, engine_aspiration):
        """Sets the engine_aspiration of this SearchFacets.


        :param engine_aspiration: The engine_aspiration of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._engine_aspiration = engine_aspiration

    @property
    def engine_block(self):
        """Gets the engine_block of this SearchFacets.  # noqa: E501


        :return: The engine_block of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._engine_block

    @engine_block.setter
    def engine_block(self, engine_block):
        """Sets the engine_block of this SearchFacets.


        :param engine_block: The engine_block of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._engine_block = engine_block

    @property
    def source(self):
        """Gets the source of this SearchFacets.  # noqa: E501


        :return: The source of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SearchFacets.


        :param source: The source of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._source = source

    @property
    def seller_name_o(self):
        """Gets the seller_name_o of this SearchFacets.  # noqa: E501


        :return: The seller_name_o of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._seller_name_o

    @seller_name_o.setter
    def seller_name_o(self, seller_name_o):
        """Sets the seller_name_o of this SearchFacets.


        :param seller_name_o: The seller_name_o of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._seller_name_o = seller_name_o

    @property
    def seller_name(self):
        """Gets the seller_name of this SearchFacets.  # noqa: E501


        :return: The seller_name of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._seller_name

    @seller_name.setter
    def seller_name(self, seller_name):
        """Sets the seller_name of this SearchFacets.


        :param seller_name: The seller_name of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._seller_name = seller_name

    @property
    def dealer_id(self):
        """Gets the dealer_id of this SearchFacets.  # noqa: E501


        :return: The dealer_id of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._dealer_id

    @dealer_id.setter
    def dealer_id(self, dealer_id):
        """Sets the dealer_id of this SearchFacets.


        :param dealer_id: The dealer_id of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._dealer_id = dealer_id

    @property
    def data_source(self):
        """Gets the data_source of this SearchFacets.  # noqa: E501


        :return: The data_source of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this SearchFacets.


        :param data_source: The data_source of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._data_source = data_source

    @property
    def carfax_1_owner(self):
        """Gets the carfax_1_owner of this SearchFacets.  # noqa: E501


        :return: The carfax_1_owner of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._carfax_1_owner

    @carfax_1_owner.setter
    def carfax_1_owner(self, carfax_1_owner):
        """Sets the carfax_1_owner of this SearchFacets.


        :param carfax_1_owner: The carfax_1_owner of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._carfax_1_owner = carfax_1_owner

    @property
    def carfax_clean_title(self):
        """Gets the carfax_clean_title of this SearchFacets.  # noqa: E501


        :return: The carfax_clean_title of this SearchFacets.  # noqa: E501
        :rtype: list[FacetItem]
        """
        return self._carfax_clean_title

    @carfax_clean_title.setter
    def carfax_clean_title(self, carfax_clean_title):
        """Sets the carfax_clean_title of this SearchFacets.


        :param carfax_clean_title: The carfax_clean_title of this SearchFacets.  # noqa: E501
        :type: list[FacetItem]
        """

        self._carfax_clean_title = carfax_clean_title

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
        if not isinstance(other, SearchFacets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
