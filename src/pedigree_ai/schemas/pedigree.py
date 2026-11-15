from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


# --------------------------------------------------
# Shared configuration
# --------------------------------------------------
class PedigreeSchema(BaseModel):
    """Base schema configuration for pedigree API schemas."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )


# --------------------------------------------------
# Create
# --------------------------------------------------
class PedigreeCreate(PedigreeSchema):
    """Schema for creating a new pedigree."""

    name: str = Field(
        min_length=1,
        max_length=150,
        description="Name of the pedigree.",
    )
    description: str | None = Field(
        default=None,
        max_length=2000,
        description="Optional description of the pedigree.",
    )


# --------------------------------------------------
# Update
# --------------------------------------------------


class PedigreeUpdate(PedigreeSchema):
    """Schema for partially updating an existing pedigree."""

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=150,
        description="Updated pedigree name.",
    )
    description: str | None = Field(
        default=None,
        max_length=2000,
        description="Updated pedigree description.",
    )

    @field_validator("name", mode="before")
    @classmethod
    def validate_name(cls, value: str | None) -> str:
        """Reject explicit null values for the pedigree name."""
        if value is None:
            raise ValueError("Pedigree name cannot be null.")

        return value


# --------------------------------------------------
# Read
# --------------------------------------------------


class PedigreeRead(PedigreeSchema):
    """Schema for returning pedigree information."""

    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
        str_strip_whitespace=True,
    )

    id: UUID
    name: str
    description: str | None
    created_at: datetime
    updated_at: datetime
