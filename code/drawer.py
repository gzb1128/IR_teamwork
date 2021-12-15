import pandas as pd
import math

def drawerParser():
    relationship_data = pd.read_csv('relationship.csv')
    namenode_data = pd.read_csv('namecnt.csv')
    nameidf_data = pd.read_csv('nameidf.csv')
    relationship_data_list = relationship_data.values.tolist()
    namenode_data_list = namenode_data.values.tolist()
    nameidf_data_list = nameidf_data.values.tolist()
    nameidf={}
    for item in nameidf_data_list:
        nameidf[item[0]]=item[2]

    relative={}
    for link in relationship_data_list:
        if link[0]=='秦可卿' or link[1]=='秦可卿':
            relative[link[0]]=relative[link[1]]=1
    relation={}
    for link in relationship_data_list:
        if link[0]=='秦可卿' or link[1]=='秦可卿':
            if relative.get(link[0]) is not None and relative.get(link[1]) is not None:
                if(relation.get(link[0]) is None):
                    relation[link[0]]={}
                relation[link[0]][link[1]]=link[2]*nameidf[link[0]]*nameidf[link[1]]
    #            if(link[0]!="秦可卿" and link[1]!="秦可卿"):#与秦可卿相关的人相连的不包含秦可卿的边，用tf idf
    #                relation[link[0]][link[1]]=math.log2(1+link[2])
                relation[link[0]][link[1]]=math.ceil(relation[link[0]][link[1]])

    
    with open("relationparser.csv","w",encoding='utf-8') as f:
        f.write("Source,Target,Weight\n")
        for u,e in relation.items():
            for v,w in e.items():
                if relative.get(u) is not None and relative.get(v) is not None:
                    f.write(u+","+v+","+str(w)+"\n")
    with open("nameparser.csv", "w", encoding='utf-8') as f:
        f.write("Id,Label,Weight\n")
        for name in namenode_data_list:
            if relative.get(name[0]) is not None:
                f.write(name[0] + "," + name[1] + "," + str(name[2]) + "\n")
    
    
def main():
    if(__name__!='__main__'):
        return
    drawerParser()

main()