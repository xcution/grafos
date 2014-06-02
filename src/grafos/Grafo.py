'''
Created on 25/05/2014

@author: salazar
'''

class Grafo:
    def __init__(self, ordem, vertices = []):
        self.ordem = ordem
        self.vertices = vertices
        
    '''Adiciona um novo vertice em G'''
    def adicionarVertice(self, novoVertice):
        return 0
    
    '''"Remove um  vertice de G, juntamente com todas as conexoes"'''    
    def removerVertice(self, vertice):
        return 0
        
    '''Conecta os vertices v1 e v2 em G'''
    def conecta(self, vertice1, vertice2):
        return 0
    
    '''Desconecta os vertices v1 e v2 em G'''
    def desconecta(self, vertice1, vertice2):
        return 0
    
    '''Retorna o numero de vertices de G'''
    def ordem(self):
        return self.ordem
    
    '''Retorna um conjunto contendo os vertices de G'''
    def vertices(self):
        return self.vertices
    
    '''Retorna um vertice qualquer de G'''
    def getVertice(self):
        return 0
    
    '''Retorna um conjunto contendo os vertices adjacentes a v em G'''
    def adjacentes(self, vertice):
        return 0
    
    '''Retorna o numero de vertices adjacentes a v em G'''
    def grau(self, vertice):
        return 0
            
class Vertice:
    
    def __init__(self, rotulo, adjacentes = []):
        self.rotulo = rotulo
        self.adjacentes = adjacentes 
        
        print 'Rotulo vertice: %i' % self.rotulo
    
v = Vertice(10)