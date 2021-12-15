## 部署流程：
1. 运行`parser.py`
2. 运行`analyzer.py`
3. 运行`draw.py`
4. 在gephi中导入节点文件`nameparser.csv`，导入边文件`relationparser.csv`

## 文件
1. `analyzer.py`: 分析器，获取`names.md`中格式化的人名信息并且抓取红楼梦文本进行分析,
7. `drawer.py`: 产生`relationparser.csv`和`nameparser.csv`为与秦可卿相关的人物的名称和关系得分，
2. `ori_names.md`: 从网上扒的红楼梦人名表,
3. `parser.py`: 用于对`ori_names.md`进行格式化,
4. `names.md`: `ori_names`格式化得到的结果,
5. `relationship.csv`: `analyzer.py`的产出，表明秦可卿与其他人物发生交集的次数,
6. `nameidf.csv`: `analyzer.py`的产出，表明人物以段落为粒度的idf值，
7. `namecnt.csv`: `analyzer.py`的产出，表明人物在全文中出现的次数，目前在项目中还无应用场景，
8. `relationparser.csv`: `drawer.py`的产出
9. `nameparser.csv`: `drawer.py`的产出
10. `A-Dream.txt`: 红楼梦文本