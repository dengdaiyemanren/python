# -*- coding: utf-8 -*-

class SqliteCilent(object):
    def __init__(self):
        self.con = SimpleSQLite("pandas_df.sqlite")