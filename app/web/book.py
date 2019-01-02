from flask import jsonify, request

from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route("/book/search")
def search():
    """
    q: 关键字， ISBN
    page: 页数
    ?q=python&count=1
    """
    q = request.args['q']
    page = request.args['page']

    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)
