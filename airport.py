import openapi_client
from openapi_client.apis.tags import direct_destinations_api
from openapi_client.model.locations import Locations
from openapi_client.model.meta import Meta
from openapi_client.model.errors import Errors
from openapi_client.model.warnings import Warnings
from pprint import pprint
# Defining the host is optional and defaults to https://test.api.amadeus.com/v1
# See configuration.py for a list of all supported configuration parameters.

configuration = openapi_client.Configuration()
api_client = openapi_client.ApiClient(configuration)
api_client.default_headers['Authorization'] = 'Bearer BUFDE9i9MOt5CpSGQa1JKq11TRSQ'

api_instance = direct_destinations_api.DirectDestinationsApi(api_client)

query_params = {
    'departureAirportCode': "BLR",
}
#        api_response = api_instance.report_definition_service_add_post(report_definition_service_operation=report_definition_service_operation)
#        job_id = api_response.rval.values[0].report_definition.report_job_id
try:
    api_response = api_instance.airport__direct_destinations(
        query_params=query_params,
    )
    # pprint(dir(api_response.response))
    # pprint(api_response.body)
    # p1 = Locations(api_response)
    pprint(api_response)

    #pprint(dir(api_response.body))
except openapi_client.ApiException as e:
    print("Exception when calling Covid19AreaReportApi->g_et_covid_report: %s\n" % e)