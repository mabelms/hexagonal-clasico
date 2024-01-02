from typing import List


# Event repositoryd abstract
class ProductRepositoryAbstract:
    """
    Event repositoryd to given coherency to the concrete repositories
    """

    def get_all_product(self):
        pass
