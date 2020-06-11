# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:54:49 2020

@author: andre
"""


import numpy as nps

class Boundary:

    def __init_(self, deck, matrice_generates):
        self.matrice_generates = matrice_generates
        self.deck = deck
        self.dirichlet()    
        
    def dirichlet():        
        V0 = np.zeros((1,matrice_generates.nx))
        V0[0,0] = 1
        self.matrice_generates.M[0,:] = V0
        
        
    def Neumann(self, deck, matrice_generates):
        h=float(deck.doc["Materials"]["Thermal"]["Heat Transfer Coefficient"] )        
        C2  = 2*h*matrice_generates.dx/matrice_generates.k
        Tamb=float(deck.doc["Experimental Conditions"]["Room Temperature"] )
        
        Vnx = np.zeros((1,matrice_generates.nx))
        Vnx[0,nx-2] = 2*matrice_generates.C1
        Vnx[0,nx-1] = 1-matrice_generates.C1*(self.C2+2)
        self.M[nx-1,:] = Vnx        
        self.Vamb = np.zeros((matrice_generates.nx,1))
        self.Vamb[matrice_generates.nx-1] = matrice_generates.C1*C2*Tamb # Ajout du terme constant