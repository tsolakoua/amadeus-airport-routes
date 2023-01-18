# openapi_client.model.locations.Locations

Description of a particular point or place in physical space

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Description of a particular point or place in physical space | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | type of API result \&quot;location\&quot; | [optional] 
**subtype** | str,  | str,  | Location sub-type (e.g. airport, port, rail-station, restaurant, atm...) | [optional] 
**name** | str,  | str,  | Label associated to the location (e.g. Eiffel Tower, Madison Square) | [optional] 
**iataCode** | str,  | str,  | IATA location code | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

