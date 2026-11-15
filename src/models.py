from typing import override

from sqlalchemy import Column, Float, ForeignKey, Integer, String, null

from database import Base, SessionLocal


class Categories(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, unique=True)


class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.category_id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"))

    price = Column(Float, nullable=False)


class Suppliers(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String, nullable=False)
    email = Column(String, unique=True)
