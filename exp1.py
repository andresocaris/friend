import snap
import matplotlib.pyplot as plt
import numpy as np
def read_input():
    f = open ('inputs/musae_git_edges.csv','r')
    linea = f.readline()
    G = snap.TNGraph.New()

    v1=[]
    v2=[]
    s=set()
    maxi=0
    while ( 1 ):
        linea = f.readline()
        if linea == "": break
        x,y =map(int,linea.split(","))
        v1.append(x)
        v2.append(y)
        s.add(x)
        maxi=max(x,maxi)
        maxi=max(y,maxi)
    tam = maxi
    print("numero de nodos:")
    print(tam)
    for x in range(0,tam+1):
        G.AddNode(x)
    ind=[]
    for x in range(0,tam+1):
        ind.append(0)
    for i in range(0,len(v1)):
        G.AddEdge(v1[i],v2[i])
        ind[v1[i]]+=1
    return G,ind

# Given a graph G, compute the Best Current Friend (BCF) for node v
def BCF( G, ind, v ):
    n = G.GetNodes()      # returns the number of nodes in the graph
    cfprv = []            # CFPRV: Current Friend PageRank Vector
    for j in range(0, n):
        cfprv.append(0)
    val = 1
    for j in range(0, n):
        if G.IsEdge(j+1,v) and (ind[j+1]>1):
            G.DelEdge(j+1,v)
            PRankH2 = snap.TIntFltH()
            snap.GetPageRank(G, PRankH2)
            cfprv[j]=PRankH2[v]
            val = min( val,cfprv[j])
            G.AddEdge(j+1,v)
        else:
            cfprv[j]=1
    # The BCF of a node v is defined as the adjacent node which has minimum CFPRV
    #print(cfprv)
    for j in range(0,n):
        if abs(val-cfprv[j])<1e-7:
            return j, cfprv
            
# Plot the pagerank of node's n neighbors
def plot( G, pageranks, n ):
    for u in G.Nodes():
        if u.GetId() == n:
            x = []
            pr = []
            for v in u.GetInEdges():
                x.append(v)
                pr.append(pageranks[v])
            plt.bar(x, pr)
            plt.show()
            return

def imprimir(x,y):
    objects = x
    y_pos = np.arange(len(objects))
    performance = y
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Page Rank')
    plt.title('Node')
    plt.show()
def main():
    G, ind = read_input()
    bcf, cfprv = BCF(G, ind, 4353)
    print(bcf)
    v = []
    for i in range(0,len(cfprv)):
        v.append((i,cfprv[i]))
    x=[]
    y=[]
    v.sort(key = lambda x: x[1]) 
    for i in range(0,8):
        x.append(v[i][0])
        y.append(v[i][1])
    imprimir(x,y)

if __name__ == "__main__":
        main()
