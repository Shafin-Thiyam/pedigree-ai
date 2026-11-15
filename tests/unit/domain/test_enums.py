from pedigree_ai.domain.enums import (
    ParentageType,
    PartnershipStatus,
    PedigreeSex,
    RelationshipSource,
    RelationshipType,
)


def test_pedigree_sex():
    assert PedigreeSex.MALE.value == "male"


def test_partnership_status():
    assert PartnershipStatus.DIVORCED.value == "divorced"


def test_parentage_type():
    assert ParentageType.GENETIC.value == "genetic"


def test_cousin_relationship():
    assert RelationshipType.COUSIN.value == "cousin"


def test_relationship_source():
    assert RelationshipSource.USER_INPUT.value == "user_input"
