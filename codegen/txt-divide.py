import os

# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 打开文件并读取内容
with open("test.txt", "r") as f:
    content = f.read()

# 将内容按照段落分割
paragraphs = content.split("\n\n")

# 遍历每个段落，提取序号和内容，并将内容保存到对应的文件中
for p in paragraphs:
    # 提取序号和内容
    index, content = p.split(". ", 1)
    index = int(index)
    
    # 生成文件名和文件路径
    filename = f"{index}.txt"
  #  filepath = f"/path/to/directory/{filename}"
    filepath = os.path.join(script_dir, filename)
  
    # 将内容保存到文件中
    with open(filepath, "w") as f:
        f.write(content)

