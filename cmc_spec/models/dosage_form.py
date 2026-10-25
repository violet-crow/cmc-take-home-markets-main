"""A dosage form: the worked example of a seeded reference list."""

from __future__ import annotations

from typing import Annotated

from cmc_spec.core import DataModel, Reference, ReferenceCode, Strid, reference_data


class DosageFormCode(ReferenceCode):
    TABLET = "TABLET"
    CAPSULE = "CAPSULE"
    SOLUTION_FOR_INJECTION = "SOLUTION_FOR_INJECTION"


@reference_data
class DosageForm(DataModel):
    """A dosage form a product can be manufactured in. Seeded in `data/dosage_forms.py`."""

    code: DosageFormCode
    name: str


DosageFormRef = Annotated[Strid, Reference(DosageForm)]
