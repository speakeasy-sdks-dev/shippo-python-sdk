"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .customsexporteridentification import CustomsExporterIdentification
from .customsinvoicedcharges import CustomsInvoicedCharges
from .objectstateenum import ObjectStateEnum
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from shippo import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomsDeclaration:
    certify: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certify') }})
    r"""Expresses that the certify_signer has provided all information of this customs declaration truthfully."""
    certify_signer: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certify_signer') }})
    r"""Name of the person who created the customs declaration and is responsible for the validity of all
    information provided.
    """
    contents_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contents_type') }})
    r"""Type of goods of the shipment.
    Allowed values available <a href=\"#tag/Customs-Declaration-Contents-Type\">here</a>
    """
    items: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    r"""Distinct Parcel content items as Customs Items object_ids."""
    non_delivery_option: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('non_delivery_option') }})
    r"""Indicates how the carrier should proceed in case the shipment can't be delivered.
    Allowed values available <a href=\"#tag/Customs-Declaration-Non-Delivery-Option\">here</a>
    """
    aes_itn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aes_itn'), 'exclude': lambda f: f is None }})
    r"""**required if eel_pfc is `AES_ITN`**<br>
    AES / ITN reference of the shipment.
    """
    b13a_filing_option: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('b13a_filing_option'), 'exclude': lambda f: f is None }})
    r"""B13A Option details are obtained by filing a B13A Canada Export Declaration via the Canadian Export Reporting System (CERS).
    <a href=\"https://www.cbsa-asfc.gc.ca/services/export/guide-eng.html\" target=\"_blank\" rel=\"noopener noreferrer\"> More information on reporting commercial exports from Canada. </a>
    Allowed values available <a href=\"#tag/Customs-Declaration-B13A-Filing-Option\">here</a>
    """
    b13a_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('b13a_number'), 'exclude': lambda f: f is None }})
    r"""**must be provided if and only if b13a_filing_option is provided**<br>
    Represents:<br> the Proof of Report (POR) Number when b13a_filing_option is `FILED_ELECTRONICALLY`;<br> 
    the Summary ID Number when b13a_filing_option is `SUMMARY_REPORTING`;<br> 
    or the Exemption Number when b13a_filing_option is `NOT_REQUIRED`.
    """
    certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificate'), 'exclude': lambda f: f is None }})
    r"""Certificate reference of the shipment."""
    commercial_invoice: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commercial_invoice'), 'exclude': lambda f: f is None }})
    contents_explanation: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contents_explanation'), 'exclude': lambda f: f is None }})
    r"""**required if contents_type is `OTHER`**<br>
    Explanation of the type of goods of the shipment.
    """
    disclaimer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disclaimer'), 'exclude': lambda f: f is None }})
    r"""Disclaimer for the shipment and customs information that have been provided."""
    exporter_identification: Optional[CustomsExporterIdentification] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exporter_identification'), 'exclude': lambda f: f is None }})
    r"""Additional exporter identification that may be required to ship in certain countries"""
    exporter_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exporter_reference'), 'exclude': lambda f: f is None }})
    r"""Exporter reference of an export shipment."""
    importer_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('importer_reference'), 'exclude': lambda f: f is None }})
    r"""Importer reference of an import shipment."""
    is_vat_collected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_vat_collected'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the shipment's destination VAT has been collected. May be required for some destinations."""
    invoice: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice'), 'exclude': lambda f: f is None }})
    r"""Invoice reference of the shipment."""
    license: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('license'), 'exclude': lambda f: f is None }})
    r"""License reference of the shipment."""
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A string of up to 100 characters that can be filled with any additional information you
    want to attach to the object.
    """
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes'), 'exclude': lambda f: f is None }})
    r"""Additional notes to be included in the customs declaration."""
    address_importer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_importer'), 'exclude': lambda f: f is None }})
    r"""Object ID of the Importer address."""
    eel_pfc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eel_pfc'), 'exclude': lambda f: f is None }})
    r"""EEL / PFC type of the shipment. For most shipments from the US to CA, `NOEEI_30_36` is applicable; for most
    other shipments from the US, `NOEEI_30_37_a` is applicable.
    Allowed values available <a href=\"#tag/Customs-Declaration-EELPFC\">here</a>
    """
    incoterm: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('incoterm'), 'exclude': lambda f: f is None }})
    r"""The incoterm reference of the shipment. FCA is available for DHL Express and FedEx only.
    eDAP is available for DPD UK only. DAP is available for DHL Express and DPD UK.
    If expecting DAP for other carriers, please use DDU.
    Allowed values available <a href=\"#tag/Customs-Declaration-Incoterm\">here</a>
    """
    invoiced_charges: Optional[CustomsInvoicedCharges] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiced_charges'), 'exclude': lambda f: f is None }})
    r"""Additional invoiced charges to be shown on the Customs Declaration Commercial Invoice."""
    object_created: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_created'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Date and time of object creation."""
    object_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the given object."""
    object_owner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_owner'), 'exclude': lambda f: f is None }})
    r"""Username of the user who created the object."""
    object_state: Optional[ObjectStateEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_state'), 'exclude': lambda f: f is None }})
    r"""Indicates the validity of the enclosing object"""
    object_updated: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_updated'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Date and time of last object update."""
    test: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the object has been created in test mode."""
    

