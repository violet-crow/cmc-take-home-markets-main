"""The building blocks every model uses. See `models/dosage_form.py` for them in use."""

from __future__ import annotations

import hashlib
from collections.abc import Sequence
from collections.abc import Set as AbstractSet
from dataclasses import dataclass
from enum import StrEnum
from typing import Annotated, TypeVar
from uuid import UUID

from pydantic import AfterValidator, BaseModel, ConfigDict

Strid = UUID
"""A record's identifier. The only value anything joins on."""

_T = TypeVar("_T")

ImmutableList = Annotated[Sequence[_T], AfterValidator(tuple)]
"""A list a validator reads: stored as a tuple, so it can't be edited past the validator."""

ImmutableSet = Annotated[AbstractSet[_T], AfterValidator(frozenset)]
"""A set a validator reads: stored as a frozenset, for the same reason."""


class ValueModel(BaseModel):
    """A nested value with no identity. Closed: unknown fields are rejected."""

    model_config = ConfigDict(extra="forbid", validate_assignment=True)


class DataModel(ValueModel):
    """A record: something with identity, referenced by its `strid`."""

    strid: Strid


class ReferenceCode(StrEnum):
    """Base for a governed code list. Codes are immutable and never re-used."""


@dataclass(frozen=True)
class Reference:
    """Marks a strid field as pointing at another model:

    DosageFormRef = Annotated[Strid, Reference(DosageForm)]
    """

    model: type[DataModel]


_M = TypeVar("_M", bound=type[DataModel])


def reference_data(model: _M) -> _M:
    """Mark a model whose rows are seeded in `data/` and never written by the product."""
    model.model_config = {**model.model_config, "frozen": True}
    return model


def seed_strid(kind: str, code: str, /) -> UUID:
    """A stable strid for a seeded row, derived from its kind and code."""
    digest = hashlib.sha256(f"{kind}:{code}".encode()).digest()
    raw = bytearray(bytes(6) + digest[:10])
    raw[6] = 0x70 | (raw[6] & 0x0F)  # version 7
    raw[8] = 0x80 | (raw[8] & 0x3F)  # RFC 9562 variant
    return UUID(bytes=bytes(raw))
