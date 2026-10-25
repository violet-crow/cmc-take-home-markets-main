"""A recorded regulatory category for a change, product, and license."""

from __future__ import annotations

from datetime import date
from typing import Annotated

from cmc_spec.core import DataModel, Reference, Strid
from cmc_spec.models.change import ChangeRef
from cmc_spec.models.license import LicenseRef
from cmc_spec.models.product import ProductRef
from cmc_spec.models.reportingcategory import ReportingCategoryRef


class ImpactClassification(DataModel):
    """The category selected for one Change × Product × License combination.

    Only completed classifications are represented by this record. An unresolved
    combination has no ImpactClassification row; the assessment review identifies
    that gap by comparing expected active product/license combinations with the
    recorded classifications.

    Cross-record rules (for example, that the product is affected by the change,
    the license belongs to the product, and the category is eligible for the
    license's authority and the assessment date) must be validated by the data or
    application layer, because the UUID references alone cannot enforce them.
    """

    change_strid: ChangeRef
    product_strid: ProductRef
    license_strid: LicenseRef
    reporting_category_strid: ReportingCategoryRef
    assessment_date: date


ImpactClassificationRef = Annotated[Strid, Reference(ImpactClassification)]
"""A reference to an ImpactClassification record."""
