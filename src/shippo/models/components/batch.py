"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .batchshipmentpaginatedlist import BatchShipmentPaginatedList
from .labelfiletypeenum import LabelFileTypeEnum
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from shippo import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ObjectResults:
    r"""An object containing the following counts:<br>`creation_succeeded`<br>`creation_failed`<br>`purchase_succeeded`<br>`purchase_failed`"""
    creation_failed: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creation_failed') }})
    creation_succeeded: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creation_succeeded') }})
    purchase_failed: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purchase_failed') }})
    purchase_succeeded: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purchase_succeeded') }})
    



class BatchStatus(str, Enum):
    r"""Batches that are `VALIDATING` are being created and validated<br>
    `VALID` batches can be purchased<br>
    `INVALID` batches cannot be purchased, `INVALID` BatchShipments must be removed<br>
    Batches that are in the `PURCHASING` state are being purchased<br>
    `PURCHASED` batches are finished purchasing.
    """
    VALIDATING = 'VALIDATING'
    VALID = 'VALID'
    INVALID = 'INVALID'
    PURCHASING = 'PURCHASING'
    PURCHASED = 'PURCHASED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Batch:
    default_carrier_account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_carrier_account') }})
    r"""ID of the Carrier Account object to use as the default for all shipments in this Batch.
    The carrier account can be changed on a per-shipment basis by changing the carrier_account in the 
    corresponding BatchShipment object.
    """
    default_servicelevel_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_servicelevel_token') }})
    r"""Token of the service level to use as the default for all shipments in this Batch.
    The servicelevel can be changed on a per-shipment basis by changing the servicelevel_token in the 
    corresponding BatchShipment object. <a href=\"#tag/Service-Levels\">Servicelevel tokens can be found here.</a>
    """
    batch_shipments: BatchShipmentPaginatedList = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_shipments') }})
    label_url: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label_url') }})
    r"""An array of URLs each pointing to a merged file of 100 labels each"""
    object_created: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_created') }})
    r"""Date and time of Batch creation"""
    object_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_id') }})
    r"""Unique identifier of the given Batch object"""
    object_owner: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_owner') }})
    r"""Username of the user who created the Address object."""
    object_results: ObjectResults = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_results') }})
    r"""An object containing the following counts:<br>`creation_succeeded`<br>`creation_failed`<br>`purchase_succeeded`<br>`purchase_failed`"""
    object_updated: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_updated') }})
    r"""Date and time of last update to the Batch"""
    status: BatchStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Batches that are `VALIDATING` are being created and validated<br>
    `VALID` batches can be purchased<br>
    `INVALID` batches cannot be purchased, `INVALID` BatchShipments must be removed<br>
    Batches that are in the `PURCHASING` state are being purchased<br>
    `PURCHASED` batches are finished purchasing.
    """
    label_filetype: Optional[LabelFileTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label_filetype'), 'exclude': lambda f: f is None }})
    r"""Print format of the <a href=\\"https://docs.goshippo.com/docs/shipments/shippinglabelsizes/\\">label</a>. If empty, will use the default format set from
    <a href=\"https://apps.goshippo.com/settings/labels\">the Shippo dashboard.</a>
    """
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""
    test: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test'), 'exclude': lambda f: f is None }})
    

