vagon1 = input().split()
vagon2 = input().split()
counter = 0
size = len(vagon1)
for i in range(len(vagon1)):
    if vagon1[i]=='1' and vagon2[i]=='1':
        counter = counter+1
print(counter)