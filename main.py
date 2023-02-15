from graph import Graph
from dij_test import DijkistraAlgo
from help import Helpers

if __name__ == '__main__':

    n = 30#int(input("Enter n = "))
    s = 5#int(input("Enter s = "))
    costs = []
    helpFucntions = Helpers()

    testing_dij = DijkistraAlgo(n)
    constructed_graph = Graph(n,s,costs)
    testing_dij.graph = costs
    store_dics = []

    nodeCostList = []
    for i in range(0,n*2):
        store_dics.append(testing_dij.dijkstra(i))

        nodeCostList.append(testing_dij.getNodeCostDict())

    same1 = []
    notSame1 = []
    heads = []
    for i in range(0,n):
        
        node1 = store_dics[i]
        node2 = store_dics[(i+s) % (n)]
        same1.append([node1["Source"],node2["Source"]])
        notSame1.append([node1["Source"],node2["Source"]])
        heads.append([node1["Source"],node2["Source"]])

        helpFucntions.compareSame(node1,node2,same1)
        helpFucntions.compareNotSame(node1,node2,notSame1)

    same2 = []
    notSame2 = []
    for i in range(0,n):
        node1 = store_dics[i+n]
        node2 = store_dics[(i+n) % (n)]
        same2.append([node1["Source"],node2["Source"]])
        notSame2.append([node1["Source"],node2["Source"]])
        heads.append([node1["Source"],node2["Source"]])

        helpFucntions.compareSame(node1,node2,same2)
        helpFucntions.compareNotSame(node1,node2,notSame2)
    

    same3 = []
    notSame3 = []
    for i in range(0,n):
        
        if i == n-1:
            node1 = store_dics[n+i]
            node2 = store_dics[n]
        else:
            node1 = store_dics[n+i]
            node2 = store_dics[(n+i+1) % (n*2)]
        same3.append([node1["Source"],node2["Source"]])
        notSame3.append([node1["Source"],node2["Source"]])
        heads.append([node1["Source"],node2["Source"]])

        helpFucntions.compareSame(node1,node2,same3)
        helpFucntions.compareNotSame(node1,node2,notSame3)

    helpFucntions.writeTextFile(n,s,costs,nodeCostList,heads,same1,same2,same2,notSame1,notSame2,notSame3)
    
    # print("Seperaetd Same costs")
    # helpFucntions.printNodes(same1)
    # helpFucntions.printNodes(same2)
    # helpFucntions.printNodes(same3)

    # print("\nSeperated diff costs")
    # helpFucntions.printNodes(notSame1)
    # helpFucntions.printNodes(notSame2)
    # helpFucntions.printNodes(notSame3)

    print("FURTHER DETAILS INSIDE TEXT FILE")

