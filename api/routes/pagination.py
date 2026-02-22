from pydantic import BaseModel, Field


class PaginationParms(BaseModel):
    limit: int = Field(ge=0, le=100, description='limit of page')
    offset: int = Field(ge=0, description='offset of page')