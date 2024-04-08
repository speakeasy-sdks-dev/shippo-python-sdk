"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InitiateOauth2SigninCarrierAccountsResponseResponseBody(Exception):
    r"""Invalid carrier account provided by the user"""
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    detail: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detail'), 'exclude': lambda f: f is None }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InitiateOauth2SigninCarrierAccountsResponseBody(Exception):
    r"""Invalid ShippoToken or unsupported carrier account provided by the user"""
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    detail: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detail'), 'exclude': lambda f: f is None }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InitiateOauth2SigninResponseBody(Exception):
    r"""Invalid parameters provided by the user"""
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    detail: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detail'), 'exclude': lambda f: f is None }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))
