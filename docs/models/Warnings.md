# openapi_client.model.warnings.Warnings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | decimal.Decimal, int,  | decimal.Decimal,  | A machine-readable error code from the Canned Messages table, that will enable the API Consumers code to handle this type of error | [optional] 
**title** | str,  | str,  | An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized | [optional] 
**detail** | str,  | str,  | An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be localized. | [optional] 
**[source](#source)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The Warning Source Definition | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# source

The Warning Source Definition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Warning Source Definition | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**parameter** | str,  | str,  | The key of the URI path or query parameter that caused the error | [optional] 
**pointer** | str,  | str,  | A JSON Pointer RFC6901 to the associated entity in the request body that caused this error | [optional] 
**example** | str,  | str,  | A sample input to guide the user when resolving this issue | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

