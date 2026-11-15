
from enum import Enum


class PedigreeSex(str, Enum):
    """Sex classification used for pedigree representation."""

    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


class PartnershipType(str, Enum):
    """Type of partnership between individuals."""

    MARRIAGE = "marriage"
    DOMESTIC_PARTNERSHIP = "domestic_partnership"
    UNMARRIED_PARTNERSHIP = "unmarried_partnership"
    OTHER = "other"
    UNKNOWN = "unknown"


class PartnershipStatus(str, Enum):
    """Current or historical status of a partnership."""

    CURRENT = "current"
    SEPARATED = "separated"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    ENDED = "ended"
    ANNULLED = "annulled"
    UNKNOWN = "unknown"


class ParentageType(str, Enum):
    """Nature of a parent-child relationship."""

    GENETIC = "genetic"
    ADOPTIVE = "adoptive"
    LEGAL = "legal"
    FOSTER = "foster"
    GUARDIAN = "guardian"
    UNKNOWN = "unknown"


class RelationshipType(str, Enum):
    """Directly asserted kinship relationship between individuals."""

    SIBLING = "sibling"
    FULL_SIBLING = "full_sibling"
    HALF_SIBLING = "half_sibling"
    STEP_SIBLING = "step_sibling"
    ADOPTIVE_SIBLING = "adoptive_sibling"

    COUSIN = "cousin"

    PARENT = "parent"
    CHILD = "child"

    GRANDPARENT = "grandparent"
    GRANDCHILD = "grandchild"

    AUNT_UNCLE = "aunt_uncle"
    NIECE_NEPHEW = "niece_nephew"

    OTHER = "other"
    UNKNOWN = "unknown"


class RelationshipVerificationStatus(str, Enum):
    """Verification state of an asserted relationship."""

    UNVERIFIED = "unverified"
    USER_CONFIRMED = "user_confirmed"
    DOCUMENTED = "documented"
    DISPUTED = "disputed"
    REJECTED = "rejected"


class RelationshipSource(str, Enum):
    """Origin of relationship information."""

    USER_INPUT = "user_input"
    IMPORTED = "imported"
    SYSTEM_DERIVED = "system_derived"
    EXTERNAL_SOURCE = "external_source"
