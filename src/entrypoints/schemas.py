"""coding=utf-8."""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class DailyProduction(BaseModel):
    chicken: int


class DetailInvoice(BaseModel):
    invoice_id: str = None
    food_id: str = None


class Invoice(BaseModel):
    client_id: str = None
    employee_id: str = None
    type: str = None
    product_ids: List[str] = None


class Product(BaseModel):
    name: str = None
    price: float = None
