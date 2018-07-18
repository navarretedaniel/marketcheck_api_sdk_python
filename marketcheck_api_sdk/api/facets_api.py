# coding: utf-8

"""
    Marketcheck Cars API

    <b>Access the New, Used and Certified cars inventories for all Car Dealers in US.</b> <br/>The data is sourced from online listings by over 44,000 Car dealers in US. At any time, there are about 6.2M searchable listings (about 1.9M unique VINs) for Used & Certified cars and about 6.6M (about 3.9M unique VINs) New Car listings from all over US. We use this API at the back for our website <a href='https://www.marketcheck.com' target='_blank'>www.marketcheck.com</a> and our Android and iOS mobile apps too.<br/><h5> Few useful links : </h5><ul><li>A quick view of the API and the use cases is depicated <a href='https://portals.marketcheck.com/mcapi/' target='_blank'>here</a></li><li>The Postman collection with various usages of the API is shared here https://www.getpostman.com/collections/2752684ff636cdd7bac2</li></ul>  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from marketcheck_api_sdk.api_client import ApiClient


class FacetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_facets(self, fields, **kwargs):  # noqa: E501
        """Facets  # noqa: E501

        [Merged with the /search API - Please check the 'facets' parameter to the Search API above] Get the facets for the given simple filter criteria (by given VIN's basic specification, Or by Year, Make, Model, Trim criteria) and facet fields  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_facets(fields, async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Comma separated list of fields to generate facets for. Supported fields are - year, make, model, trim, exterior_color, interior_color, drivetrain, vehicle_type, car_type, body_style, body_subtype, doors (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :param str vin: VIN as a reference to the type of car for which facets data is to be returned
        :param str year: Year of the car
        :param str make: Make of the car
        :param str model: Model of the Car
        :param str trim: Trim of the Car
        :return: list[FacetItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_facets_with_http_info(fields, **kwargs)  # noqa: E501
        else:
            (data) = self.get_facets_with_http_info(fields, **kwargs)  # noqa: E501
            return data

    def get_facets_with_http_info(self, fields, **kwargs):  # noqa: E501
        """Facets  # noqa: E501

        [Merged with the /search API - Please check the 'facets' parameter to the Search API above] Get the facets for the given simple filter criteria (by given VIN's basic specification, Or by Year, Make, Model, Trim criteria) and facet fields  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_facets_with_http_info(fields, async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Comma separated list of fields to generate facets for. Supported fields are - year, make, model, trim, exterior_color, interior_color, drivetrain, vehicle_type, car_type, body_style, body_subtype, doors (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :param str vin: VIN as a reference to the type of car for which facets data is to be returned
        :param str year: Year of the car
        :param str make: Make of the car
        :param str model: Model of the Car
        :param str trim: Trim of the Car
        :return: list[FacetItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'api_key', 'vin', 'year', 'make', 'model', 'trim']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_facets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fields' is set
        if ('fields' not in params or
                params['fields'] is None):
            raise ValueError("Missing the required parameter `fields` when calling `get_facets`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))  # noqa: E501
        if 'vin' in params:
            query_params.append(('vin', params['vin']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'make' in params:
            query_params.append(('make', params['make']))  # noqa: E501
        if 'model' in params:
            query_params.append(('model', params['model']))  # noqa: E501
        if 'trim' in params:
            query_params.append(('trim', params['trim']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/facets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FacetItem]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)