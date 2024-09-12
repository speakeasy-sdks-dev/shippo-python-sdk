"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from shippo import utils
from typing import Optional


class RecipientType(str, Enum):
    r"""Mandatory for Fedex only. License type of the recipient of the Alcohol Package."""
    LICENSEE = 'licensee'
    CONSUMER = 'consumer'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Alcohol:
    r"""Indicates that a shipment contains Alcohol (Fedex and UPS only)."""
    contains_alcohol: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contains_alcohol'), 'exclude': lambda f: f is None }})
    r"""Mandatory for Fedex and UPS. Specifies that the package contains Alcohol."""
    recipient_type: Optional[RecipientType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recipient_type'), 'exclude': lambda f: f is None }})
    r"""Mandatory for Fedex only. License type of the recipient of the Alcohol Package."""
    

