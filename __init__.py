import contextlib
import sqlite3


# TODO: create the `links` table definition here.
# HINT: should have columns for the long and short
# links, and whatever else your shortening algo
# needs.
# HINT: think about what to do if the table already
# exists.
LINKS_TABLE_DDL = '''

'''


class Store:

    @classmethod
    def initialize(cls):
        cls.setup()

        return cls

    @classmethod
    def connection(cls):
        connection = sqlite3.connect('store.db')
        connection.row_factory = sqlite3.Row

        return connection

    @classmethod
    def setup(cls):
        with contextlib.closing(cls.connection()) as con:
            with con:
                con.execute(LINKS_TABLE_DDL)

        return True

    @classmethod
    def find(cls, short_link):
        # TODO: implement code that, given a short_link, finds
        # the corresponding long_link in our database.
        # HINT: think about what happens if no long link
        # exists.
        with contextlib.closing(cls.connection()) as con:
            with con:
                with contextlib.closing(con.cursor()) as cursor:
                    # HINT: find the record here. note that
                    # the above context manager will
                    # autocommit / rollback, so you can safely
                    # just do cursor.execute(your_sql)
                    raise NotImplementedError

    @classmethod
    def create(cls, long_link, short_link):
        # TODO: implement code that creates a link record
        # in the `links` table.
        with contextlib.closing(cls.connection()) as con:
            with con:
                # HINT: create the record here. note that
                # the immediately above context manager will
                # autocommit / rollback, so you can safely
                # just do con.execute(your_sql)
                raise NotImplementedError
