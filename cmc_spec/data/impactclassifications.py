"""Illustrative completed classifications for the v1 model.

These rows are synthetic examples, not real regulatory decisions. The example
change affects the three demonstration products used in data/licenses.py.
There is intentionally no row for the active UK license: its rule source is
marked NEEDS_REVIEW, so the combination should remain an unresolved gap rather
than receive an unsupported category. The inactive Mexico license is not
classified.

ImpactClassification is user-recorded data, not immutable reference data, so
this example tuple is NOT decorated with @reference_data.
"""

from __future__ import annotations

from datetime import date

from cmc_spec.core import seed_strid
from cmc_spec.data.authorities import AUTHORITIES_BY_CODE
from cmc_spec.data.licenses import (
    DEMO_PRODUCT_001,
    DEMO_PRODUCT_002,
    DEMO_PRODUCT_003,
    LICENSES,
    LICENSES_BY_CODE,
)
from cmc_spec.data.reportingcategories import (
    REPORTING_CATEGORIES,
    REPORTING_CATEGORIES_BY_AUTHORITY_CODE_AND_SOURCE,
)
from cmc_spec.data.rulesources import RULESOURCES
from cmc_spec.models.authority import AuthorityCode
from cmc_spec.models.change import Change
from cmc_spec.models.impactclassification import ImpactClassification
from cmc_spec.models.reportingcategory import ReportingCategory
from cmc_spec.models.rulesource import (
    RuleSource,
    RuleSourceCode,
    RuleSourceVerificationStatus,
)


# The Change itself is normally maintained as customer data. This synthetic
# instance provides a coherent example context for the classifications below.
DEMO_CHANGE_001 = Change(
    strid=seed_strid("change", "DEMO-CHG-001"),
    summary="Illustrative supplier change affecting three products",
    product_strids=frozenset(
        {DEMO_PRODUCT_001, DEMO_PRODUCT_002, DEMO_PRODUCT_003}
    ),
)

# These are examples of when a specialist has made and recorded a classification.
# They do not claim that the example change actually qualifies for these categories.
IMPACT_CLASSIFICATIONS: tuple[ImpactClassification, ...] = (
    ImpactClassification(
        strid=seed_strid("impact_classification", "DEMO-IC-001-EU"),
        change_strid=DEMO_CHANGE_001.strid,
        product_strid=DEMO_PRODUCT_001,
        license_strid=LICENSES_BY_CODE["DEMO-LIC-001-EU-EEA"].strid,
        reporting_category_strid=REPORTING_CATEGORIES_BY_AUTHORITY_CODE_AND_SOURCE[
            (
                AUTHORITIES_BY_CODE[AuthorityCode.EU_COMMISSION].strid,
                "IB",
                seed_strid(
                    "rulesource",
                    RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045.value,
                ),
            )
        ].strid,
        assessment_date=date(2026, 10, 25),
    ),
    ImpactClassification(
        strid=seed_strid("impact_classification", "DEMO-IC-002-US"),
        change_strid=DEMO_CHANGE_001.strid,
        product_strid=DEMO_PRODUCT_001,
        license_strid=LICENSES_BY_CODE["DEMO-LIC-002-US"].strid,
        reporting_category_strid=REPORTING_CATEGORIES_BY_AUTHORITY_CODE_AND_SOURCE[
            (
                AUTHORITIES_BY_CODE[AuthorityCode.FDA].strid,
                "PAS",
                seed_strid("rulesource", RuleSourceCode.FDA_314_70.value),
            )
        ].strid,
        assessment_date=date(2026, 10, 25),
    ),
    ImpactClassification(
        strid=seed_strid("impact_classification", "DEMO-IC-003-DE"),
        change_strid=DEMO_CHANGE_001.strid,
        product_strid=DEMO_PRODUCT_002,
        license_strid=LICENSES_BY_CODE["DEMO-LIC-003-DE"].strid,
        reporting_category_strid=REPORTING_CATEGORIES_BY_AUTHORITY_CODE_AND_SOURCE[
            (
                AUTHORITIES_BY_CODE[AuthorityCode.BFARM].strid,
                "IB",
                seed_strid(
                    "rulesource",
                    RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045.value,
                ),
            )
        ].strid,
        assessment_date=date(2026, 10, 25),
    ),
    ImpactClassification(
        strid=seed_strid("impact_classification", "DEMO-IC-004-SG"),
        change_strid=DEMO_CHANGE_001.strid,
        product_strid=DEMO_PRODUCT_003,
        license_strid=LICENSES_BY_CODE["DEMO-LIC-005-SG"].strid,
        reporting_category_strid=REPORTING_CATEGORIES_BY_AUTHORITY_CODE_AND_SOURCE[
            (
                AUTHORITIES_BY_CODE[AuthorityCode.HSA].strid,
                "MIV-1",
                seed_strid(
                    "rulesource",
                    RuleSourceCode.HSA_THERAPEUTIC_PRODUCT_GUIDANCE.value,
                ),
            )
        ].strid,
        assessment_date=date(2026, 10, 25),
    ),
)


