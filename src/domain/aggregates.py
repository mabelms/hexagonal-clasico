from typing import List

from pydantic import BaseModel, Field, constr


class DailyProduction(BaseModel):
    id: str = None
    chicken: int = None


class DetailInvoice(BaseModel):
    id: int = None
    invoice_id: str = None
    food_id: str = None


class Invoice(BaseModel):
    id: str
    client_id: str = None
    employee_id: str = None
    type: str = None
    created_at: str = None
    total: str = None
    product_ids: List[str] = None


class Product(BaseModel):
    id: str
    name: str = None
    price: str = None
