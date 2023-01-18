import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.direct_destinations_api import DirectDestinationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DIRECTDESTINATIONS: DirectDestinationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DIRECTDESTINATIONS: DirectDestinationsApi,
    }
)
