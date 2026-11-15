from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from uuid import UUID, uuid4

from pedigree_ai.domain.enums import (
    ParentageType,
    PartnershipStatus,
    PartnershipType,
    PedigreeSex,
    RelationshipSource,
    RelationshipType,
    RelationshipVerificationStatus,
)


def utc_now() -> datetime:
    """Return the current timezone-aware UTC datetime."""
    return datetime.now(UTC)


# --------------------------------------------------
# Pedigree
# --------------------------------------------------


@dataclass
class Pedigree:
    """Represents a family or genetic pedigree."""

    name: str
    description: str | None = None
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        self.name = self.name.strip()

        if not self.name:
            raise ValueError("Pedigree name cannot be empty.")


# --------------------------------------------------
# Person
# --------------------------------------------------


@dataclass
class Person:
    """Represents an individual within a pedigree."""

    pedigree_id: UUID
    given_name: str | None = None
    family_name: str | None = None
    sex: PedigreeSex = PedigreeSex.UNKNOWN
    date_of_birth: date | None = None
    date_of_death: date | None = None
    is_proband: bool = False
    notes: str | None = None

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if self.given_name is not None:
            self.given_name = self.given_name.strip() or None

        if self.family_name is not None:
            self.family_name = self.family_name.strip() or None

        if (
            self.date_of_birth is not None
            and self.date_of_death is not None
            and self.date_of_death < self.date_of_birth
        ):
            raise ValueError("Date of death cannot be earlier than date of birth.")

    @property
    def full_name(self) -> str:
        """Return the person's available name."""
        return (
            " ".join(part for part in (self.given_name, self.family_name) if part)
            or "Unknown"
        )


# --------------------------------------------------
# Partnership
# --------------------------------------------------


@dataclass
class Partnership:
    """Represents a partnership between individuals."""

    pedigree_id: UUID
    partnership_type: PartnershipType = PartnershipType.UNKNOWN
    status: PartnershipStatus = PartnershipStatus.UNKNOWN
    start_date: date | None = None
    end_date: date | None = None
    notes: str | None = None

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if (
            self.start_date is not None
            and self.end_date is not None
            and self.end_date < self.start_date
        ):
            raise ValueError("Partnership end date cannot be earlier than start date.")


# --------------------------------------------------
# Partnership Member
# --------------------------------------------------


@dataclass
class PartnershipMember:
    """Connects a person to a partnership."""

    partnership_id: UUID
    person_id: UUID

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=utc_now)


# --------------------------------------------------
# Parentage
# --------------------------------------------------


@dataclass
class Parentage:
    """Represents a parent-child relationship."""

    parent_id: UUID
    child_id: UUID
    parentage_type: ParentageType = ParentageType.UNKNOWN
    source: RelationshipSource = RelationshipSource.USER_INPUT
    verification_status: RelationshipVerificationStatus = (
        RelationshipVerificationStatus.UNVERIFIED
    )
    notes: str | None = None

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if self.parent_id == self.child_id:
            raise ValueError("A person cannot be their own parent.")


# --------------------------------------------------
# Relationship Assertion
# --------------------------------------------------


@dataclass
class RelationshipAssertion:
    """
    Stores a directly reported kinship relationship.

    This is an assertion, not a parentage record.
    It must not automatically create biological parentage.
    """

    subject_person_id: UUID
    related_person_id: UUID
    relationship_type: RelationshipType

    source: RelationshipSource = RelationshipSource.USER_INPUT
    verification_status: RelationshipVerificationStatus = (
        RelationshipVerificationStatus.UNVERIFIED
    )
    notes: str | None = None

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if self.subject_person_id == self.related_person_id:
            raise ValueError(
                "A person cannot have a relationship assertion with themselves."
            )
