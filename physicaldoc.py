from document import Document
from datetime import date


class PhysicalDoc(Document):

    def __init__(self, id_document: int = 1, author: str = "author",
                 publication_date: date = date(1500, 1, 1), number_pag: int = 1,
                 location: str = "sector 0",    purchase_price: float = 1.0) -> object:

        self._location = location
        self._purchase_price = purchase_price

        super().__init__(id_document, author, publication_date, number_pag)

    def __del__(self):
        return super().__del__()

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, new_location: str):
        self._location = new_location

    @location.deleter
    def location(self):
        del self._location

    @property
    def purchase_price(self) -> float:
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, new_purchase_price: str):
        self._purchase_price = new_purchase_price

    @purchase_price.deleter
    def purchase_price(self):
        del self._purchase_price

    def __str__(self) -> str:
        return super().__str__()+f"""\nLocation: {self._location}\npurchase price: {self._purchase_price}"""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PhysicalDoc):
            return False
        return (self._id_document == other._id_document and
                self._author == other._author and
                self._publication_date == other._publication_date and
                self._number_pag == other._number_pag and
                self._location == other._location and
                self._purchase_price == other._purchase_price)


fecha = date(2023, 11, 14)
docu = PhysicalDoc(545454, "Samuel", fecha, 50)
print(docu)
