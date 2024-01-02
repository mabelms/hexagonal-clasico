from domain.repository import ProductRepositoryAbstract
from repository.models import RepositoryU


class MerchantMarcaRepository(ProductRepositoryAbstract):
    def __init__(self, sqlalchemy_session):
        self.sqlalchemy_repo = RepositoryU(session=sqlalchemy_session)

    def get_all_product(self):
        print("------------------------------ line 12")

        asd = self.sqlalchemy_repo.get_all_product()
        print("funciono line 13")
        return asd
