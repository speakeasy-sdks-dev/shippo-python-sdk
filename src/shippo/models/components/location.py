"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .addresscompletecreaterequest import AddressCompleteCreateRequest
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from shippo import utils
from typing import Optional


class BuildingLocationType(str, Enum):
    r"""Where your parcels will be available for pickup. \\"Security Deck\\" and \\"Shipping Dock\\" are only
    supported for DHL Express.
    """
    BACK_DOOR = 'Back Door'
    RING_BELL = 'Ring Bell'
    SECURITY_DECK = 'Security Deck'
    SHIPPING_DOCK = 'Shipping Dock'
    FRONT_DOOR = 'Front Door'
    KNOCK_ON_DOOR = 'Knock on Door'
    IN_AT_MAILBOX = 'In/At Mailbox'
    MAIL_ROOM = 'Mail Room'
    OFFICE = 'Office'
    OTHER = 'Other'
    RECEPTION = 'Reception'
    SIDE_DOOR = 'Side Door'


class BuildingType(str, Enum):
    r"""The type of building where the pickup is located."""
    APARTMENT = 'apartment'
    BUILDING = 'building'
    DEPARTMENT = 'department'
    FLOOR = 'floor'
    ROOM = 'room'
    SUITE = 'suite'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Location:
    r"""Location where the parcel(s) will be picked up."""
    address: AddressCompleteCreateRequest = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    r"""The pickup address, which includes your name, company name, street address, city, state, zip code,
    country, phone number, and email address (strings). Special characters should not be included in 
    any address element, especially name, company, and email.
    """
    building_location_type: BuildingLocationType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('building_location_type') }})
    r"""Where your parcels will be available for pickup. \\"Security Deck\\" and \\"Shipping Dock\\" are only
    supported for DHL Express.
    """
    building_type: Optional[BuildingType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('building_type'), 'exclude': lambda f: f is None }})
    r"""The type of building where the pickup is located."""
    instructions: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instructions'), 'exclude': lambda f: f is None }})
    r"""Pickup instructions for the courier. This is a mandatory field if the building_location_type is \\"Other\\"."""
    

