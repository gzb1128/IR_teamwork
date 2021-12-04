with open("ori_names.md","r",encoding="utf-8") as f:
    content=f.readlines()
    content=content[0].split()
    with open("names.md","w",encoding="utf-8") as out:
        out.write("name\n")
        for x in content:
            out.write((x+" nr\n"))