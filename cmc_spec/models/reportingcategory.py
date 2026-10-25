"""An authority- and source-specific reporting category for a regulatory change."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from cmc_spec.core import DataModel, Reference, Strid, reference_data
from cmc_spec.models.authority import AuthorityRef
from cmc_spec.models.rulesource import RuleSourceRef


@reference_data
class ReportingCategory(DataModel):
    """A category a specialist may select when its source is applicable.

    ``code`` is intentionally a string, not a globally unique enum: different
    authorities may use the same visible code (for example, ``IB``) for
    distinct categories. The record identity and its authority/source
    references keep those categories separate.

    Effective dates and version are recorded on the linked RuleSource, avoiding
    duplicated temporal metadata here. Category availability still requires
    checking that source's verification status and applicability to the
    license, proposed change, and assessment date.
    """

    code: str = Field(min_length=1)
    description: str = Field(min_length=1)
    authority_strid: AuthorityRef
    rulesource_strid: RuleSourceRef


ReportingCategoryRef = Annotated[Strid, Reference(ReportingCategory)]
