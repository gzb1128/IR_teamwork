## 部署流程：
1. 运行`parser.py`
2. 运行`analyzer.py`

## 文件
1. `analyzer.py`: 分析器，获取`names.md`中格式化的人名信息并且抓取红楼梦文本进行分析,
2. `ori_names.md`: 从网上扒的红楼梦人名表,
3. `parser.py`: 用于对`ori_names.md`进行格式化,
4. `names.md`: `ori_names`格式化得到的结果,
5. `relationship.md`: `analyzer.py`的产出，表明秦可卿与其他人物发生交集的次数,
6. `A-Dream.txt`: 红楼梦文本
