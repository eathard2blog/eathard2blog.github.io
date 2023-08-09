import os

# 获取当前目录下的文件列表
file_list = os.listdir()

# 创建一个HTML文件并写入文件列表
with open("index.html", "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html>\n")
    f.write("<html lang=\"zh\">\n")
    f.write("<head>\n")
    f.write("  <meta charset=\"UTF-8\">\n")
    f.write("  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    f.write("  <title>文件列表</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("  <h1>文件列表</h1>\n")
    f.write("  <ul>\n")
    for file in file_list:
        if file != "index.html":
            f.write(f"    <li><a href=\"{file}\">{file}</a></li>\n")
    f.write("  </ul>\n")
    f.write("</body>\n")
    f.write("</html>\n")