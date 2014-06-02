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
        if novoVertice in self.vertices:
            print 'Vertice ja existe no grafo'
            return -1
        self.vertices.append(novoVertice)
        print 'Vertice adicionado com sucesso'
        return 0
    
    '''
    Remove um  vertice de G, juntamente com todas as conexoes
    '''    
    def removerVertice(self, vertice):
        if vertice in self.vertices:
             
            self.vertices.remove(vertice)
            print 'Vertice removido com sucesso'
            return 0
        print 'Vertice nao existente no grafo'
        return -1
        
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
    
    '''
    Retorna um vertice qualquer de G
    '''
    def getVertice(self, rotulo):
        if not rotulo:
            return self.vertices[0]
        for i in range(len(self.vertices)):
            if self.vertices[i] == rotulo:
                return self.vertices[i]
        print 'Vertice nao existe'
        return -1
                
class Vertice:
    
    def __init__(self, rotulo, adjacentes = []):
        self.rotulo = rotulo
        self.adjacentes = adjacentes
        print 'Rotulo vertice: %i' % self.rotulo
        
    '''
    Retorna um conjunto contendo os vertices adjacentes a v em G
    '''
    def adjacentes(self, vertice):
        # lista vazia?
        if not vertice.adjacentes:
            #grafo desconexo
            return -1
        return vertice.adjacentes 
            
    '''
    Retorna o numero de vertices adjacentes a v em G
    '''
    def grau(self, vertice):
        adj = vertice.adjacentes
        if not adj:
            print 'Nao ha nenhum vertice adjacente ao vertice ' + str(vertice.rotulo) 
            return 0
        return len(adj)
                        
v1 = Vertice(1)
v2 = Vertice(2, [v1])

g = Grafo(2)

g.adicionarVertice(v1)
g.removerVertice(v2)
g.adicionarVertice(v2)
g.removerVertice(v2)
g.adicionarVertice(v1)