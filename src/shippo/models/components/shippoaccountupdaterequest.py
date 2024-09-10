"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShippoAccountUpdateRequest:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    company_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_name') }})
    

