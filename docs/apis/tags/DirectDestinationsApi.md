<a name="__pageTop"></a>
# openapi_client.apis.tags.direct_destinations_api.DirectDestinationsApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airport__direct_destinations**](#airport__direct_destinations) | **get** /airport/direct-destinations | get airport direct routes

# **airport__direct_destinations**
<a name="airport__direct_destinations"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} airport__direct_destinations(departure_airport_code)

get airport direct routes

### Example

```python
import openapi_client
from openapi_client.apis.tags import direct_destinations_api
from openapi_client.model.locations import Locations
from openapi_client.model.meta import Meta
from openapi_client.model.errors import Errors
from openapi_client.model.warnings import Warnings
from pprint import pprint
# Defining the host is optional and defaults to https://test.api.amadeus.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://test.api.amadeus.com/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_destinations_api.DirectDestinationsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'departureAirportCode': "BLR",
    }
    try:
        # get airport direct routes
        api_response = api_instance.airport__direct_destinations(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DirectDestinationsApi->airport__direct_destinations: %s\n" % e)

    # example passing only optional values
    query_params = {
        'departureAirportCode': "BLR",
        'max': 3.14,
    }
    try:
        # get airport direct routes
        api_response = api_instance.airport__direct_destinations(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DirectDestinationsApi->airport__direct_destinations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
departureAirportCode | DepartureAirportCodeSchema | | 
max | MaxSchema | | optional


# DepartureAirportCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#airport__direct_destinations.ApiResponseFor200) | Success Response
400 | [ApiResponseFor400](#airport__direct_destinations.ApiResponseFor400) | Bad Request  code    | title                                  ------- | -------------------------------------  572     | INVALID OPTION                          32171   | MANDATORY DATA MISSING  477     | INVALID FORMAT                        
500 | [ApiResponseFor500](#airport__direct_destinations.ApiResponseFor500) | Internal Server Error  code    | title                                  ------- | -------------------------------------  141     | SYSTEM ERROR HAS OCCURRED

#### airport__direct_destinations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[warnings](#warnings)** | list, tuple,  | tuple,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**meta** | [**Meta**]({{complexTypePrefix}}Meta.md) | [**Meta**]({{complexTypePrefix}}Meta.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# warnings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Warnings**]({{complexTypePrefix}}Warnings.md) | [**Warnings**]({{complexTypePrefix}}Warnings.md) | [**Warnings**]({{complexTypePrefix}}Warnings.md) |  | 

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Locations**]({{complexTypePrefix}}Locations.md) | [**Locations**]({{complexTypePrefix}}Locations.md) | [**Locations**]({{complexTypePrefix}}Locations.md) |  | 

#### airport__direct_destinations.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Errors**]({{complexTypePrefix}}Errors.md) | [**Errors**]({{complexTypePrefix}}Errors.md) | [**Errors**]({{complexTypePrefix}}Errors.md) |  | 

#### airport__direct_destinations.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, SchemaFor500ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Errors**]({{complexTypePrefix}}Errors.md) | [**Errors**]({{complexTypePrefix}}Errors.md) | [**Errors**]({{complexTypePrefix}}Errors.md) |  | 

# SchemaFor500ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The Error Definition | 

# items

The Error Definition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Error Definition | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status** | decimal.Decimal, int,  | decimal.Decimal,  | The [HTTP status code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) of this response. This is present only in terminal errors which cause an unsuccessful response. In the case of multiple errors, they must all have the same status. | [optional] 
**code** | decimal.Decimal, int,  | decimal.Decimal,  | A machine-readable error code from the Amadeus Canned Messages table, that will enable the API Consumers code to handle this type of error | [optional] 
**title** | str,  | str,  | An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized | [optional] 
**detail** | str,  | str,  | An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be localized. | [optional] 
**[source](#source)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# source

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**parameter** | str,  | str,  | The key of the URI path or query parameter that caused the error | [optional] 
**pointer** | str,  | str,  | A JSON Pointer [RFC6901] to the associated entity in the request body that caused this error | [optional] 
**example** | str,  | str,  | A sample input to guide the user when resolving this issue | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

