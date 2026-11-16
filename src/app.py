from os import path
from unicodedata import category

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import delete, select
from sqlalchemy.orm import Session
# from pydantic import BaseModel, ConfigDict


from database import Base, SessionLocal, engine, get_db

from models import Categories, Products, Suppliers
from pydantic_model import CategoryCreate, ProductCreate, SupplierCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management API")


@app.get("/")
def home():
    return {"message": "Inventory API is running"}


@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Products).all()


@app.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Categories).all()
    return categories


@app.post("/products/{category_id}/{supplier_id}")
def create_a_new_product(
    category_id: int,
    supplier_id: int,
    product_create: ProductCreate,
    db: Session = Depends(get_db),
):

    new_product = Products(
        category_id=category_id, supplier_id=supplier_id, **product_create.model_dump()
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {"Created a new product under the category"}


@app.post("/create/supplier")
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):

    supply = Suppliers(**supplier.model_dump())  # pyright: ignore[reportCallIssue]

    db.add(supply)
    db.commit()
    db.refresh(supply)


@app.get("/product/{category_id}/{supplier_id}")
def get_single_product(
    category_id: int, supplier_id: int, db: Session = Depends(get_db)
):

    stmt = select(Products).where(
        Products.category_id == category_id, Products.supplier_id == supplier_id
    )

    products = db.scalars(stmt).all()
    return products


@app.delete("/delete/categories/all")
def delete_all_categories(db: Session = Depends(get_db)):

    db.execute(delete(Categories))
    db.commit()

    return {"All categories successfully deleted"}


@app.delete("/delete/categories/{category_id}")
def delete_categories(category_id: int, db: Session = Depends(get_db)):
    category = db.get(Categories, category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
    db.refresh(category)
    return {"message": "Category deleted successfully"}


@app.post("/create/category")
def create_new_categroy(category: CategoryCreate, db: Session = Depends(get_db)):

    new_category = Categories(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return {"Added a new category"}
