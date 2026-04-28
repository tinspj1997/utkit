from pydantic import BaseModel, Field


class PaginationParams(BaseModel):
    page: int = Field(1, gt=0 ,description="Page number, starting from 1")
    page_size: int = Field(10, ge=0, description="Number of items per page")
   