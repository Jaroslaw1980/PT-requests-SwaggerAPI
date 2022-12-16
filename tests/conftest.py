from pytest import fixture, mark
from tests.books_fixtures import *
from tests.activities_fixtures import *
from tests.authors_fixtures import *


# Group of fixtures for Books API
@mark.usefixtures("add_book_method")
@fixture
def books_add_method(add_book_method):
    return add_book_method


@mark.usefixtures("delete_book_method")
@fixture
def books_delete_method(delete_book_method):
    return delete_book_method


@mark.usefixtures("get_all_books_method")
@fixture
def books_get_all_method(get_all_books_method):
    return get_all_books_method


# Group of fixtures for Activities API
@mark.usefixtures("add_activity_method")
@fixture
def activities_add_method(add_activity_method):
    return add_activity_method


@mark.usefixtures("delete_activity_method")
@fixture
def activities_delete_method(delete_activity_method):
    return delete_activity_method


@mark.usefixtures("get_all_activities_method")
@fixture
def activities_get_all_method(get_all_activities_method):
    return get_all_activities_method


@mark.usefixtures("get_activity_method")
@fixture
def activities_get_method(get_activity_method):
    return get_activity_method


# Group of fixtures for Authors API

@mark.usefixtures("add_author")
@fixture
def author_add_method(add_author):
    return add_author


@mark.usefixtures("delete_author")
@fixture
def author_delete_method(delete_author):
    return delete_author


@mark.usefixtures("get_all_authors")
@fixture
def author_get_all_method(get_all_authors):
    return get_all_authors


@mark.usefixtures("get_author_method")
@fixture
def author_get_method(get_author):
    return get_author


@mark.usefixtures("get_book_by_bookid")
@fixture
def get_book_by_id_method(get_book_by_bookid):
    return get_book_by_bookid
