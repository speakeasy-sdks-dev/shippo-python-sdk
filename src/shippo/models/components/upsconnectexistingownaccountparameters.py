"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UPSConnectExistingOwnAccountParameters:
    r"""An array of additional parameters for the account, such as e.g. password or token.
    Please check the <a href=\"https://docs.goshippo.com/docs/carriers/carrieraccounts/\">carrier accounts tutorial</a> page for the parameters per carrier.<br> 
    To protect account information, this field will be masked in any API response.
    """
    account_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_number') }})
    r"""The UPS account number"""
    billing_address_city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_city') }})
    billing_address_country_iso2: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_country_iso2') }})
    billing_address_state: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_state') }})
    billing_address_street1: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_street1') }})
    billing_address_zip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_zip') }})
    collec_country_iso2: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collec_country_iso2') }})
    collec_zip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collec_zip') }})
    r"""Zip code of the collection/pickup address"""
    company: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company') }})
    r"""Company name. Full name is acceptable in this field if the user has no company name"""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    full_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full_name') }})
    has_invoice: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_invoice') }})
    r"""true if user has been issued a UPS invoice within the past 90 days for the US or Canada; and 45 days for any other countries. User can use data from any of the last 3 invoices"""
    phone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    r"""User's title, e.g. including but not limited to Manager, Doctor, Artist, Engineer, Mr, Ms, Mrs, Mx"""
    ups_agreements: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ups_agreements') }})
    r"""Whether the user agrees to the UPS terms and conditions or not. Error 400 will be returned if passed in as false"""
    aia_country_iso2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aia_country_iso2'), 'exclude': lambda f: f is None }})
    r"""Only required if has_invoice is true. Country associated with the account that issued the invoice"""
    billing_address_street2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_street2'), 'exclude': lambda f: f is None }})
    r"""Empty string acceptable for billing_address_street2"""
    currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency_code'), 'exclude': lambda f: f is None }})
    r"""Only required if has_invoice is true. 3-letter currency code associated with invoice_value"""
    invoice_controlid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_controlid'), 'exclude': lambda f: f is None }})
    r"""Only required if aia_country_iso2 is US and has_invoice is true."""
    invoice_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_date'), 'exclude': lambda f: f is None }})
    r"""Only required if has_invoice is true. Date the invoice was issued. yyyymmdd format"""
    invoice_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_number'), 'exclude': lambda f: f is None }})
    invoice_value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_value'), 'exclude': lambda f: f is None }})
    r"""Only required if has_invoice is true. Max 16 digits before decimal and 2 digits after decimal"""
    

