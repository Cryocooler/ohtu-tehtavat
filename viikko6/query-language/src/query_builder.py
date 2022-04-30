from hashlib import new


from matchers import *

class QueryBuilder:
    def __init__(self, query=All()):
        self.query_obj = query

    def playsIn(self, team):
        andQuery = And(self.query_obj, PlaysIn(team))
        return QueryBuilder(andQuery)

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_obj, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_obj, HasFewerThan(value, attr)))

    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))


    def build(self):
        return self.query_obj
