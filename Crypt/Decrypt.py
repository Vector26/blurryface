import os
dic={'l':'q','a':'w','j':'e','s':'r','v':'t','g':'y','k':'u','q':'i','r':'o','f':'p',
'w':'a','x':'s','e':'d','y':'f','b':'g','m':'h',
't':'j','i':'k','c':'l','h':'z','u':'x','p':'c','d':'v','n':'b',
'o':'n','z':'m','\n':'\n'}
spa=['fpr','okj','bgh','per','lkj','kjf','afk','lqw','mfd','lvf','bvw']
def decrypt():
    c=0
    filename=input("please input the filename with full path: ")
    file=input('filename with extension: ')
    f=open(filename, 'r+')
    f2=open('Decry-'+file, 'a+')
    m=""
    for i in f:
        s=i
        for op in spa:
            s=s.replace(op,' ')
        for j in s:
            if((j in dic or j.lower() in dic) and j!='\n'):
                if(j.isupper()):
                    m+=dic[j.lower()].upper()
                else:
                    m+=dic[j]
            elif(j==" "):
                m+=" "
            else:
                m+=j

        print(m)
        f2.write(m)
        m=""
    f.close()
    f2.close()
    os.system('del '+filename)

decrypt()
