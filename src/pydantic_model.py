from pydantic import BaseModel


class CategoryCreate(BaseModel):
    # category_id: int
    category_name: str


class ProductCreate(BaseModel):
    product_name: str
    # category_id: int
    # supplier_id: int
    price: int


class SupplierCreate(BaseModel):
    supplier_name: str
    email: str
