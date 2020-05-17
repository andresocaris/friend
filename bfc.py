import snap
import matplotlib.pyplot as plt

def read_input():
    f = open ('inputs/musae_git_edges.csv','r')
    linea = f.readline()
    G = snap.TNGraph.New()
    for x in range(0,50000):
        G.AddNode(x)
    ind=[]
    for x in range(0,50000):
        ind.append(0)
        
    while ( 1 ):
        linea = f.readline()
        if linea == "": break
        x,y =map(int,linea.split(","))
        #print(x," ",y)
        G.AddEdge(x,y)
        ind[x]+=1
    return G,ind

# Given a graph G, compute the Best Current Friend (BCF) for node v
def BCF( G, ind, v ):
    n = G.GetNodes()      # returns the number of nodes in the graph
    cfprv = []            # CFPRV: Current Friend PageRank Vector
    for j in range(0, n):
        cfprv.append(0)
    val = 100
    for j in range(0, n):
        if G.IsEdge(j+1,v) and (ind[j+1]>1):
            G.DelEdge(j+1,v)
            PRankH2 = snap.TIntFltH()
            snap.GetPageRank(G, PRankH2)
            cfprv[j]=PRankH2[v]
            val = min( val,cfprv[j])
            G.AddEdge(j+1,v)
        else:
            cfprv[j]=100
    # The BCF of a node v is defined as the adjacent node which has minimum CFPRV
    for j in range(0,n):
        if abs(val-cfprv[j])<1e-8:
            return j+1, cfprv
            
# Plot the pagerank of node's n neighbors
def plot( G, pageranks, n ):
    for u in G.Nodes():
        if u.GetId() == n:
            x = []
            pr = []
            for v in u.GetOutEdges():
                x.append(v)
                pr.append(pageranks[v])
            plt.bar(x, pr)
            plt.show()
            return


def main():
    G, ind = read_input()
    bcf, cfprv = BCF(G, ind, 100)
    print(bcf)
    plot(G, cfprv, 3)

if __name__ == "__main__":
        main()
