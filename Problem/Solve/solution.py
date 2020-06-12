import numpy as np

class Solution:
    
    def _init(self, deck, matrice_generates, initial_conditions, boundary):
        
        self.deck = deck
        self.matrice_generates = matrice_generates
        self.initial_conditions = initial_conditions
        self.boundary = boundary
        self.solve_equation()
    
    def solve_equation(self):
        
        self.nt = int(float(deck.doc["Simulation"]["time"])/matrice_generates.dt+1)
        self.Ttot = initial_conditions.T
        for t in range (self.nt-1):
            initial_conditions.T = np.dot(matrice_generates.M,initial_conditions.T)+boundary.Vamb
            self.Ttot = np.append(self.Ttot,initial_conditions.T,axis=1)