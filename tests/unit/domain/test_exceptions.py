import pytest

from pedigree_ai.domain.exceptions import (
    AncestryCycleError,
    ConflictingRelationshipError,
    DuplicateRelationshipError,
    EntityNotFoundError,
    ParentageNotFoundError,
    PartnershipNotFoundError,
    PedigreeDomainError,
    PedigreeNotFoundError,
    PersonNotFoundError,
    RelationshipValidationError,
)


def test_person_not_found_error():
    error = PersonNotFoundError("Person not found")

    assert isinstance(error, EntityNotFoundError)
    assert isinstance(error, PedigreeDomainError)
    assert str(error) == "Person not found"


def test_pedigree_not_found_error():
    error = PedigreeNotFoundError("Pedigree not found")

    assert isinstance(error, EntityNotFoundError)
    assert str(error) == "Pedigree not found"


def test_partnership_not_found_error():
    error = PartnershipNotFoundError("Partnership not found")

    assert isinstance(error, EntityNotFoundError)
    assert str(error) == "Partnership not found"


def test_parentage_not_found_error():
    error = ParentageNotFoundError("Parentage not found")

    assert isinstance(error, EntityNotFoundError)
    assert str(error) == "Parentage not found"


def test_ancestry_cycle_error():
    error = AncestryCycleError("Circular ancestry detected")

    assert isinstance(error, RelationshipValidationError)
    assert str(error) == "Circular ancestry detected"


def test_duplicate_relationship_error():
    error = DuplicateRelationshipError("Duplicate relationship")

    assert isinstance(error, RelationshipValidationError)
    assert str(error) == "Duplicate relationship"


def test_conflicting_relationship_error():
    error = ConflictingRelationshipError("Conflicting relationship")

    assert isinstance(error, RelationshipValidationError)
    assert str(error) == "Conflicting relationship"


def test_domain_exception_hierarchy():
    with pytest.raises(PedigreeDomainError):
        raise PersonNotFoundError("Person not found")


def test_relationship_exception_hierarchy():
    with pytest.raises(RelationshipValidationError):
        raise AncestryCycleError("Circular ancestry detected")
