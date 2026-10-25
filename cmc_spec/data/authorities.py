"""Seeded regulatory authorities used by the illustrative v1 license data."""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.models.authority import Authority, AuthorityCode


AUTHORITIES: tuple[Authority, ...] = (
    Authority(
        strid=seed_strid("authority", AuthorityCode.EU_COMMISSION),
        code=AuthorityCode.EU_COMMISSION,
        name="European Commission",
    ),
    Authority(
        strid=seed_strid("authority", AuthorityCode.FDA),
        code=AuthorityCode.FDA,
        name="U.S. Food and Drug Administration (FDA)",
    ),
    Authority(
        strid=seed_strid("authority", AuthorityCode.BFARM),
        code=AuthorityCode.BFARM,
        name="Federal Institute for Drugs and Medical Devices (BfArM)",
    ),
    Authority(
        strid=seed_strid("authority", AuthorityCode.MHRA),
        code=AuthorityCode.MHRA,
        name="Medicines and Healthcare products Regulatory Agency (MHRA)",
    ),
    Authority(
        strid=seed_strid("authority", AuthorityCode.HSA),
        code=AuthorityCode.HSA,
        name="Health Sciences Authority (HSA), Singapore",
    ),
    Authority(
        strid=seed_strid("authority", AuthorityCode.COFEPRIS),
        code=AuthorityCode.COFEPRIS,
        name="Federal Commission for Protection against Sanitary Risks (COFEPRIS)",
    ),
)

AUTHORITIES_BY_CODE = {row.code: row for row in AUTHORITIES}
