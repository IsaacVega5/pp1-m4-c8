class Books:

    def __init__(self, id, name, publisher, year, edition, authors):
        self.id = id
        self.name = name
        self.publisher = publisher
        self.year = year
        self.edition = edition
        self.authors = authors

    def __dict__(self):
        return {
            "patient_id": self.id,
            "name": self.name,
            "publisher": self.publisher,
            "year": self.year,
            "edition": self.edition,
            "authors": self.authors
        }
