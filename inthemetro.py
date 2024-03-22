vagon1 = input().split()
vagon2 = input().split()
count = 0
size = len(vagon1)
for i in range(len(vagon1)):
    if vagon1[i]=='1' and vagon2[i]=='1':
        count = count+1
print(count)