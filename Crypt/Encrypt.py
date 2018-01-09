import os
dic ={'q':'l','w':'a',
'e':'j',
'r':'s',
't':'v','y':'g','u':'k','i':'q','o':'r','p':'f','a':'w','s':'x','d':'e','f':'y','g':'b','h':'m','j':'t','k':'i','l':'c','z':'h','x':'u','c':'p','v':'d','b':'n','n':'o','m':'z','\n':'\n'}
spa=['fpr','okj','bgh','per','lkj','kjf','afk','lqw','mfd','lvf','bvw']
def encrypt():
    c=0
    filename=input("please input the filename with full path: ")
    file=input('filename with extension: ')
    f=open(filename, 'r+')
    f2=open('Encr-'+file, 'a+')
    m=""
    for i in f:
        s=i
        for j in s:
            if((j in dic) or j.lower() in dic):
                if(j.isupper()):
                    m+=dic[j.lower()].upper()
                else:
                    m+=dic[j]
            elif(j==" "):
                if(c>10):
                    c=0
                m+=spa[c]
                c+=1
            else:
                m+=j
        f2.write(m)
        print(m)

        m=""
    f.close()
    f2.close()
    os.system('del '+filename)

encrypt()