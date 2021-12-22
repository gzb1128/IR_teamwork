import pandas as pd
import math
def TakeThird(a):
    return a[2]
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

    MajorPerson = list()
    MajorPerson.append("宝玉")
    MajorPerson.append("贾蓉")
    MajorPerson.append("贾珍")
    MajorPerson.append("秦钟")
    MajorPerson.append("王熙凤")
    MajorPerson.append("警幻")
    MajorPerson.append("尤氏")
    MajorPerson.append("贾母")
    MPdict = {}
    MPdict["宝玉"] = math.ceil(relation["秦可卿"]["宝玉"] * 0.12)
    MPdict["贾蓉"] = math.ceil(relation["秦可卿"]["贾蓉"] * 0.12)
    MPdict["贾珍"] = math.ceil(relation["秦可卿"]["贾珍"] * 0.12)
    MPdict["秦钟"] = math.ceil(relation["秦可卿"]["秦钟"] * 0.12)
    MPdict["王熙凤"] = math.ceil(relation["秦可卿"]["王熙凤"] * 0.1)
    MPdict["警幻"] = math.ceil(relation["秦可卿"]["警幻"] * 0.1)
    MPdict["尤氏"] = math.ceil(relation["秦可卿"]["尤氏"] * 0.1)
    MPdict["贾母"] = math.ceil(relation["秦可卿"]["贾母"] * 0.1)

    for link in relationship_data_list:
        if link[0] in MajorPerson:
            if relation['秦可卿'].get(link[1]) is None:
                relation["秦可卿"][link[1]] = 0
            relation['秦可卿'][link[1]] += MPdict[link[0]] #双向的，所以只算一边

    SortList = list()
    for u,e in relation.items():
        for i,j in e.items():
            if u == '秦可卿' and j >= 1500:
                SortList.append((u, i, j))
    SortList.sort(key = TakeThird, reverse = 1)
    with open("relationparser.csv","w",encoding='utf-8') as f:
        f.write("Source,Target,Weight\n")
        for a in SortList:
            f.write(a[0] +","+a[1]+","+str(a[2])+"\n")
            if (relative.get(a[1]) is None):
                relative[a[1]] = 1
    with open("nameparser.csv", "w", encoding='utf-8') as f:
        f.write("Id,Label,Weight\n")
        for name in namenode_data_list:
            if relative.get(name[0]) is not None and relation["秦可卿"][name[0]] >= 1500:
                f.write(name[0] + "," + name[1] + "," + str(name[2]) + "\n")
    
    
def main():
    if(__name__!='__main__'):
        return
    drawerParser()

main()