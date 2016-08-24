"""
Sample file for trying sqlite binding from SQLObject

http://www.sqlobject.org/
"""
import os
from sqlobject import (
    SQLObject, StringCol, IntCol, ForeignKey,
    connectionForURI, sqlhub)


class Response(SQLObject):
    """
    Represents table in Sqlite
    """
    text = StringCol()
    occurence = IntCol()


class Statement(SQLObject):
    """
    Represents table in database
    """
    text = StringCol()
    response = ForeignKey('Response')


def file_path(file_name):
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    directory_sep = os.path.sep
    return directory_sep.join([current_dir_path, file_name])


def create_connection(file_name):
    if os.path.exists(file_name):
        os.unlink(file_name)
    _scheme = 'sqlite:' + file_name
    conn = connectionForURI(_scheme)
    sqlhub.processConnection = conn
    return conn

if __name__ == '__main__':
    _path = file_path("library.db")
    connection = create_connection(_path)

    # create table
    Response.createTable()

    # add records to table
    response_1 = Response(text="Hi", occurence=12)
    response_2 = Response(text="How are you", occurence=34)
    response_3 = Response(text="I'm fine", occurence=44)
    response_4 = Response(text="Hi", occurence=12)

    # update a record
    response_2.set(text="Bye")

    # fetch single item
    print Response.get(1)

    # count of all records
    print Response.select().count()

    # fetching miltiple
    Response._connection.debug = True
    _sicps = Response.selectBy(text="Hi")
    print _sicps.count()
    for book in _sicps:
        print book.text
