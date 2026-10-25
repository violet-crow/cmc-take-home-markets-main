"""A legal territory covered by a marketing authorization."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from cmc_spec.core import DataModel, ImmutableSet, Reference, Strid


class Market(DataModel):
    """A national or multi-country territory covered by an authorization."""

    code: str
    name: str
    country_codes: ImmutableSet[str] = Field(min_length=1)


MarketRef = Annotated[Strid, Reference(Market)]