import openapi_client
from openapi_client.apis.tags import direct_destinations_api
from openapi_client.model.locations import Locations
from openapi_client.model.meta import Meta
from openapi_client.model.errors import Errors
from openapi_client.model.warnings import Warnings
from pprint import pprint
import json
from frozendict import frozendict 
# Defining the host is optional and defaults to https://test.api.amadeus.com/v1
# See configuration.py for a list of all supported configuration parameters.

configuration = openapi_client.Configuration()
api_client = openapi_client.ApiClient(configuration)
api_client.default_headers['Authorization'] = 'Bearer YOUR_TOKEN'

api_instance = direct_destinations_api.DirectDestinationsApi(api_client)

query_params = {
    'departureAirportCode': "BLR",
}

try:
    api_response = api_instance.airport__direct_destinations(
        query_params=query_params,
    )
    location_obj = Locations(frozendict(api_response.body['data'][0]))
    pprint(location_obj.get('name'))

except openapi_client.ApiException as e:
    print("Exception when calling Covid19AreaReportApi->g_et_covid_report: %s\n" % e)