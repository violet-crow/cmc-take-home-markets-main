"""Representative, source-backed reporting categories for the v1 model.

Only categories linked to rule sources marked VERIFIED or AUTHORITY_CONFIRMED
are included. This is a small demonstration dataset, not a complete regulatory
category register. UK and Mexico categories are intentionally omitted because
the corresponding RuleSource records are currently marked NEEDS_REVIEW.
"""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.data.authorities import AUTHORITIES
from cmc_spec.data.rulesources import RULESOURCES
from cmc_spec.models.authority import AuthorityCode
from cmc_spec.models.reportingcategory import ReportingCategory
from cmc_spec.models.rulesource import (
    RuleSourceCode,
    RuleSourceVerificationStatus,
)


_ALLOWED_SOURCE_STATUSES = {
    RuleSourceVerificationStatus.VERIFIED,
    RuleSourceVerificationStatus.AUTHORITY_CONFIRMED,
}

_AUTHORITY_STRIDS = {row.strid for row in AUTHORITIES}
_RULESOURCES_BY_STRID = {row.strid: row for row in RULESOURCES}


def _category(
    *,
    authority_code: AuthorityCode,
    rulesource_code: RuleSourceCode,
    code: str,
    description: str,
) -> ReportingCategory:
    """Create a stable category ID scoped to authority, source, and code."""
    category_key = f"{authority_code.value}:{rulesource_code.value}:{code}"
    return ReportingCategory(
        strid=seed_strid("reporting_category", category_key),
        code=code,
        description=description,
        authority_strid=seed_strid("authority", authority_code.value),
        rulesource_strid=seed_strid("rulesource", rulesource_code.value),
    )


REPORTING_CATEGORIES: tuple[ReportingCategory, ...] = (
    # United States: representative CMC reporting categories described in the
    # supplied evidence under 21 CFR 314.70.
    _category(
        authority_code=AuthorityCode.FDA,
        rulesource_code=RuleSourceCode.FDA_314_70,
        code="PAS",
        description="Prior Approval Supplement; major change requiring prior approval.",
    ),
    _category(
        authority_code=AuthorityCode.FDA,
        rulesource_code=RuleSourceCode.FDA_314_70,
        code="CBE-30",
        description="Changes Being Effected in 30 Days; moderate change with a 30-day wait.",
    ),
    _category(
        authority_code=AuthorityCode.FDA,
        rulesource_code=RuleSourceCode.FDA_314_70,
        code="CBE-0",
        description="Changes Being Effected; moderate change that may be implemented on receipt.",
    ),
    _category(
        authority_code=AuthorityCode.FDA,
        rulesource_code=RuleSourceCode.FDA_314_70,
        code="AR",
        description="Annual Report; minor change reported annually.",
    ),
    # EU centralized procedure: current category details are linked to the
    # current Commission variation guideline. Its effective date/version is
    # stored on the RuleSource record.
    _category(
        authority_code=AuthorityCode.EU_COMMISSION,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="IA",
        description="Type IA minor variation; included in the applicable annual grouping.",
    ),
    _category(
        authority_code=AuthorityCode.EU_COMMISSION,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="IA_IN",
        description="Type IA minor variation requiring immediate notification.",
    ),
    _category(
        authority_code=AuthorityCode.EU_COMMISSION,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="IB",
        description="Type IB minor variation; the default notify-then-wait category.",
    ),
    _category(
        authority_code=AuthorityCode.EU_COMMISSION,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="II",
        description="Type II major variation requiring prior approval.",
    ),
    _category(
        authority_code=AuthorityCode.EU_COMMISSION,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="EXT",
        description="Extension of a marketing authorisation.",
    ),
    # Germany: same EU framework, but separate category records because the
    # applicable authority differs from the centralized-procedure authority.
    _category(
        authority_code=AuthorityCode.BFARM,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="IA",
        description="Type IA minor variation under the EU variation framework for a German national authorisation.",
    ),
    _category(
        authority_code=AuthorityCode.BFARM,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="IA_IN",
        description="Type IA minor variation requiring immediate notification under the EU variation framework for a German national authorisation.",
    ),
    _category(
        authority_code=AuthorityCode.BFARM,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="IB",
        description="Type IB minor variation under the EU variation framework for a German national authorisation.",
    ),
    _category(
        authority_code=AuthorityCode.BFARM,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="II",
        description="Type II major variation requiring prior approval under the EU variation framework for a German national authorisation.",
    ),
    _category(
        authority_code=AuthorityCode.BFARM,
        rulesource_code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        code="EXT",
        description="Extension of a marketing authorisation under the EU variation framework for a German national authorisation.",
    ),
    # Singapore: HSA-specific terminology rather than generic ASEAN codes.
    _category(
        authority_code=AuthorityCode.HSA,
        rulesource_code=RuleSourceCode.HSA_THERAPEUTIC_PRODUCT_GUIDANCE,
        code="MAV-1",
        description="Major Variation Application, category MAV-1.",
    ),
    _category(
        authority_code=AuthorityCode.HSA,
        rulesource_code=RuleSourceCode.HSA_THERAPEUTIC_PRODUCT_GUIDANCE,
        code="MAV-2",
        description="Major Variation Application, category MAV-2.",
    ),
    _category(
        authority_code=AuthorityCode.HSA,
        rulesource_code=RuleSourceCode.HSA_THERAPEUTIC_PRODUCT_GUIDANCE,
        code="MIV-1",
        description="Minor Variation Application requiring prior approval.",
    ),
    _category(
        authority_code=AuthorityCode.HSA,
        rulesource_code=RuleSourceCode.HSA_THERAPEUTIC_PRODUCT_GUIDANCE,
        code="MIV-2 (Notification)",
        description="Minor variation notification with a standstill period.",
    ),
    _category(
        authority_code=AuthorityCode.HSA,
        rulesource_code=RuleSourceCode.HSA_THERAPEUTIC_PRODUCT_GUIDANCE,
        code="MIV-2 (Do-and-Tell)",
        description="Minor variation handled through the HSA do-and-tell process.",
    ),
    _category(
        authority_code=AuthorityCode.HSA,
        rulesource_code=RuleSourceCode.HSA_THERAPEUTIC_PRODUCT_GUIDANCE,
        code="Non-notifiable",
        description="Change listed as not requiring notification to HSA.",
    ),
)


# Fail early if a category references a missing authority/source or a source
# that has not been verified sufficiently for category selection.
for _row in REPORTING_CATEGORIES:
    if _row.authority_strid not in _AUTHORITY_STRIDS:
        raise ValueError(
            f"Reporting category {_row.code!r} references an unknown authority"
        )
    _source = _RULESOURCES_BY_STRID.get(_row.rulesource_strid)
    if _source is None:
        raise ValueError(
            f"Reporting category {_row.code!r} references an unknown rule source"
        )
    if _source.verification_status not in _ALLOWED_SOURCE_STATUSES:
        raise ValueError(
            f"Reporting category {_row.code!r} references a rule source that is not verified"
        )


# A category code is not globally unique. Use the authority + code + source key.
REPORTING_CATEGORIES_BY_AUTHORITY_CODE_AND_SOURCE = {
    (row.authority_strid, row.code, row.rulesource_strid): row
    for row in REPORTING_CATEGORIES
}
