from datetime import date
from abc import abstractmethod


class Document(object):

    def __init__(self, id_document: int = 1, author: str = "author",
                 publication_date: date = date(1500, 1, 1), number_pag: int = 1) -> object:

        self._id_document = id_document
        self._author = author
        self._publication_date = publication_date
        self._number_pag = number_pag

    def __del__(self):
        pass

    @property
    def id_document(self) -> int:
        return self._id_document

    @id_document.setter
    def id_document(self, new_id_document: int):
        self._id_document = new_id_document

    @id_document.deleter
    def id_document(self):
        del self._id_document

    @property
    def author(self) -> str:
        return self._author

    @ author.setter
    def author(self, new_author: str):
        self._author = new_author

    @author.deleter
    def author(self):
        del self._author

    @property
    def publication_date(self) -> date:
        return self._publication_date

    @publication_date.setter
    def publication_date(self, new_publication_date: date):
        self._publication_date = new_publication_date

    @publication_date.deleter
    def publication_date(self):
        del self._publication_date

    @property
    def number_pag(self) -> int:
        return self._number_pag

    @number_pag.setter
    def number_page(self, new_number_page: int):
        self._number_pag = new_number_page

    @number_pag.deleter
    def number_pag(self):
        del self._number_pag

    # def __str__(self):
        # return {"ID": self._id_document, "Author": self._author, "publication date": self._publication_date, "Number of pages": self._number_pag}

    @abstractmethod
    def __str__(self) -> str:
        return f"""\nId: {self._id_document}\nAuthor: {self._author}\npublication date: {self._publication_date}\nNumber of pages: {self._number_pag}"""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Document):
            return False
        return (self._id_document == other._id_document and
                self._author == other._author and
                self._publication_date == other._publication_date and
                self._number_pag == other._number_pag)


fecha = date(2023, 11, 14)
docu = Document(545454, "andres", fecha, 50)
print(docu)
