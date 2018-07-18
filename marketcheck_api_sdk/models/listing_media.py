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


class ListingMedia(object):
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
        'photo_url': 'str',
        'photo_links': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'photo_url': 'photo_url',
        'photo_links': 'photo_links'
    }

    def __init__(self, id=None, photo_url=None, photo_links=None):  # noqa: E501
        """ListingMedia - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._photo_url = None
        self._photo_links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if photo_url is not None:
            self.photo_url = photo_url
        if photo_links is not None:
            self.photo_links = photo_links

    @property
    def id(self):
        """Gets the id of this ListingMedia.  # noqa: E501

        Unique identifier representing a specific listing from the Marketcheck database  # noqa: E501

        :return: The id of this ListingMedia.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListingMedia.

        Unique identifier representing a specific listing from the Marketcheck database  # noqa: E501

        :param id: The id of this ListingMedia.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def photo_url(self):
        """Gets the photo_url of this ListingMedia.  # noqa: E501

        Single photo url of the car  # noqa: E501

        :return: The photo_url of this ListingMedia.  # noqa: E501
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """Sets the photo_url of this ListingMedia.

        Single photo url of the car  # noqa: E501

        :param photo_url: The photo_url of this ListingMedia.  # noqa: E501
        :type: str
        """

        self._photo_url = photo_url

    @property
    def photo_links(self):
        """Gets the photo_links of this ListingMedia.  # noqa: E501

        A list of photo urls for the car  # noqa: E501

        :return: The photo_links of this ListingMedia.  # noqa: E501
        :rtype: list[str]
        """
        return self._photo_links

    @photo_links.setter
    def photo_links(self, photo_links):
        """Sets the photo_links of this ListingMedia.

        A list of photo urls for the car  # noqa: E501

        :param photo_links: The photo_links of this ListingMedia.  # noqa: E501
        :type: list[str]
        """

        self._photo_links = photo_links

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
        if not isinstance(other, ListingMedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
