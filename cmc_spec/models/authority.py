"""A regulatory authority used to determine applicable classification rules."""

from __future__ import annotations

from typing import Annotated

from cmc_spec.core import (
    DataModel,
    Reference,
    ReferenceCode,
    Strid,
    reference_data,
)


class AuthorityCode(ReferenceCode):
    """Stable identifiers for the representative authorities seeded in v1."""

    EU_COMMISSION = "EU_COMMISSION"
    FDA = "FDA"
    BFARM = "BFARM"
    MHRA = "MHRA"
    HSA = "HSA"
    COFEPRIS = "COFEPRIS"


@reference_data
class Authority(DataModel):
    """A regulatory body used to identify the applicable category framework."""

    code: AuthorityCode
    name: str


AuthorityRef = Annotated[Strid, Reference(Authority)]
