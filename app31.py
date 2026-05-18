class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read_pages = 0

    def info(self):
        print(self.title)
        print(self.author)
        print(self.pages)

    def read(self, page):
        self.read_pages += page
        print("Oqildi:", self.read_pages)

    def finish(self):
        if self.read_pages >= self.pages:
            print("Kitob tugadi")
        else:
            print("Hali tugamagan")

    def reset(self):
        self.read_pages = 0
        print("Qayta boshlandi")

    def summary(self):
        print(self.title, "-", self.author)

    def add_pages(self, p):
        self.pages += p
        print("Yangi sahifa:", self.pages)

    def bookmark(self):
        print("Bookmark qoyildi")

    def rate(self, star):
        print("Reyting:", star)


b1 = Book("Python Basics", "John", 200)

b1.info()
b1.read(50)
b1.bookmark()
b1.rate(5)
b1.summary()
b1.add_pages(20)
b1.finish()
b1.reset()