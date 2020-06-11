# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:00:27 2020

@author: andre
"""


cwd = os.getcwd()
#All the data from deck.yaml is now in the following deck variable
deck = Deck( cwd + "/data.yaml" )

matrice_generaters=matrice_generates(deck)
dirichlet=dirichlet(matrice_generator)
