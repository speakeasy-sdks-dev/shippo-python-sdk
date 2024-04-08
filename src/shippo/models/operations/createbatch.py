"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import batchcreaterequest as components_batchcreaterequest
from typing import Optional


@dataclasses.dataclass
class CreateBatchGlobals:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class CreateBatchRequest:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    batch_create_request: Optional[components_batchcreaterequest.BatchCreateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Batch details."""
    

