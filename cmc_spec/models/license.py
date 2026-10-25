"""A marketing authorization held for a product in a defined market."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from cmc_spec.core import DataModel, Reference, Strid
from cmc_spec.models.authority import AuthorityRef
from cmc_spec.models.market import MarketRef
from cmc_spec.models.product import ProductRef


class License(DataModel):
    """A specific authorization record from the company's license register.

    ``authority_strid`` identifies the authority used for category selection.
    The applicable rule source is not stored permanently on this record: it
    may depend on the proposed change and assessment date, and should be
    recorded/resolved in the classification/rule-source model.
    """

    license_code: str = Field(min_length=1)
    product_strid: ProductRef
    market_strid: MarketRef
    authority_strid: AuthorityRef
    is_active: bool


LicenseRef = Annotated[Strid, Reference(License)]