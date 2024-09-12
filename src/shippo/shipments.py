"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from shippo import utils
from shippo._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext
from shippo.models import components, errors, operations
from typing import Optional

class Shipments:
    r"""A shipment is the act of transporting goods. A shipment object contains **to** and **from** addresses, and the parcel details that you are shipping. You can use the shipment object to retrieve shipping rates and purchase a shipping label.
    <SchemaDefinition schemaRef=\"#/components/schemas/Shipment\"/>

    # Shipment Extras
    The following values are supported for the `extra` field of the shipment object.
    <SchemaDefinition schemaRef=\"#/components/schemas/ShipmentExtra\"/>
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def list(self, request: operations.ListShipmentsRequest) -> components.ShipmentPaginatedList:
        r"""List all shipments
        Returns a list of all shipment objects.<br><br>
        In order to filter results, you must use the below path parameters. 
        A maximum date range of 90 days is permitted. 
        Provided dates should be ISO 8601 UTC dates (timezone offsets are currently not supported).<br><br>

        Optional path parameters:<br>
          `object_created_gt`- object(s) created greater than a provided date time<br>
          `object_created_gte` - object(s) created greater than or equal to a provided date time<br>
          `object_created_lt` - object(s) created less than a provided date time<br>
          `object_created_lte` - object(s) created less than or equal to a provided date time<br>

          Date format examples:<br>
            `2017-01-01`<br>
            `2017-01-01T03:30:30` or `2017-01-01T03:30:30.5`<br>
            `2017-01-01T03:30:30Z`<br><br>

          Example URL:<br>
            `https://api.goshippo.com/shipments/?object_created_gte=2017-01-01T00:00:30&object_created_lt=2017-04-01T00:00:30`
        """
        hook_ctx = HookContext(operation_id='ListShipments', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        _globals = operations.ListShipmentsGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/shipments'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        query_params = { **utils.get_query_params(request, _globals), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 200:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.ShipmentPaginatedList])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    
    
    def create(self, request: components.ShipmentCreateRequest) -> components.Shipment:
        r"""Create a new shipment
        Creates a new shipment object.
        """
        hook_ctx = HookContext(operation_id='CreateShipment', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        _globals = operations.CreateShipmentGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/shipments'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, components.ShipmentCreateRequest, "request", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 201:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.Shipment])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    
    
    def get(self, shipment_id: str) -> components.Shipment:
        r"""Retrieve a shipment
        Returns an existing shipment using an object ID
        """
        hook_ctx = HookContext(operation_id='GetShipment', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetShipmentRequest(
            shipment_id=shipment_id,
        )
        
        _globals = operations.GetShipmentGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/shipments/{ShipmentId}', request, _globals)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 200:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.Shipment])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    

