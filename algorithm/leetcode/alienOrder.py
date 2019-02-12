from _collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = defaultdict(set)
        self.edges = set()
        self.allnodes = set()
    
    def addEdge(self, small, large):
        self.vertices[small].add(large)
        self.edges.add((small, large))
        self.allnodes.add(small)
        self.allnodes.add(large)

    def removeEdge(self, small, large):
        self.edges.remove((small, large))
        self.vertices[small].remove(large)
        
    def hasCycle(self):
        return None
    
    def hasCycleUtil(self):
        return None
    
    def hasIncoming(self, node):
        for edge in self.edges:
            if edge[1] == node:
                return True
        return False
    
    def findAllNoIncoming(self):
        starts = set()
        for node in self.allnodes:
            if (self.hasIncoming(node) == False) :
                starts.add(node)
        return  starts
        
    def generateTopologicalOrder(self):
        l = []
        startNodes = self.findAllNoIncoming()
        print("startNodes", startNodes)
        if len(startNodes) == 0:
            return l
        while len(startNodes) > 0:
            current = startNodes.pop()
            l.append(current)
            for next in list(self.vertices[current]):
                self.removeEdge(current, next)
                if self.hasIncoming(next) == False:
                    startNodes.add(next)
          
        if len(self.edges) > 0:
            return []    
            
        return l
    
    def __str__(self):
        return str(self.edges) + "\n" + str(self.vertices) + "\n" + str(self.allnodes)

class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        word = ""
        charset = set()
        rules = []
        
        if len(set(words))<=1:
            return "".join(set(words))
         
        for i in range(len(words)):
            for j in range(len(words[i])):
                charset.add(words[i][j])
                 
        g = Graph()
        
        for i in range(1, len(words)):
            for j in range(len(words[i-1])):
                if words[i][j] != words[i-1][j]:
                    g.addEdge(words[i-1][j], words[i][j])
                    rules.append((words[i-1][j], words[i][j]))
                    break
        print(charset)
        charset= charset - g.allnodes
        result = list(charset)
        
#         if g.hasCycle():
#             return ""
        print(g)
        

        orders = g.generateTopologicalOrder()
        if len(g.edges) > 0:
            return ""
        else:
            return "".join(orders) + "".join(charset) 
# g = Graph()
# g.addEdge("w", "b")
# g.addEdge("w", "e")
# g.addEdge("e", "r")
# g.addEdge("e", "b")
# g.addEdge("r", "t")
# g.addEdge("r", "a")
# g.addEdge("t", "f")
# print()
print(Solution().alienOrder([
"wrt","wrtkj"
]))    
# print(Solution().alienOrder([
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]))