"""Representative market territories for the v1 specification."""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.models.market import Market


EU_EEA_COUNTRIES = frozenset({
    # EU member states
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI",
    "FR", "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU",
    "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE",

    # EEA-EFTA states
    "IS", "LI", "NO",
})


MARKETS: tuple[Market, ...] = (
    Market(
        strid=seed_strid("market", "US"),
        code="US",
        name="United States",
        country_codes=frozenset({"US"}),
    ),
    Market(
        strid=seed_strid("market", "DE"),
        code="DE",
        name="Germany",
        country_codes=frozenset({"DE"}),
    ),
    Market(
        strid=seed_strid("market", "GB"),
        code="GB",
        name="United Kingdom",
        country_codes=frozenset({"GB"}),
    ),
    Market(
        strid=seed_strid("market", "SG"),
        code="SG",
        name="Singapore",
        country_codes=frozenset({"SG"}),
    ),
    Market(
        strid=seed_strid("market", "MX"),
        code="MX",
        name="Mexico",
        country_codes=frozenset({"MX"}),
    ),
    Market(
        strid=seed_strid("market", "EU_EEA_FULL"),
        code="EU_EEA_FULL",
        name="EU/EEA (full territory)",
        country_codes=EU_EEA_COUNTRIES,
    ),
)

MARKETS_BY_CODE = {row.code: row for row in MARKETS}