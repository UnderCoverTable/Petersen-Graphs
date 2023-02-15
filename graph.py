
class Graph:

    def __init__(self,n,s,graph_list=[]):
        self.vertices = n*2
        self.verticesSpacing = s
        self.graphStore = graph_list

        self.make_v_graph(self.vertices,self.graphStore)
        self.make_u_graph(self.vertices,self.graphStore)
        
        

    def make_v_graph(self,n,graph_list):

        half_list = n//2
        turn = -1

        for j in range(0,half_list):

            i_fill = [0 for x in range(n)]
            turn += 1

            for i in range(0,n):

                if (turn+self.verticesSpacing) > (half_list-1) or (turn+half_list-self.verticesSpacing) > (half_list-1): # To wrap around 

                    i_fill[abs((turn+self.verticesSpacing) % (half_list))] = 1
                    i_fill[abs((turn+half_list-self.verticesSpacing) % (half_list))] = 1

                else: # normal case
                    i_fill[turn + self.verticesSpacing] = 1
                    i_fill[turn + (half_list-self.verticesSpacing)] = 1

                i_fill[turn + half_list] = 1 # connects u node

            graph_list.append(i_fill)


    def make_u_graph(self,n,graph_list):
        turn = -1
        half = (n//2)

        for j in range(0,(n//2)):
            i_fill = [0 for x in range(n)]
            turn += 1

            for i in range(0,n):
                if turn == (half - 1):
                    i_fill[half] = 1
                    i_fill[((half+turn) - 1) ] = 1

                if turn == 0:
                    i_fill[((half+turn) + 1) ] = 1
                    i_fill[(half+(half-1)) ] = 1

                if turn != 0 and turn != (half-1):
                    i_fill[((half+turn) + 1) ] = 1
                    i_fill[((half+turn) - 1) ] = 1

                i_fill[turn] = 1


            graph_list.append(i_fill)
            



# t = Graph(11)
# e=1
# for i in t.graphStore:
    
#     print(e,i)
#     e+=1
    
    
# 1  [0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
# 2  [0, 0, 0, 1, 1, 0, 1, 0, 0, 0]
# 3  [1, 0, 0, 0, 1, 0, 0, 1, 0, 0]
# 4  [1, 1, 0, 0, 0, 0, 0, 0, 1, 0]
# 5  [0, 1, 1, 0, 0, 0, 0, 0, 0, 1]

# 6  [1, 0, 0, 0, 0, 0, 1, 0, 0, 1]
# 7  [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]
# 8  [0, 0, 1, 0, 0, 0, 1, 0, 1, 0]
# 9  [0, 0, 0, 1, 0, 0, 0, 1, 0, 1]
# 10 [0, 0, 0, 0, 1, 1, 0, 0, 1, 0]