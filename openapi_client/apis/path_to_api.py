import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.airport_direct_destinations import AirportDirectDestinations

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AIRPORT_DIRECTDESTINATIONS: AirportDirectDestinations,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AIRPORT_DIRECTDESTINATIONS: AirportDirectDestinations,
    }
)
