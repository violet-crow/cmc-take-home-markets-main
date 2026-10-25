"""A medicinal product the customer holds licences for."""

from __future__ import annotations

from typing import Annotated

from cmc_spec.core import DataModel, Reference, Strid
from cmc_spec.models.dosage_form import DosageFormRef


class Product(DataModel):
    name: str
    dosage_form_strid: DosageFormRef


ProductRef = Annotated[Strid, Reference(Product)]
