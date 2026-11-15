from enum import Enum
class PedigreeSex(str, Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"

class PartnershipType(str, Enum):
    MARRIAGE = "marriage"
    DOMESTIC_PARTNERSHIP = "domestic_partnership"
    UNMARRIED_PARTNERSHIP = "unmarried_partnership"
    OTHER = "other"
    UNKNOWN = "unknown"

class PartnershipStatus(str, Enum):

    CURRENT = "current"
    SEPARATED = "separated"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    ENDED = "ended"
    ANNULLED = "annulled"
    UNKNOWN = "unknown"


class ParentageType(str, Enum):

    GENETIC = "genetic"
    ADOPTIVE = "adoptive"
    LEGAL = "legal"
    FOSTER = "foster"
    GUARDIAN = "guardian"
    UNKNOWN = "unknown"


class RelationshipType(str, Enum):

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

    UNVERIFIED = "unverified"
    USER_CONFIRMED = "user_confirmed"
    DOCUMENTED = "documented"
    DISPUTED = "disputed"
    REJECTED = "rejected"


class RelationshipSource(str, Enum):

    USER_INPUT = "user_input"
    IMPORTED = "imported"
    SYSTEM_DERIVED = "system_derived"
    EXTERNAL_SOURCE = "external_source"

