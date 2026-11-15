from datetime import date
from uuid import uuid4

import pytest

from pedigree_ai.domain.entities import (
    Parentage,
    Partnership,
    Pedigree,
    Person,
    RelationshipAssertion,
)
from pedigree_ai.domain.enums import (
    ParentageType,
    PartnershipStatus,
    PartnershipType,
    PedigreeSex,
    RelationshipType,
)


def test_create_pedigree():
    pedigree = Pedigree(name="Smith Family")

    assert pedigree.name == "Smith Family"
    assert pedigree.id is not None


def test_pedigree_name_cannot_be_empty():
    with pytest.raises(ValueError):
        Pedigree(name="   ")


def test_create_person():
    person = Person(
        pedigree_id=uuid4(),
        given_name="John",
        family_name="Smith",
        sex=PedigreeSex.MALE,
    )

    assert person.full_name == "John Smith"
    assert person.sex == PedigreeSex.MALE


def test_person_with_unknown_name():
    person = Person(pedigree_id=uuid4())

    assert person.full_name == "Unknown"


def test_person_death_date_cannot_precede_birth_date():
    with pytest.raises(ValueError):
        Person(
            pedigree_id=uuid4(),
            date_of_birth=date(2000, 1, 1),
            date_of_death=date(1999, 1, 1),
        )


def test_create_partnership():
    partnership = Partnership(
        pedigree_id=uuid4(),
        partnership_type=PartnershipType.MARRIAGE,
        status=PartnershipStatus.CURRENT,
    )

    assert partnership.partnership_type == PartnershipType.MARRIAGE


def test_partnership_end_date_validation():
    with pytest.raises(ValueError):
        Partnership(
            pedigree_id=uuid4(),
            start_date=date(2020, 1, 1),
            end_date=date(2019, 1, 1),
        )


def test_parentage_cannot_reference_same_person():
    person_id = uuid4()

    with pytest.raises(ValueError):
        Parentage(
            parent_id=person_id,
            child_id=person_id,
        )


def test_create_genetic_parentage():
    parentage = Parentage(
        parent_id=uuid4(),
        child_id=uuid4(),
        parentage_type=ParentageType.GENETIC,
    )

    assert parentage.parentage_type == ParentageType.GENETIC


def test_relationship_assertion_cannot_reference_same_person():
    person_id = uuid4()

    with pytest.raises(ValueError):
        RelationshipAssertion(
            subject_person_id=person_id,
            related_person_id=person_id,
            relationship_type=RelationshipType.SIBLING,
        )
