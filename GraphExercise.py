class Node(object):
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->'\
            + self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + '->'\
            +self.dest.getName() + ' ('\
            +str(self.getWeight()) + ')'

class Digraph(object):
    def __init__(self):
        self.edges = {}
    
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + ' -> '\
                    + dest.getName() + '\n'
        return result[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        reverse = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, reverse)

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

g.addEdge(Edge(g.getNode('ABC'),g.getNode('BAC')))
g.addEdge(Edge(g.getNode('ABC'),g.getNode('ACB')))
g.addEdge(Edge(g.getNode('BAC'),g.getNode('BCA')))
g.addEdge(Edge(g.getNode('CBA'),g.getNode('BCA')))
g.addEdge(Edge(g.getNode('CBA'),g.getNode('CAB')))
g.addEdge(Edge(g.getNode('ACB'),g.getNode('CAB')))