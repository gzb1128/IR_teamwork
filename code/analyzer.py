import pandas as pd
import jieba
import jieba.posseg as divider

def analyzer():
    with open("A-Dream.txt",encoding='utf-8') as f:
        text=f.readlines()
    jieba.add_word("可卿")
    nameData=pd.read_csv("names.md")
    nameList=[]#人物名称词典
    for k in nameData.values:
        nameList.append((k.tolist()[0].split())[0])
    nameCnt={}
    relationships={}
    for line in text:#对每一个段落进行检查
        lineDivider=divider.cut(line)#用jieba词性分词
        nameStorage=[]#存储当前段落中出现的人名
        nameMark=0
        for item in lineDivider:
            #秦可卿的各种别名
            if item.word=='可卿' or item.word=='可儿' or item.word=='秦氏' or item.word=='蓉大奶奶' or item.word=='兼美':#把可卿过滤掉，顺便mark一下这段有可卿
                nameMark=1
                '''
            if item.word=="鸳鸯":
                print("find 鸳鸯",item)
            if item.word=="警幻":
                print("find 警幻",item)
            '''
            #找在人名词典中的,第一个判断可以过滤掉很多没用的东西能跑快很多
            if (item.flag!="nr" and item.flag!="n") or item.word not in nameList:
                continue
            nameStorage.append(item.word)
            if nameCnt.get(item.word) is None:
                nameCnt[item.word]=0
            nameCnt[item.word] += 1
        if(nameMark==0):
            continue
        print(nameStorage)
        for name in nameStorage:#有可卿了,扫一下别的人名
            if relationships.get(name) is None:
                relationships[name]=0
            relationships[name]+=1
    print("relationship")
    print(relationships)
    with open("relationship.md","w",encoding='utf-8') as f:
        f.write("v,w\n")
        for v,w in relationships.items():
            f.write(v+","+str(w)+"\n")




analyzer()