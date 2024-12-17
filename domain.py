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
            "id": self.id,
            "name": self.name,
            "publisher": self.publisher,
            "year": self.year,
            "edition": self.edition,
            "authors": self.authors
        }

class Lending:

    def __init__(self, book_id, user_id, start_date, end_date):
        self.book_id = book_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date

    def __dict__(self):
        return {
            "book_id": self.book_id,
            "user_id": self.user_id,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
