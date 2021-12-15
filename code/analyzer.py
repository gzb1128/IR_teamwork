import pandas as pd
import jieba
import jieba.posseg as divider
import math

def analyzer():
    with open("A-Dream.txt",encoding='utf-8') as f:
        text=f.readlines()
    jieba.add_word("可卿")
    nameData=pd.read_csv("names.md")
    nameList=[]#人物名称词典
    for k in nameData.values:
        nameList.append((k.tolist()[0].split())[0])
    nameCnt={}
    nameIdf={}#段落为粒度的idf
    relationships={}
    relationships["秦可卿"]={}
    lineNum=0
    for line in text:#对每一个段落进行检查
        lineDivider=divider.cut(line)#用jieba词性分词
        nameStorage=[]#存储当前段落中出现的人名
        nameIdfStorage={}
        lineNum+=1
        for item in lineDivider:
            #秦可卿的各种别名
            if item.word=='可卿' or item.word=='可儿' or item.word=='秦氏' or item.word=='蓉大奶奶' or item.word=='兼美':#把可卿过滤掉，顺便mark一下这段有可卿
                item.word='秦可卿'
                item.flag='nr'
            if item.word=='贾宝玉':
                item.word='宝玉'
                item.flag='nr'
            if(item.word=='王夫人' or item.word=='凤辣子' or item.word=='王熙凤' or item.word=="熙凤" or item.word=="凤姐"):
                item.word='王熙凤'
                item.flag='nr'
            #找在人名词典中的,第一个判断可以过滤掉很多没用的东西能跑快很多
            if (item.flag!="nr" and item.flag!="n") or item.word not in nameList:
                continue
            nameStorage.append(item.word)
            if nameCnt.get(item.word) is None:#Idf和Cnt同时第一次出现
                nameCnt[item.word]=0
                nameIdf[item.word]=0
            if nameIdfStorage.get(item.word) is None:#人名在这个段落第一次出现
                nameIdfStorage[item.word]=1
                nameIdf[item.word]+=1
            if item.word=='凤姐':
                print("where is fengjie")
                return
            nameCnt[item.word] += 1
        for name1 in nameStorage:#扫一下当前段落的人名并增加他们的关系得分
            for name2 in nameStorage:
                if(name1!=name2):
                    if relationships.get(name1) is None:
                        relationships[name1]={}
                    if(relationships[name1].get(name2) is None):
                        relationships[name1][name2]=0
                    relationships[name1][name2]+=1;
    with open("relationship.csv","w",encoding='utf-8') as f:
        f.write("Source,Target,Weight\n")
        for u,e in relationships.items():
            for v,w in e.items():
               f.write(u+","+v+","+str(w)+"\n")
    with open("namecnt.csv", "w", encoding='utf-8') as f:
        f.write("Id,Label,Weight\n")
        for name, times in nameCnt.items():
            f.write(name + "," + name + "," + str(times) + "\n")
    with open("nameidf.csv", "w", encoding='utf-8') as f:
        f.write("Id,Label,Idf\n")
        for name, times in nameIdf.items():
            f.write(name + "," + name + "," + str(math.ceil(math.log2(lineNum/times))) + "\n")

def main():
    if(__name__!='__main__'):
        return
    analyzer()

main()