#deal with raw data
import re
def deal(path):
    matrix=[]
    f=open(path,encoding='utf-8')
    data=f.read()
    p=re.compile(r'(?<=PM2.5,).*?(?=\n)')
    pre=re.findall(p,data)
    for i in pre:
        strtype=i.split(',')
        for j in range(len(strtype)):
            strtype[j]=int(strtype[j])
        matrix.append(strtype)

    return matrix
