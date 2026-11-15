from pydantic import BaseModel


class CategoryCreate(BaseModel):
    # category_id: int
    category_name: str
