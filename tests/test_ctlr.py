#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestCtlr10(unittest.TestCase):
	def setUp(self):
		execfile("applications/teste01/controllers/10.py", globals())
		db(db.game.id>0).delete()  # Clear the database
		db.commit()

	def test_index(self):
		self.assertEquals(index(),"index")

	def test_ctlr01(self):
		self.assertEquals(ctlr01(),[0,1,2,3,4])

	def test_ctlr02(self):
		self.assertEquals(ctlr02(),{"oi":"huebr"})

	def test_ctlr03(self):
		self.assertEquals(ctlr03(),10)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestCtlr10))
unittest.TextTestRunner(verbosity=2).run(suite)


#fonte: http://www.web2py.com/AlterEgo/default/show/260