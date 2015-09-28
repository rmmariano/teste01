#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #
# # Para rodar os testes: 
# # - no shell entre na pasta: web2py/
# # - execute: python web2py.py -S NOMEPROJETO -M -R applications/NOMEPROJETO/tests/run_tests.py 
# # Assim este arquivo de encarregará de rodar os testes na pasta tests/
# #

import sys
import os

# caminho da pasta anterior a pasta atual (raiz projeto)
PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
# somente o nome do projeto
PROJECT = PROJECT_PATH.split('/')[-1]

# TODO: CRIAR FUNÇÃO PARA RECUPERAR O NOME DOS ARQUIVOS *.PY AUTOMATICAMENTE

files=['test_ctlr.py','test_mdl.py']
for f in files:
	print "\n"
	execfile("applications/"+PROJECT+"/tests/"+f, globals())









# # # Salva os caminhos das pastas que serão testadas no sys.path
# # import sys
# # import os
# # # Pasta onde fica localizado o web2py
# # W2P_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-4])
# # #W2P_PATH = "/home/rodrigo/Arquivos/web2py" #o comando acima pegara este caminho
# # # sys.path.append(os.path.abspath(W2P_PATH))
# # # sys.path.append(os.path.abspath(W2P_PATH+'/gluon'))
# # # sys.path.append(os.path.abspath(W2P_PATH+'/site-packages'))
# # # Pasta anterior a pasta atual (raiz projeto)
# # PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
# # # Pasta atual, onde o run_tests.py está
# # ROOT_PATH = os.path.dirname(__file__)
# # #adiciona no sys.path os diretorios que contém arquivos ou módulos a serem testados
# # mods=['controllers','modules','tests']
# # for m in mods:
# #     sys.path.append(os.path.abspath(PROJECT_PATH+'/'+m))


# import os
# import sys
# ROOT_PATH = os.path.dirname(__file__)
# # PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
# # sys.path.append(os.path.abspath(PROJECT_PATH+'/tests'))

# #print sys.path

# import test_here

# print dir(test_here)

# test_here.pp()

# from unittest import TestLoader, TextTestRunner, TestSuite

# if __name__ == '__main__':
#     # # Pega todos os arquivos da pasta corrente que sejam .py
#     # tests = TestLoader().discover(ROOT_PATH, "*.py")
#     # # Roda os testes
#     # # verbosity=2 aumenta o nível de detalhe da saida
#     # result = TextTestRunner(verbosity=2).run(tests) 
#     # #result = TextTestRunner().run(tests)
#     # # Se houver algum problema nos testes, fecha o programa
#     # if not result.wasSuccessful():
#     #     sys.exit(1)


#     loader = TestLoader()
#     suite = TestSuite((
#         loader.loadTestsFromTestCase(test_here.TestCtlr10)
#         ))

#     runner = TextTestRunner(verbosity = 2)
#     runner.run(suite)