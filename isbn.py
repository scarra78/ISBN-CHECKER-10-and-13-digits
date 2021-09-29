
class book():
    def __init__(self, title, author, y_publish, no_pages, isbn):
        self.title = title
        self.author = author
        self.y_publish = y_publish
        self.no_pages = no_pages
        self.isbn = isbn

    def __repr__(self):
        return f" book title is {self.title}\n Author is {self.author}\n Year Published {self.y_publish}\n Number of pages {self.no_pages}\n ISBN is {self.isbn}\n"

    def cisbn(self):
        code_string = self.isbn
        x = self.isbn
        x = x.replace("-", "").replace(" ", "")
        code_string = code_string.replace("-", "").replace(" ", "")
        if len(code_string) == 10:
            if not code_string[0:8].isdigit() or not (code_string[9].isdigit() or code_string[9].lower() == "x"):
                return " not valid"
            result = 0
            for i in range(9):
                result = result + int(code_string[i]) * (10 - i)
            if code_string[9].lower() == "x":
                result += 10
            else:
                result += int(code_string[9])

            if result % 11 == 0:
                return " valid"
            else:
                return " not valid"
        elif len(x) == 13:
            diglist = [int(x) for x in x]
            if diglist[-1] == 10 - ((sum([diglist[i] for i in range(12) if i % 2 == 0]) + 3 * sum([diglist[i] for i in range(12) if i % 2 != 0])) % 10):
                return "this is a valid isbn"
        else:
            return"this is not a valid isbn"


class fantasy_novel(book):
    def __init__(self, title, author, y_publish, no_pages, isbn, genre):
        super().__init__(title, author, y_publish, no_pages, isbn)
        self.genre = genre

    def __repr__(self):
        return f" book title is {self.title}\n Author is {self.author}\n Year Published {self.y_publish}\n Number of pages {self.no_pages}\n ISBN is {self.isbn}\n and the genre is {self.genre}"


class scifi_novel(book):
    def __init__(self, title, author, y_publish, no_pages, isbn, genre):
        super().__init__(title, author, y_publish, no_pages, isbn)
        self.genre = genre

    def __repr__(self):
        return f" book title is {self.title}\n Author is {self.author}\n Year Published {self.y_publish}\n Number of pages {self.no_pages}\n ISBN is {self.isbn}\n and the genre is {self.genre}"


magician = book("magician", "raymod e fiest", 1980, 500, "978-92-95055-02-5")
print(magician.__repr__())
print(magician.cisbn())

gunslinger = fantasy_novel("magician", "steve king",
                           1980, 500, "0007525494", "Fantasy")
print(gunslinger.__repr__())

tron = scifi_novel("magician", "that dude", 1980, 500, "0007525494", "scifi")
print(tron.__repr__())


