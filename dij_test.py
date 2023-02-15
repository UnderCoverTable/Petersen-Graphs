
import sys

class DijkistraAlgo:

	def __init__(self, vertices):
		self.dic = {}
		self.V = vertices*2
		self.graph = None

	def printSolution(self, dist,src):
		self.dic={}
		if src < self.V //2:
			self.dic["Source"] = "V"+str(src+1)
			#print(f"Vertex \t\tSource --> V{src+1}")
		else:
			#print(f"Vertex \t\tSource --> U{src-self.V//2+1}")
			self.dic["Source"] = "U"+str(src-self.V//2+1)

		

		for node in range(self.V):
			if node < self.V//2:
				#print(f"V{node+1}		{dist[node]}")
				self.dic["V"+str(node+1)] = dist[node]
			else:
				#print(f"U{node-self.V//2+1}		{dist[node]}")
				self.dic["U"+str(node-self.V//2+1)] = dist[node]

	def getNodeCostDict(self):
		return self.dic 

	
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = sys.maxsize

		# Search not nearest vertex not in the
		# shortest path tree
		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u

		return min_index

	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):
		
			x = self.minDistance(dist, sptSet)
			
			sptSet[x] = True
			
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and \
				dist[y] > dist[x] + self.graph[x][y]:
						dist[y] = dist[x] + self.graph[x][y]

		self.printSolution(dist,src)
		return self.dic

