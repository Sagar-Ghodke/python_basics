'''list files in folder in size'''

import os
PATH = "/home/cyberenvy/"

size=0
content=(os.listdir(PATH))
sizes=[]

# print(sizes)
for file in content:
    size+= os.path.getsize(PATH+file)
    sizes.append(size)

def selectionSort(sizes):
    for index in range(0, len(sizes)):
        x=index
        for i in range(index,len(sizes)):
            if sizes[x]>sizes[i]:
                x=i
        sizes[index], sizes[x] = sizes[x], sizes[index]
    return sizes

newlist= selectionSort(sizes)

final=list(zip(content, newlist))
print(final)





