from datetime import UTC, datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from pedigree_ai.domain.entities import Pedigree
from pedigree_ai.schemas.pedigree import (
    PedigreeCreate,
    PedigreeRead,
    PedigreeUpdate,
)


def test_create_pedigree_schema():
    schema = PedigreeCreate(
        name="Smith Family",
        description="Family medical history",
    )

    assert schema.name == "Smith Family"
    assert schema.description == "Family medical history"


def test_create_pedigree_schema_strips_whitespace():
    schema = PedigreeCreate(name="  Smith Family  ")

    assert schema.name == "Smith Family"


def test_create_pedigree_schema_rejects_empty_name():
    with pytest.raises(ValidationError):
        PedigreeCreate(name="   ")


def test_create_pedigree_schema_rejects_missing_name():
    with pytest.raises(ValidationError):
        PedigreeCreate()


def test_update_pedigree_schema_allows_partial_update():
    schema = PedigreeUpdate(
        description="Updated description",
    )

    assert schema.model_dump(exclude_unset=True) == {
        "description": "Updated description"
    }


def test_update_pedigree_schema_allows_clearing_description():
    schema = PedigreeUpdate(description=None)

    assert schema.model_dump(exclude_unset=True) == {"description": None}


def test_update_pedigree_schema_rejects_null_name():
    with pytest.raises(ValidationError):
        PedigreeUpdate(name=None)


def test_update_pedigree_schema_rejects_empty_name():
    with pytest.raises(ValidationError):
        PedigreeUpdate(name="   ")


def test_update_pedigree_schema_allows_empty_update():
    schema = PedigreeUpdate()

    assert schema.model_dump(exclude_unset=True) == {}


def test_read_pedigree_schema_from_domain_entity():
    now = datetime.now(UTC)

    pedigree = Pedigree(
        name="Smith Family",
        description="Family medical history",
        id=uuid4(),
        created_at=now,
        updated_at=now,
    )

    schema = PedigreeRead.model_validate(pedigree)

    assert schema.id == pedigree.id
    assert schema.name == pedigree.name
    assert schema.description == pedigree.description
    assert schema.created_at == pedigree.created_at
    assert schema.updated_at == pedigree.updated_at


def test_create_pedigree_schema_rejects_unknown_fields():
    with pytest.raises(ValidationError):
        PedigreeCreate(
            name="Smith Family",
            unknown_field="unexpected",
        )
