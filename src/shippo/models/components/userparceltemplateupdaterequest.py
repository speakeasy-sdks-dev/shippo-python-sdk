"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .distanceunitenum import DistanceUnitEnum
from .weightunitenum import WeightUnitEnum
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UserParcelTemplateUpdateRequest:
    distance_unit: DistanceUnitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('distance_unit') }})
    r"""The measure unit used for length, width and height."""
    height: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height') }})
    r"""The height of the package, in units specified by the `distance_unit` attribute. Required, but if using a preset carrier template then this field must be empty."""
    length: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('length') }})
    r"""The length of the package, in units specified by the `distance_unit` attribute. Required, but if using a preset carrier template then this field must be empty."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the User Parcel Template"""
    width: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width') }})
    r"""The width of the package, in units specified by the `distance_unit` attribute. Required, but if using a preset carrier template then this field must be empty."""
    weight: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight'), 'exclude': lambda f: f is None }})
    r"""The weight of the package, in units specified by the weight_unit attribute."""
    weight_unit: Optional[WeightUnitEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight_unit'), 'exclude': lambda f: f is None }})
    r"""The unit used for weight."""
    

