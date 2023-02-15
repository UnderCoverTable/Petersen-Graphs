class Helpers:
    def compareSame(self,node1,node2,same):
        node1Vals =[]
        node2Vals = []
        for key, value in list(node1.items())[1:]:
            node1Vals.append([key,value])

        for key, value in list(node2.items())[1:]:    
            node2Vals.append([key,value])

        for i in range(0,len(node1Vals)):
            if node1Vals[i][1] == node2Vals[i][1]:
                same.append(node1Vals[i][0])

        return same

    def compareNotSame(self,node1,node2,same):
        node1Vals =[]
        node2Vals = []
        for key, value in list(node1.items())[1:]:
            node1Vals.append([key,value])

        for key, value in list(node2.items())[1:]:    
            node2Vals.append([key,value])

        for i in range(0,len(node1Vals)):
            if node1Vals[i][1] != node2Vals[i][1]:
                same.append(node1Vals[i][0])

        return same


    def printNodes(self,same_list):
        printList = []
        print()

        for i in range(0,len(same_list)):
            if type(same_list[i]) == list:
                head = same_list[i]

                j = i+1
                while type(same_list[j]) != list:
                    printList.append(same_list[j])
                    j+=1
                    if j >= len(same_list):
                        break

                print(f"{head} --> {[i for i in printList]}")
                printList = []

    def writeTextFile(self,n,s,costMatrix,dictsList,dictHeads,same1,same2,same3,notSame1,notSame2,notSame3):
        with open("P("+str(n)+","+str(s)+")"+".txt",'w') as f:
            
            f.writelines("COSTS:\n")

            for i in range(0,len(costMatrix)):
                if i < 9:
                    whitespacezero = "0"
                else:
                    whitespacezero = ""

                if i < len(costMatrix)//2:
                    f.writelines("V "+whitespacezero+str(i+1)+" = ")
                else:
                    f.writelines("U "+whitespacezero+str(i+1)+" = ")

                for j in costMatrix[i]:
                    
                    f.writelines(str(j)+" ")
                f.writelines("\n")

            f.writelines("\n")

            f.writelines("Vertice Comparison\n\n")
            for i in range(0,len(dictHeads)):
                currentCompare = dictHeads[i]
                h1 = currentCompare[0]
                h2 = currentCompare[1]
                
                for i in range(0,len(dictsList)):
                    if dictsList[i]["Source"] == h1:
                        h1dict = dictsList[i]
                    if dictsList[i]["Source"] == h2:
                        h2dict = dictsList[i] 

                f.writelines(f"Vertex    {h1}       {h2}\n")

                for v in range (0,len(list(h1dict.keys())[1:])):
                    if len(list(h1dict.keys())[1:][v]) > 2:
                        f.writelines(f"{list(h1dict.keys())[1:][v]}       {list(h1dict.values())[1:][v]}        {list(h2dict.values())[1:][v]}")
                    else:
                        f.writelines(f"{list(h1dict.keys())[1:][v]}        {list(h1dict.values())[1:][v]}        {list(h2dict.values())[1:][v]}")
                    
                    f.writelines("\n")
                f.writelines("\n")

            f.writelines("Nodes with same costs: \n")

            listOfSames = [same1,same2,same3,notSame1,notSame2,notSame3]
            for i in range(0,len(listOfSames)):
                if i==3:
                    f.writelines("Nodes with diff costs: \n")
                currList = listOfSames[i]
                printList = []
                for i in range(0,len(currList )):
                    if type(currList [i]) == list:
                        head = currList[i]

                        j = i+1
                        if j >= len(currList):
                            break
                        while type(currList [j]) != list:
                            printList.append(currList [j])
                            j+=1
                            if j >= len(currList ):
                                break

                        f.writelines(f"{head} --> {[i for i in printList]}")
                        f.writelines("\n")
                        printList = []

                f.writelines("\n")
        f.close()
            








