import pyclesperanto_prototype as cle

all = ""
for key in cle.operations():
    all = all + key + ", "

filename = "index.rst"
index = open(filename).readlines()
new_index = []
for line in index:
    if ":members:" in line:
        line = "   :members: " + all
    new_index = new_index + [line]

result = open(filename, "w+")
result.writelines(new_index)
result.close()
