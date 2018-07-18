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


class VinReport(object):
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
        'icon': 'str',
        'some_text': 'str'
    }

    attribute_map = {
        'icon': 'icon',
        'some_text': 'some_text'
    }

    def __init__(self, icon=None, some_text=None):  # noqa: E501
        """VinReport - a model defined in Swagger"""  # noqa: E501

        self._icon = None
        self._some_text = None
        self.discriminator = None

        if icon is not None:
            self.icon = icon
        if some_text is not None:
            self.some_text = some_text

    @property
    def icon(self):
        """Gets the icon of this VinReport.  # noqa: E501

        icon url  # noqa: E501

        :return: The icon of this VinReport.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this VinReport.

        icon url  # noqa: E501

        :param icon: The icon of this VinReport.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def some_text(self):
        """Gets the some_text of this VinReport.  # noqa: E501

        Some descriptional text  # noqa: E501

        :return: The some_text of this VinReport.  # noqa: E501
        :rtype: str
        """
        return self._some_text

    @some_text.setter
    def some_text(self, some_text):
        """Sets the some_text of this VinReport.

        Some descriptional text  # noqa: E501

        :param some_text: The some_text of this VinReport.  # noqa: E501
        :type: str
        """

        self._some_text = some_text

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
        if not isinstance(other, VinReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
