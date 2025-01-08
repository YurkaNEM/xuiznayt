class Book():
    def __init__(self, species, title, author, year):
        self.species = species
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return  self.species, self.title, self.author, self.year
    def get_title(self):
        return  self.title
book = Book(species="книга", title='Лунный жаворонок', author='Шеннон Месенджр', year=2012)
print(book.get_info())
print(book.get_title())