import snap
f = open ('musae_git_edges.csv','r')
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
    print(x," ",y)
    G.AddEdge(x,y)
    ind[x]+=1

def BCF( x ):
    n = G.GetNodes()
    v = []
    for j in range(0,n):
        v.append(0)
    val = 100
    for j in range( 0, n):
        if G.IsEdge(j+1,x) and (ind[j+1]>1):
            G.DelEdge(j+1,x)
            PRankH2 = snap.TIntFltH()
            snap.GetPageRank(G, PRankH2)
            v[j]=PRankH2[x]
            val = min( val,v[j])
            G.AddEdge(j+1,x)
        else:
            v[j]=100
    for j in range(0,n):
        if abs(val-v[j])<1e-8:
            return j+1
            
print(BCF(100))


