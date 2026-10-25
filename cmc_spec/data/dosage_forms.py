"""The seeded dosage forms. Rows written out in full; strids derived from the code."""

from __future__ import annotations

from cmc_spec.core import seed_strid
from cmc_spec.models.dosage_form import DosageForm, DosageFormCode

DOSAGE_FORMS: tuple[DosageForm, ...] = (
    DosageForm(
        strid=seed_strid("dosage_form", DosageFormCode.TABLET),
        code=DosageFormCode.TABLET,
        name="Tablet",
    ),
    DosageForm(
        strid=seed_strid("dosage_form", DosageFormCode.CAPSULE),
        code=DosageFormCode.CAPSULE,
        name="Capsule",
    ),
    DosageForm(
        strid=seed_strid("dosage_form", DosageFormCode.SOLUTION_FOR_INJECTION),
        code=DosageFormCode.SOLUTION_FOR_INJECTION,
        name="Solution for injection",
    ),
)

DOSAGE_FORMS_BY_CODE = {row.code: row for row in DOSAGE_FORMS}
