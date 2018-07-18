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


class DealerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dealer_search(self, latitude, longitude, radius, **kwargs):  # noqa: E501
        """Find car dealers around  # noqa: E501

        The dealers API returns a list of dealers around a given point and radius.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.dealer_search(latitude, longitude, radius, async=True)
        >>> result = thread.get()

        :param async bool
        :param float latitude: Latitude component of location (required)
        :param float longitude: Longitude component of location (required)
        :param int radius: Radius around the search location (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :param float rows: Number of results to return. Default is 10. Max is 50
        :param float start: Offset for the search results. Default is 1.
        :return: DealersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.dealer_search_with_http_info(latitude, longitude, radius, **kwargs)  # noqa: E501
        else:
            (data) = self.dealer_search_with_http_info(latitude, longitude, radius, **kwargs)  # noqa: E501
            return data

    def dealer_search_with_http_info(self, latitude, longitude, radius, **kwargs):  # noqa: E501
        """Find car dealers around  # noqa: E501

        The dealers API returns a list of dealers around a given point and radius.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.dealer_search_with_http_info(latitude, longitude, radius, async=True)
        >>> result = thread.get()

        :param async bool
        :param float latitude: Latitude component of location (required)
        :param float longitude: Longitude component of location (required)
        :param int radius: Radius around the search location (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :param float rows: Number of results to return. Default is 10. Max is 50
        :param float start: Offset for the search results. Default is 1.
        :return: DealersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['latitude', 'longitude', 'radius', 'api_key', 'rows', 'start']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dealer_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'latitude' is set
        if ('latitude' not in params or
                params['latitude'] is None):
            raise ValueError("Missing the required parameter `latitude` when calling `dealer_search`")  # noqa: E501
        # verify the required parameter 'longitude' is set
        if ('longitude' not in params or
                params['longitude'] is None):
            raise ValueError("Missing the required parameter `longitude` when calling `dealer_search`")  # noqa: E501
        # verify the required parameter 'radius' is set
        if ('radius' not in params or
                params['radius'] is None):
            raise ValueError("Missing the required parameter `radius` when calling `dealer_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))  # noqa: E501
        if 'latitude' in params:
            query_params.append(('latitude', params['latitude']))  # noqa: E501
        if 'longitude' in params:
            query_params.append(('longitude', params['longitude']))  # noqa: E501
        if 'radius' in params:
            query_params.append(('radius', params['radius']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501

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
            '/dealers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DealersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dealer(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer by id  # noqa: E501

        Get a particular dealer's information by its id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Dealer id to get all the dealer info attributes (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :return: Dealer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dealer_with_http_info(dealer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dealer_with_http_info(dealer_id, **kwargs)  # noqa: E501
            return data

    def get_dealer_with_http_info(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer by id  # noqa: E501

        Get a particular dealer's information by its id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_with_http_info(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Dealer id to get all the dealer info attributes (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :return: Dealer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dealer_id', 'api_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dealer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dealer_id' is set
        if ('dealer_id' not in params or
                params['dealer_id'] is None):
            raise ValueError("Missing the required parameter `dealer_id` when calling `get_dealer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dealer_id' in params:
            path_params['dealer_id'] = params['dealer_id']  # noqa: E501

        query_params = []
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))  # noqa: E501

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
            '/dealer/{dealer_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dealer',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dealer_active_inventory(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer inventory  # noqa: E501

        Get a dealer's currently active inventory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_active_inventory(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Id representing the dealer to fetch the active inventory for (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :param str rows: Number of results to return. Default is 10. Max is 50
        :param str start: Page number to fetch the results for the given criteria. Default is 1. Pagination is allowed only till first 1000 results for the search and sort criteria. The page value can be only between 1 to 1000/rows
        :return: BaseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dealer_active_inventory_with_http_info(dealer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dealer_active_inventory_with_http_info(dealer_id, **kwargs)  # noqa: E501
            return data

    def get_dealer_active_inventory_with_http_info(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer inventory  # noqa: E501

        Get a dealer's currently active inventory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_active_inventory_with_http_info(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Id representing the dealer to fetch the active inventory for (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :param str rows: Number of results to return. Default is 10. Max is 50
        :param str start: Page number to fetch the results for the given criteria. Default is 1. Pagination is allowed only till first 1000 results for the search and sort criteria. The page value can be only between 1 to 1000/rows
        :return: BaseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dealer_id', 'api_key', 'rows', 'start']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dealer_active_inventory" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dealer_id' is set
        if ('dealer_id' not in params or
                params['dealer_id'] is None):
            raise ValueError("Missing the required parameter `dealer_id` when calling `get_dealer_active_inventory`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dealer_id' in params:
            path_params['dealer_id'] = params['dealer_id']  # noqa: E501

        query_params = []
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))  # noqa: E501
        if 'rows' in params:
            query_params.append(('rows', params['rows']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501

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
            '/dealer/{dealer_id}/active/inventory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseListing',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dealer_historical_inventory(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer&#39;s historical inventory  # noqa: E501

        [v1 : Not Implemented Yet] - Get a dealer's historical inventory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_historical_inventory(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Id representing the dealer to fetch the active inventory for (required)
        :return: BaseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dealer_historical_inventory_with_http_info(dealer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dealer_historical_inventory_with_http_info(dealer_id, **kwargs)  # noqa: E501
            return data

    def get_dealer_historical_inventory_with_http_info(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer&#39;s historical inventory  # noqa: E501

        [v1 : Not Implemented Yet] - Get a dealer's historical inventory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_historical_inventory_with_http_info(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Id representing the dealer to fetch the active inventory for (required)
        :return: BaseListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dealer_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dealer_historical_inventory" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dealer_id' is set
        if ('dealer_id' not in params or
                params['dealer_id'] is None):
            raise ValueError("Missing the required parameter `dealer_id` when calling `get_dealer_historical_inventory`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dealer_id' in params:
            path_params['dealer_id'] = params['dealer_id']  # noqa: E501

        query_params = []

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
            '/dealer/{dealer_id}/historical/inventory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseListing',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dealer_landing_page(self, dealer_id, **kwargs):  # noqa: E501
        """Experimental: Get cached version of dealer landing page by dealer id  # noqa: E501

        Experimental: Get cached version of dealer landing page by dealer id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_landing_page(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Robot id to get the landing page html for (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :return: DealerLandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dealer_landing_page_with_http_info(dealer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dealer_landing_page_with_http_info(dealer_id, **kwargs)  # noqa: E501
            return data

    def get_dealer_landing_page_with_http_info(self, dealer_id, **kwargs):  # noqa: E501
        """Experimental: Get cached version of dealer landing page by dealer id  # noqa: E501

        Experimental: Get cached version of dealer landing page by dealer id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_landing_page_with_http_info(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Robot id to get the landing page html for (required)
        :param str api_key: The API Authentication Key. Mandatory with all API calls.
        :return: DealerLandingPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dealer_id', 'api_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dealer_landing_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dealer_id' is set
        if ('dealer_id' not in params or
                params['dealer_id'] is None):
            raise ValueError("Missing the required parameter `dealer_id` when calling `get_dealer_landing_page`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dealer_id' in params:
            path_params['dealer_id'] = params['dealer_id']  # noqa: E501

        query_params = []
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))  # noqa: E501

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
            '/dealer/{dealer_id}/landing', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DealerLandingPage',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dealer_ratings(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer&#39;s Rating  # noqa: E501

        [MOCK] Get a dealer's Rating  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_ratings(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Id representing the dealer to fetch the ratings for (required)
        :return: DealerRating
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dealer_ratings_with_http_info(dealer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dealer_ratings_with_http_info(dealer_id, **kwargs)  # noqa: E501
            return data

    def get_dealer_ratings_with_http_info(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer&#39;s Rating  # noqa: E501

        [MOCK] Get a dealer's Rating  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_ratings_with_http_info(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Id representing the dealer to fetch the ratings for (required)
        :return: DealerRating
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dealer_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dealer_ratings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dealer_id' is set
        if ('dealer_id' not in params or
                params['dealer_id'] is None):
            raise ValueError("Missing the required parameter `dealer_id` when calling `get_dealer_ratings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dealer_id' in params:
            path_params['dealer_id'] = params['dealer_id']  # noqa: E501

        query_params = []

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
            '/dealer/{dealer_id}/ratings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DealerRating',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dealer_reviews(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer&#39;s Review  # noqa: E501

        [MOCK] Get a dealer's Review  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_reviews(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Id representing the dealer to fetch the ratings for (required)
        :return: DealerReview
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dealer_reviews_with_http_info(dealer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dealer_reviews_with_http_info(dealer_id, **kwargs)  # noqa: E501
            return data

    def get_dealer_reviews_with_http_info(self, dealer_id, **kwargs):  # noqa: E501
        """Dealer&#39;s Review  # noqa: E501

        [MOCK] Get a dealer's Review  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dealer_reviews_with_http_info(dealer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dealer_id: Id representing the dealer to fetch the ratings for (required)
        :return: DealerReview
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dealer_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dealer_reviews" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dealer_id' is set
        if ('dealer_id' not in params or
                params['dealer_id'] is None):
            raise ValueError("Missing the required parameter `dealer_id` when calling `get_dealer_reviews`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dealer_id' in params:
            path_params['dealer_id'] = params['dealer_id']  # noqa: E501

        query_params = []

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
            '/dealer/{dealer_id}/reviews', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DealerReview',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
