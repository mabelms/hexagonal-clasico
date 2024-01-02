from fastapi import APIRouter, Request

from services.use_case_service import get_all_products
from application.use_cases.daily_production import Sale
from entrypoints.schemas import DailyProduction, Invoice, Product

router = APIRouter(prefix='/sales')


@router.post("/daily_production/")
def create_daily_production(request: Request, daily_production: DailyProduction):
    sale = Sale()
    sale.save_daily_production(daily_production)


@router.get("/daily_production/")
def get_daily_production(request: Request):
    sale = Sale()
    production = sale.get_daily_production()
    return production


@router.post("/invoice/")
def create_invoice(request: Request, invoice: Invoice):
    sale = Sale()
    sale.save_invoice(invoice)

from repository.cqrs import cqrs
@router.get("/get-product/")
def get_product(request: Request):
    sale = Sale()
    products = sale.get_all_product(cqrs)
    get_all_products(cqrs)
    return products


@router.post("/product/")
def create_product(request: Request, product: Product):
    sale = Sale()
    sale.save_product(product)
    return product


@router.get("/invoices/")
def get_product(request: Request):
    sale = Sale()
    products = sale.get_all_invoice()
    return products

import requests


@router.get("/category/")
def get_category(name):
    params = {'name': name}
    try:
        url = 'http://127.0.0.1:8085/get-category/'
        response = requests.get(url, params=params)
        return response.json()

    except requests.exceptions.HTTPError as error:
        print(error)
