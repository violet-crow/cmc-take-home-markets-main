"""Representative seeded regulatory sources for the v1 specification.

These source records are examples based on the supplied evidence, not a
complete legal register. The UK and Mexico records are marked NEEDS_REVIEW;
verify their current primary sources before using their categories as confirmed.
"""

from __future__ import annotations

from datetime import date

from cmc_spec.core import seed_strid
from cmc_spec.models.rulesource import (
    RuleSource,
    RuleSourceCode,
    RuleSourceVerificationStatus,
)


RULESOURCES: tuple[RuleSource, ...] = (
    RuleSource(
        strid=seed_strid("rulesource", RuleSourceCode.FDA_314_70),
        code=RuleSourceCode.FDA_314_70,
        title="Post-approval changes for NDAs and ANDAs",
        publisher_name="U.S. Code of Federal Regulations",
        source_reference="21 CFR 314.70",
        version=None,
        effective_from=None,
        effective_to=None,
        verification_status=RuleSourceVerificationStatus.VERIFIED,
    ),
    RuleSource(
        strid=seed_strid("rulesource", RuleSourceCode.FDA_NDA_ANDA_GUIDANCE_2004),
        code=RuleSourceCode.FDA_NDA_ANDA_GUIDANCE_2004,
        title="Changes to an Approved NDA or ANDA",
        publisher_name="U.S. Food and Drug Administration",
        source_reference="FDA guidance, Changes to an Approved NDA or ANDA (2004)",
        version="2004",
        effective_from=None,
        effective_to=None,
        verification_status=RuleSourceVerificationStatus.VERIFIED,
    ),
    RuleSource(
        strid=seed_strid("rulesource", RuleSourceCode.EU_VARIATIONS_REGULATION_2024_1701),
        code=RuleSourceCode.EU_VARIATIONS_REGULATION_2024_1701,
        title="EU variations regulation as amended by Delegated Regulation (EU) 2024/1701",
        publisher_name="European Commission",
        source_reference=(
            "Commission Regulation (EC) No 1234/2008, as amended by "
            "Commission Delegated Regulation (EU) 2024/1701"
        ),
        version="2024/1701 amendment",
        effective_from=date(2025, 1, 1),
        effective_to=None,
        verification_status=RuleSourceVerificationStatus.VERIFIED,
    ),
    RuleSource(
        strid=seed_strid("rulesource", RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045),
        code=RuleSourceCode.EU_VARIATIONS_GUIDELINE_C_2025_5045,
        title="Guideline on the details of the various categories of variations",
        publisher_name="European Commission",
        source_reference="Commission Guideline C/2025/5045",
        version="C/2025/5045",
        effective_from=date(2026, 1, 15),
        effective_to=None,
        verification_status=RuleSourceVerificationStatus.VERIFIED,
    ),
    RuleSource(
        strid=seed_strid("rulesource", RuleSourceCode.HSA_THERAPEUTIC_PRODUCT_GUIDANCE),
        code=RuleSourceCode.HSA_THERAPEUTIC_PRODUCT_GUIDANCE,
        title="Guidance on Therapeutic Product Registration in Singapore",
        publisher_name="Health Sciences Authority (HSA), Singapore",
        source_reference=(
            "Health Products Act 2007; Health Products (Therapeutic Products) "
            "Regulations 2016; HSA Guidance on Therapeutic Product Registration "
            "in Singapore, including the applicable variation appendices"
        ),
        version=None,
        effective_from=None,
        effective_to=None,
        verification_status=RuleSourceVerificationStatus.VERIFIED,
    ),
    RuleSource(
        strid=seed_strid("rulesource", RuleSourceCode.MHRA_NATIONAL_VARIATIONS_FRAMEWORK),
        code=RuleSourceCode.MHRA_NATIONAL_VARIATIONS_FRAMEWORK,
        title="UK national variations framework for marketing authorisations",
        publisher_name="Medicines and Healthcare products Regulatory Agency (MHRA)",
        source_reference=(
            "Human Medicines Regulations 2012 (SI 2012/1916), regulation 65C "
            "and Schedule 10A; current MHRA guidance on variations to marketing authorisations"
        ),
        version=None,
        effective_from=None,
        effective_to=None,
        verification_status=RuleSourceVerificationStatus.NEEDS_REVIEW,
    ),
    RuleSource(
        strid=seed_strid("rulesource", RuleSourceCode.COFEPRIS_MCRS_FRAMEWORK),
        code=RuleSourceCode.COFEPRIS_MCRS_FRAMEWORK,
        title="Mexico: modifications to conditions of sanitary registration",
        publisher_name="COFEPRIS / Secretaría de Salud",
        source_reference=(
            "Reglamento de Insumos para la Salud and the 2022–2023 regulatory-"
            "simplification agreements; source evidence cites homoclaves "
            "COFEPRIS-2022-022-011-A, COFEPRIS-2022-022-012-A, and "
            "COFEPRIS-2022-022-013-A"
        ),
        version="2022–2023 framework; confirm current source/version",
        effective_from=None,
        effective_to=None,
        verification_status=RuleSourceVerificationStatus.NEEDS_REVIEW,
    ),
)

RULESOURCES_BY_CODE = {row.code: row for row in RULESOURCES}
