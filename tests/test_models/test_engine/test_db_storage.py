#!/usr/bin/python3
"""test for db storage"""
import unittest
import pep8
import json
import os
from os import getenv
import MySQLdb
from models.base_model import BaseModel, Base
from models.state import State
from models.engine.db_storage import DBStorage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO db engine found')
class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage engine'''

    @classmethod
    def setUpClass(self):
        """set up for test"""
        self.User = getenv("HBNB_MYSQL_USER")
        self.Passwd = getenv("HBNB_MYSQL_PWD")
        self.Db = getenv("HBNB_MYSQL_DB")
        self.Host = getenv("HBNB_MYSQL_HOST")
        self.db = MySQLdb.connect(host=self.Host, user=self.User,
                                  passwd=self.Passwd, db=self.Db,
                                  charset="utf8")
        self.query = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def teardown(self):
        """this will tear it down when test ends"""
        self.query.close()
        self.db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'No db engine found')
    def test_pep8_DBStorage(self):
        """Test Pep8 spec"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'No db engine found')
    def test_if_states_empty(self):
        """test if states empty"""
        self.query.execute("SELECT * FROM states")
        states = self.query.fetchall()
        self.assertEqual(len(states), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'No db engine found')
    def test_add_states(self):
        """Test add state"""
        self.query.execute("SELECT * FROM states")
        states = self.query.fetchall()
        self.assertEqual(len(states), 0)
        state = State(name="CONGO")
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT * FROM states")
        states = self.query.fetchall()
        self.assertEqual(len(states), 1)

if __name__ == "__main__":
    unittest.main()
