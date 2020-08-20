Record={}
Words=input("Text:")
Words=Words.split(' ')
length=0
for line in Words:
    if len(line)>=length:length=len(line)
    if line in Record.keys(): Record[line]+=1
    else:Record[line]=1
for line2 in Record:
    print("{:{}}".format(line2,length),":","{}".format(Record[line2]))