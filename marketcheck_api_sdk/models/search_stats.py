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

from marketcheck_api_sdk.models.stats_item import StatsItem  # noqa: F401,E501


class SearchStats(object):
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
        'price': 'StatsItem',
        'miles': 'StatsItem',
        'dom': 'StatsItem',
        'dom_180': 'StatsItem',
        'dom_active': 'StatsItem',
        'msrp': 'StatsItem',
        'lease_term': 'StatsItem',
        'lease_emp': 'StatsItem',
        'lease_down_payment': 'StatsItem',
        'finance_loan_term': 'StatsItem',
        'finance_loan_apr': 'StatsItem',
        'finance_emp': 'StatsItem',
        'finance_down_payment': 'StatsItem',
        'finance_down_payment_per': 'StatsItem'
    }

    attribute_map = {
        'price': 'price',
        'miles': 'miles',
        'dom': 'dom',
        'dom_180': 'dom_180',
        'dom_active': 'dom_active',
        'msrp': 'msrp',
        'lease_term': 'lease_term',
        'lease_emp': 'lease_emp',
        'lease_down_payment': 'lease_down_payment',
        'finance_loan_term': 'finance_loan_term',
        'finance_loan_apr': 'finance_loan_apr',
        'finance_emp': 'finance_emp',
        'finance_down_payment': 'finance_down_payment',
        'finance_down_payment_per': 'finance_down_payment_per'
    }

    def __init__(self, price=None, miles=None, dom=None, dom_180=None, dom_active=None, msrp=None, lease_term=None, lease_emp=None, lease_down_payment=None, finance_loan_term=None, finance_loan_apr=None, finance_emp=None, finance_down_payment=None, finance_down_payment_per=None):  # noqa: E501
        """SearchStats - a model defined in Swagger"""  # noqa: E501

        self._price = None
        self._miles = None
        self._dom = None
        self._dom_180 = None
        self._dom_active = None
        self._msrp = None
        self._lease_term = None
        self._lease_emp = None
        self._lease_down_payment = None
        self._finance_loan_term = None
        self._finance_loan_apr = None
        self._finance_emp = None
        self._finance_down_payment = None
        self._finance_down_payment_per = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if miles is not None:
            self.miles = miles
        if dom is not None:
            self.dom = dom
        if dom_180 is not None:
            self.dom_180 = dom_180
        if dom_active is not None:
            self.dom_active = dom_active
        if msrp is not None:
            self.msrp = msrp
        if lease_term is not None:
            self.lease_term = lease_term
        if lease_emp is not None:
            self.lease_emp = lease_emp
        if lease_down_payment is not None:
            self.lease_down_payment = lease_down_payment
        if finance_loan_term is not None:
            self.finance_loan_term = finance_loan_term
        if finance_loan_apr is not None:
            self.finance_loan_apr = finance_loan_apr
        if finance_emp is not None:
            self.finance_emp = finance_emp
        if finance_down_payment is not None:
            self.finance_down_payment = finance_down_payment
        if finance_down_payment_per is not None:
            self.finance_down_payment_per = finance_down_payment_per

    @property
    def price(self):
        """Gets the price of this SearchStats.  # noqa: E501


        :return: The price of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SearchStats.


        :param price: The price of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._price = price

    @property
    def miles(self):
        """Gets the miles of this SearchStats.  # noqa: E501


        :return: The miles of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._miles

    @miles.setter
    def miles(self, miles):
        """Sets the miles of this SearchStats.


        :param miles: The miles of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._miles = miles

    @property
    def dom(self):
        """Gets the dom of this SearchStats.  # noqa: E501


        :return: The dom of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._dom

    @dom.setter
    def dom(self, dom):
        """Sets the dom of this SearchStats.


        :param dom: The dom of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._dom = dom

    @property
    def dom_180(self):
        """Gets the dom_180 of this SearchStats.  # noqa: E501


        :return: The dom_180 of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._dom_180

    @dom_180.setter
    def dom_180(self, dom_180):
        """Sets the dom_180 of this SearchStats.


        :param dom_180: The dom_180 of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._dom_180 = dom_180

    @property
    def dom_active(self):
        """Gets the dom_active of this SearchStats.  # noqa: E501


        :return: The dom_active of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._dom_active

    @dom_active.setter
    def dom_active(self, dom_active):
        """Sets the dom_active of this SearchStats.


        :param dom_active: The dom_active of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._dom_active = dom_active

    @property
    def msrp(self):
        """Gets the msrp of this SearchStats.  # noqa: E501


        :return: The msrp of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._msrp

    @msrp.setter
    def msrp(self, msrp):
        """Sets the msrp of this SearchStats.


        :param msrp: The msrp of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._msrp = msrp

    @property
    def lease_term(self):
        """Gets the lease_term of this SearchStats.  # noqa: E501


        :return: The lease_term of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._lease_term

    @lease_term.setter
    def lease_term(self, lease_term):
        """Sets the lease_term of this SearchStats.


        :param lease_term: The lease_term of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._lease_term = lease_term

    @property
    def lease_emp(self):
        """Gets the lease_emp of this SearchStats.  # noqa: E501


        :return: The lease_emp of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._lease_emp

    @lease_emp.setter
    def lease_emp(self, lease_emp):
        """Sets the lease_emp of this SearchStats.


        :param lease_emp: The lease_emp of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._lease_emp = lease_emp

    @property
    def lease_down_payment(self):
        """Gets the lease_down_payment of this SearchStats.  # noqa: E501


        :return: The lease_down_payment of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._lease_down_payment

    @lease_down_payment.setter
    def lease_down_payment(self, lease_down_payment):
        """Sets the lease_down_payment of this SearchStats.


        :param lease_down_payment: The lease_down_payment of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._lease_down_payment = lease_down_payment

    @property
    def finance_loan_term(self):
        """Gets the finance_loan_term of this SearchStats.  # noqa: E501


        :return: The finance_loan_term of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._finance_loan_term

    @finance_loan_term.setter
    def finance_loan_term(self, finance_loan_term):
        """Sets the finance_loan_term of this SearchStats.


        :param finance_loan_term: The finance_loan_term of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._finance_loan_term = finance_loan_term

    @property
    def finance_loan_apr(self):
        """Gets the finance_loan_apr of this SearchStats.  # noqa: E501


        :return: The finance_loan_apr of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._finance_loan_apr

    @finance_loan_apr.setter
    def finance_loan_apr(self, finance_loan_apr):
        """Sets the finance_loan_apr of this SearchStats.


        :param finance_loan_apr: The finance_loan_apr of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._finance_loan_apr = finance_loan_apr

    @property
    def finance_emp(self):
        """Gets the finance_emp of this SearchStats.  # noqa: E501


        :return: The finance_emp of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._finance_emp

    @finance_emp.setter
    def finance_emp(self, finance_emp):
        """Sets the finance_emp of this SearchStats.


        :param finance_emp: The finance_emp of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._finance_emp = finance_emp

    @property
    def finance_down_payment(self):
        """Gets the finance_down_payment of this SearchStats.  # noqa: E501


        :return: The finance_down_payment of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._finance_down_payment

    @finance_down_payment.setter
    def finance_down_payment(self, finance_down_payment):
        """Sets the finance_down_payment of this SearchStats.


        :param finance_down_payment: The finance_down_payment of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._finance_down_payment = finance_down_payment

    @property
    def finance_down_payment_per(self):
        """Gets the finance_down_payment_per of this SearchStats.  # noqa: E501


        :return: The finance_down_payment_per of this SearchStats.  # noqa: E501
        :rtype: StatsItem
        """
        return self._finance_down_payment_per

    @finance_down_payment_per.setter
    def finance_down_payment_per(self, finance_down_payment_per):
        """Sets the finance_down_payment_per of this SearchStats.


        :param finance_down_payment_per: The finance_down_payment_per of this SearchStats.  # noqa: E501
        :type: StatsItem
        """

        self._finance_down_payment_per = finance_down_payment_per

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
        if not isinstance(other, SearchStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
