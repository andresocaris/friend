import snap
import matplotlib.pyplot as plt
import numpy as np
def read_input():
    f = open ('inputs/facebook.txt','r')
    G = snap.TNGraph.New()
    v1=[]
    v2=[]
    s=set()
    maxi=0
    while ( 1 ):
        linea = f.readline()
        if linea == "": break
        x,y =map(int,linea.split(" "))
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
    n2 = G.GetNodes() 
    PRankH3 = snap.TIntFltH()
    snap.GetPageRank(G, PRankH3)
    maxi=0
    for i in range(0,n2):
        if abs(PRankH3[i]-1)<1e-8:
            continue
        if PRankH3[i] > maxi:
            maxi= PRankH3[i]
            node=i
    print(node)
    print(maxi)
    bcf, cfprv = BCF(G, ind, 3)
    print(bcf)
    v = []
    for i in range(0,len(cfprv)):
        v.append((i,cfprv[i]))
    x=[]
    y=[]
    v.sort(key = lambda x: x[1]) 
    cnt = 0
    for i in range(0,len(v)):
        if abs(v[i][1]-1) < 1e-8:
            continue
        cnt += 1
        x.append(v[i][0])
        y.append(v[i][1])
        if cnt == 10 : break
    cnt =0
    for i in range(0,len(v)):
        if abs(v[len(v)-1-i][1]-1) < 1e-8:
            continue
        cnt += 1
        x.append(v[len(v)-1-i][0])
        y.append(v[len(v)-1-i][1])
        if cnt == 10 : break
    print(len(x))
    imprimir(x,y)

if __name__ == "__main__":
        main()
