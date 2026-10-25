"""Illustrative license-register rows for demonstrating the v1 model.

These are synthetic examples, not actual company authorizations. Product IDs
must match the strids used by the corresponding demonstration Product records.
Market IDs must match the IDs in data/markets.py. Authority IDs are seeded in
 data/authorities.py.
"""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.models.authority import AuthorityCode
from cmc_spec.models.license import License


# These stable IDs are placeholders for demonstration Product records.
DEMO_PRODUCT_001 = seed_strid("product", "DEMO-PROD-001")
DEMO_PRODUCT_002 = seed_strid("product", "DEMO-PROD-002")
DEMO_PRODUCT_003 = seed_strid("product", "DEMO-PROD-003")


LICENSES: tuple[License, ...] = (
    # One authorization covering the modeled EU/EEA territory: one license row,
    # not one row for each constituent country.
    License(
        strid=seed_strid("license", "DEMO-LIC-001-EU-EEA"),
        license_code="DEMO-LIC-001-EU-EEA",
        product_strid=DEMO_PRODUCT_001,
        market_strid=seed_strid("market", "EU_EEA_FULL"),
        authority_strid=seed_strid("authority", AuthorityCode.EU_COMMISSION),
        is_active=True,
    ),
    License(
        strid=seed_strid("license", "DEMO-LIC-002-US"),
        license_code="DEMO-LIC-002-US",
        product_strid=DEMO_PRODUCT_001,
        market_strid=seed_strid("market", "US"),
        authority_strid=seed_strid("authority", AuthorityCode.FDA),
        is_active=True,
    ),
    # Separate national licenses are represented as separate records.
    License(
        strid=seed_strid("license", "DEMO-LIC-003-DE"),
        license_code="DEMO-LIC-003-DE",
        product_strid=DEMO_PRODUCT_002,
        market_strid=seed_strid("market", "DE"),
        authority_strid=seed_strid("authority", AuthorityCode.BFARM),
        is_active=True,
    ),
    License(
        strid=seed_strid("license", "DEMO-LIC-004-GB"),
        license_code="DEMO-LIC-004-GB",
        product_strid=DEMO_PRODUCT_002,
        market_strid=seed_strid("market", "GB"),
        authority_strid=seed_strid("authority", AuthorityCode.MHRA),
        is_active=True,
    ),
    License(
        strid=seed_strid("license", "DEMO-LIC-005-SG"),
        license_code="DEMO-LIC-005-SG",
        product_strid=DEMO_PRODUCT_003,
        market_strid=seed_strid("market", "SG"),
        authority_strid=seed_strid("authority", AuthorityCode.HSA),
        is_active=True,
    ),
    # An inactive record demonstrates why User 2 filters by current status.
    License(
        strid=seed_strid("license", "DEMO-LIC-006-MX-INACTIVE"),
        license_code="DEMO-LIC-006-MX-INACTIVE",
        product_strid=DEMO_PRODUCT_003,
        market_strid=seed_strid("market", "MX"),
        authority_strid=seed_strid("authority", AuthorityCode.COFEPRIS),
        is_active=False,
    ),
)

LICENSES_BY_CODE = {row.license_code: row for row in LICENSES}
