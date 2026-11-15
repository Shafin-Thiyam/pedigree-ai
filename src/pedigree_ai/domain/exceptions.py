class PedigreeDomainError(Exception):
    """Base exception for all pedigree domain errors."""


# --------------------------------------------------
# Entity not found exceptions
# --------------------------------------------------


class EntityNotFoundError(PedigreeDomainError):
    """Base exception when a requested domain entity is not found."""


class PedigreeNotFoundError(EntityNotFoundError):
    """Raised when a pedigree does not exist."""


class PersonNotFoundError(EntityNotFoundError):
    """Raised when a person does not exist."""


class PartnershipNotFoundError(EntityNotFoundError):
    """Raised when a partnership does not exist."""


class ParentageNotFoundError(EntityNotFoundError):
    """Raised when a parentage relationship does not exist."""


# --------------------------------------------------
# Relationship validation exceptions
# --------------------------------------------------


class RelationshipValidationError(PedigreeDomainError):
    """Base exception for invalid relationship operations."""


class AncestryCycleError(RelationshipValidationError):
    """Raised when a parentage relationship creates an ancestry cycle."""


class DuplicateRelationshipError(RelationshipValidationError):
    """Raised when an equivalent relationship already exists."""


class ConflictingRelationshipError(RelationshipValidationError):
    """Raised when new relationship information conflicts with existing data."""
