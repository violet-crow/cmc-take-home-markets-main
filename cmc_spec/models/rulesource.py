"""An identifiable regulation, guideline, or other controlled rule source."""

from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Annotated

from pydantic import Field, model_validator

from cmc_spec.core import (
    DataModel,
    Reference,
    ReferenceCode,
    Strid,
    reference_data,
)


class RuleSourceCode(ReferenceCode):
    """Stable identifiers for the representative rule sources seeded in v1."""

    FDA_314_70 = "FDA_314_70"
    FDA_NDA_ANDA_GUIDANCE_2004 = "FDA_NDA_ANDA_GUIDANCE_2004"
    EU_VARIATIONS_REGULATION_2024_1701 = "EU_VARIATIONS_REGULATION_2024_1701"
    EU_VARIATIONS_GUIDELINE_C_2025_5045 = "EU_VARIATIONS_GUIDELINE_C_2025_5045"
    HSA_THERAPEUTIC_PRODUCT_GUIDANCE = "HSA_THERAPEUTIC_PRODUCT_GUIDANCE"
    MHRA_NATIONAL_VARIATIONS_FRAMEWORK = "MHRA_NATIONAL_VARIATIONS_FRAMEWORK"
    COFEPRIS_MCRS_FRAMEWORK = "COFEPRIS_MCRS_FRAMEWORK"


class RuleSourceVerificationStatus(StrEnum):
    """Whether a source is sufficiently verified to support category selection."""

    VERIFIED = "VERIFIED"
    AUTHORITY_CONFIRMED = "AUTHORITY_CONFIRMED"
    NEEDS_REVIEW = "NEEDS_REVIEW"
    UNVERIFIED = "UNVERIFIED"


@reference_data
class RuleSource(DataModel):
    """A source document that can support one or more reporting categories.

    The source itself is kept distinct from the authority whose categories it
    supports. That relationship belongs on ReportingCategory, so a shared
    regulation or guideline does not need duplicate source records merely
    because it is relevant to multiple authority-specific category sets.
    Applicability to a particular license, change, and assessment date must be
    resolved before a category is available for selection.
    """

    code: RuleSourceCode
    title: str = Field(min_length=1)
    publisher_name: str = Field(min_length=1)
    source_reference: str = Field(min_length=1)
    version: str | None = None
    effective_from: date | None = None
    effective_to: date | None = None
    verification_status: RuleSourceVerificationStatus

    @model_validator(mode="after")
    def effective_period_is_valid(self) -> RuleSource:
        if (
            self.effective_from is not None
            and self.effective_to is not None
            and self.effective_to < self.effective_from
        ):
            raise ValueError("effective_to must be on or after effective_from")
        return self


RuleSourceRef = Annotated[Strid, Reference(RuleSource)]
