#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# Importa o módulo que será testado
import fib

# Testes relacionado ao Módulo Fib
class TestModFib(unittest.TestCase):
	def test0(self):
		self.assertEqual(fib.fib(1), 1)
	def test1(self):
		self.assertEqual(fib.fib(2), 1)
	def test10(self):
		self.assertEqual(fib.fib(10), 55)


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestModFib))
unittest.TextTestRunner(verbosity=2).run(suite)


#fonte: http://www.web2py.com/AlterEgo/default/show/260