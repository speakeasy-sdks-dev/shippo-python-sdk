"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DryIce:
    r"""Specify that the package contains Dry Ice (FedEx, Veho, and UPS only)."""
    contains_dry_ice: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contains_dry_ice'), 'exclude': lambda f: f is None }})
    r"""Mandatory. Specifies that the package contains Dry Ice."""
    weight: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight'), 'exclude': lambda f: f is None }})
    r"""Mandatory. Units must be in Kilograms. Cannot be greater than package weight."""
    

