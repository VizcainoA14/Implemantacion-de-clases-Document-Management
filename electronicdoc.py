from datetime import datetime, date
from document import Document


class ElectronicDoc (Document):

    def __init__(self, id_document: int = 1, author: str = "author",
                 publication_date: date = date(1500, 1, 1), number_pag: int = 1,
                 rental_date: datetime = datetime(2000, 12, 1, 23, 59, 59),
                 return_date: datetime = datetime(2000, 12, 2, 23, 59, 59),
                 url: str = "www", rental_price: float = 1.0) -> object:
        self._url = url
        self._rental_date = rental_date
        self._return_date = return_date
        self._rental_price = rental_price

        super().__init__(id_document, author, publication_date, number_pag)

    def __del__(self):
        return super().__del__()

    @property
    def rental_price(self) -> datetime:
        return self._rental_price

    @rental_price.setter
    def rental_price(self, new_rental_price):
        self._rental_price = new_rental_price

    @rental_price.deleter
    def rental_price(self):
        pass

    @property
    def rental_date(self) -> datetime:
        return self._rental_date

    @rental_date.setter
    def rental_date(self, new_rental_date):
        self._rental_date = new_rental_date

    @rental_date.deleter
    def rental_date(self):
        pass

    @property
    def return_date(self) -> datetime:
        return self._return_date

    @return_date.setter
    def return_date(self, new_return_date):
        self._return_date = new_return_date

    @return_date.deleter
    def return_date(self):
        pass

    def __str__(self) -> str:
        return super().__str__()+f"""\nURL: {self._url}\nrental_date: {self._rental_date}\nreturn_date: {self._return_date}\nrental price: {self._rental_price}"""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ElectronicDoc):
            return False
        return (self._id_document == other._id_document and
                self._author == other._author and
                self._publication_date == other._publication_date and
                self._number_pag == other._number_pag and
                self._rental_date == other._rental_date and
                self._return_date == other._return_date)


fecha = date(2023, 11, 14)
docu = ElectronicDoc(545454, "andres", fecha, 50)
print(docu)
