"""A CMC change: something the manufacturer changes, whose regulatory impact must be assessed."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from cmc_spec.core import DataModel, ImmutableSet, Reference, Strid
from cmc_spec.models.product import ProductRef


class Change(DataModel):
    summary: str
    product_strids: ImmutableSet[ProductRef] = Field(min_length=1)


ChangeRef = Annotated[Strid, Reference(Change)]
