
from datetime import date, datetime
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)

from pedigree_ai.domain.enums import PedigreeSex


# --------------------------------------------------
# Shared configuration
# --------------------------------------------------


class PersonSchema(BaseModel):
    """Base schema configuration for person API schemas."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )


# --------------------------------------------------
# Create
# --------------------------------------------------

class PersonCreate(PersonSchema):
    """Schema for creating a person."""

    given_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Given or first name.",
    )

    family_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Family or last name.",
    )

    sex: PedigreeSex = Field(
        default=PedigreeSex.UNKNOWN,
        description="Sex classification used for pedigree representation.",
    )

    date_of_birth: date | None = Field(
        default=None,
        description="Date of birth.",
    )

    date_of_death: date | None = Field(
        default=None,
        description="Date of death, if applicable.",
    )

    is_proband: bool = Field(
        default=False,
        description="Indicates whether this person is the proband.",
    )

    notes: str | None = Field(
        default=None,
        max_length=2000,
        description="Additional information about the person.",
    )

    @model_validator(mode="after")
    def validate_life_dates(self):
        """Ensure death date is not earlier than birth date."""

        if (
            self.date_of_birth is not None
            and self.date_of_death is not None
            and self.date_of_death < self.date_of_birth
        ):
            raise ValueError(
                "Date of death cannot be earlier than date of birth."
            )

        return self


# --------------------------------------------------
# Update
# --------------------------------------------------


class PersonUpdate(PersonSchema):
    """Schema for partially updating a person."""

    given_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    family_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    sex: PedigreeSex | None = None

    date_of_birth: date | None = None

    date_of_death: date | None = None

    is_proband: bool | None = None

    notes: str | None = Field(
        default=None,
        max_length=2000,
    )

    @field_validator("sex", "is_proband", mode="before")
    @classmethod
    def reject_null_for_required_fields(cls, value: object) -> object:
        """Reject explicit null values for non-nullable fields."""

        if value is None:
            raise ValueError("This field cannot be null.")

        return value

    @model_validator(mode="after")
    def validate_life_dates(self):
        """Validate dates when both are supplied in the update."""

        if (
            self.date_of_birth is not None
            and self.date_of_death is not None
            and self.date_of_death < self.date_of_birth
        ):
            raise ValueError(
                "Date of death cannot be earlier than date of birth."
            )

        return self


# --------------------------------------------------
# Read
# --------------------------------------------------


class PersonRead(PersonSchema):
    """Schema for returning person information."""

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
        str_strip_whitespace=True,
    )

    id: UUID
    pedigree_id: UUID

    given_name: str | None
    family_name: str | None
    full_name: str

    sex: PedigreeSex

    date_of_birth: date | None
    date_of_death: date | None

    is_proband: bool
    notes: str | None

    created_at: datetime
    updated_at: datetime
