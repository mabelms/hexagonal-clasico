
import logging

from datetime import date
from domain import entity
# from exceptions import use_case_exception
# from repository import use_case_repository


def do_something(entity_model, cqrs):
    """
    Business operation.
    :param request: entity_model.UseCaseRequest
    :param repository: use_case_repository.AbstractUseCaseRepository
    :return: entity_model.UseCaseResponse
    """

    # if request is None:
    #     raise use_case_exception.UseCaseRequestException()

    logging.info(f"[**] /use_case_service.do_something")

    entity_ = entity.Product(entity_model.name, entity_model.price)

    with cqrs.storage:
        with cqrs.storage:
            cqrs.storage.products.get_all_product()
    return None


def get_all_products(cqrs):
    # return self.postgres_adapter.get_all_product()
    print("line 33 use case service ok")
    with cqrs.unified:
        products = cqrs.unified.products.get_all_product()
    return products