# Validate the representative rows so copy/paste mistakes in the seed data fail
# early. These checks protect this sample dataset; production callers must apply
# the same integrity rules when saving user-recorded classifications.
_LICENSES_BY_STRID = {row.strid: row for row in LICENSES}
_CATEGORIES_BY_STRID = {row.strid: row for row in REPORTING_CATEGORIES}
_SOURCES_BY_STRID = {row.strid: row for row in RULESOURCES}
_ALLOWED_SOURCE_STATUSES = {
    RuleSourceVerificationStatus.VERIFIED,
    RuleSourceVerificationStatus.AUTHORITY_CONFIRMED,
}
_seen_combinations: set[tuple[object, object, object]] = set()

for _row in IMPACT_CLASSIFICATIONS:
    _combination = (_row.change_strid, _row.product_strid, _row.license_strid)
    if _combination in _seen_combinations:
        raise ValueError(
            "Duplicate ImpactClassification for the same change/product/license combination"
        )
    _seen_combinations.add(_combination)

    if _row.change_strid != DEMO_CHANGE_001.strid:
        raise ValueError(f"Unknown Change in sample classification {_row.strid}")
    if _row.product_strid not in DEMO_CHANGE_001.product_strids:
        raise ValueError(
            f"Product {_row.product_strid} is not linked to the sample Change"
        )

    _license = _LICENSES_BY_STRID.get(_row.license_strid)
    if _license is None:
        raise ValueError(f"Unknown License in sample classification {_row.strid}")
    if _license.product_strid != _row.product_strid:
        raise ValueError(
            f"License {_license.license_code} does not belong to the classification's Product"
        )
    if not _license.is_active:
        raise ValueError(
            f"Inactive license {_license.license_code} must not receive a classification"
        )

    _category = _CATEGORIES_BY_STRID.get(_row.reporting_category_strid)
    if _category is None:
        raise ValueError(f"Unknown ReportingCategory in sample classification {_row.strid}")
    if _category.authority_strid != _license.authority_strid:
        raise ValueError(
            f"Category {_category.code!r} does not belong to the license's authority"
        )

    _source = _SOURCES_BY_STRID.get(_category.rulesource_strid)
    if _source is None:
        raise ValueError(f"Unknown RuleSource for category {_category.code!r}")
    if _source.verification_status not in _ALLOWED_SOURCE_STATUSES:
        raise ValueError(
            f"Unverified RuleSource {_source.code.value!r} cannot support a classification"
        )
    if (
        _source.effective_from is not None
        and _row.assessment_date < _source.effective_from
    ):
        raise ValueError(
            f"RuleSource {_source.code.value!r} was not yet effective on the assessment date"
        )
    if (
        _source.effective_to is not None
        and _row.assessment_date > _source.effective_to
    ):
        raise ValueError(
            f"RuleSource {_source.code.value!r} had expired by the assessment date"
        )

IMPACT_CLASSIFICATIONS_BY_STRID = {
    row.strid: row for row in IMPACT_CLASSIFICATIONS
}
IMPACT_CLASSIFICATIONS_BY_COMBINATION = {
    (row.change_strid, row.product_strid, row.license_strid): row
    for row in IMPACT_CLASSIFICATIONS
}
