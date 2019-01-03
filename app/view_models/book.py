# -*- coding: utf-8 -*-
_Author_ = 'BUPPT'


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.author = '、'.join(book['author'])
        self.publisher = book['publisher']
        self.pages = book['pages']
        self.image = book['image']
        self.price = book['price']
        self.isbn = book['isbn']
        self.summary = book['summary']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])

        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.keyword = ''
        self.total = 0
        self.books = []

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }

        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]

        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword,
        }

        if data:
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
            returned['total'] = data['total']

        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data["title"],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'] or '',
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
