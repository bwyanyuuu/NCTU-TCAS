#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request as ur
from bs4 import BeautifulSoup

def bword(st,lon):
    if len(st)<lon:
        st=st+' '*(lon-len(st))
        return st
    else:
        return st
    
def getTitle(search):
    listbox=[]
    nn=0
    ad=[]
    if search != '':
        name=str(search.encode()).strip('\'b').replace('\\x','%')
        
        #nctu+ page1
        url = 'https://plus.nctu.edu.tw/discusses/?utf8=%E2%9C%93&custom_search='+name
        f = BeautifulSoup(ur.urlopen(url),'html.parser')
        num=0
        di={}
        ld=[]
        menu=[]
        #\"content\":\"  \",\"time\"
        for lld in f.find_all('tr','clickable-hover'):
            text=lld.get('onclick')
            ld.append(text[text.find('\"content\\\":\\\"')+13:text.find('\\\",\\\"time\\\"')].replace('\\\\r','\r').replace('\\\\n','\n').replace('\\\\"','\"'))
            for n in lld.find_all('td'):
                if n.get('class')==['ct_name']:
                    menu.append([]) 
                    if num<=8:
                        menu[num].append(' '+str(num+1))
                    else:
                        menu[num].append(str(num+1))
                    menu[num].append(n.get_text())            
                elif n.get('class')==['title']:
                    c=bword(n.get_text(),20)
                    menu[num].append(c)            
                elif n.get('class')==['hidden-xs','user_name']:
                    c=bword(n.get_text(),8)
                    menu[num].append(c)                       
                elif n.get('class')==['hidden-xs']:
                    
                    menu[num].append(n.get_text())
                    num+=1                       
        if len(menu)==25:        
            #nctu+ page2 up
            for a in range(2):
                url = 'https://plus.nctu.edu.tw/discusses?custom_search='+name+'&page='+str(a+2)+'&utf8=%E2%9C%93'
                f = BeautifulSoup(ur.urlopen(url),'html.parser')    
                for lld in f.find_all('tr','clickable-hover'):
                    text=lld.get('onclick')
                    ld.append(text[text.find('\"content\\\":\\\"')+13:text.find('\\\",\\\"time\\\"')].replace('\\\\r','\r').replace('\\\\n','\n'))
                    for n in lld.find_all('td'):
                        if n.get('class')==['ct_name']:
                            menu.append([]) 
                            if num<=8:
                                menu[num].append(' '+str(num+1))
                            else:
                                menu[num].append(str(num+1))
                            menu[num].append(n.get_text())            
                        elif n.get('class')==['title']:
                            c=bword(n.get_text(),20)
                            menu[num].append(c)            
                        elif n.get('class')==['hidden-xs','user_name']:
                            c=bword(n.get_text(),8)
                            menu[num].append(c)                       
                        elif n.get('class')==['hidden-xs']:    
                            menu[num].append(n.get_text())
                            num+=1 
        
        nn=num
        
        #ptt
        url = 'https://www.ptt.cc/bbs/NCTU-Teacher/search?q='+name
        request=ur.Request(url,headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'})
        f = BeautifulSoup(ur.urlopen(request),'html.parser')   
        for lld in f.find_all('div','title'):
            ad.append(lld.find('a').get('href'))
            menu.append([])
            if num<=8:
                menu[num].append(' '+str(num+1))
            else:
                menu[num].append(str(num+1))
            menu[num].append(lld.get_text().strip('\n')) 
            num+=1
        #https://www.ptt.cc/bbs/NCTU-Teacher/search?q=%E5%BE%AE%E7%A9%8D%E5%88%86
        for l in menu:
            listbox.append('  '.join(l))
    return listbox,nn,ad

def getnText(search):
    ld=[] 
    if search != '':
        name=str(search.encode()).strip('\'b').replace('\\x','%')
        
        #nctu+ page1
        url = 'https://plus.nctu.edu.tw/discusses/?utf8=%E2%9C%93&custom_search='+name
        f = BeautifulSoup(ur.urlopen(url),'html.parser')
        num=0
           
        for lld in f.find_all('tr','clickable-hover'):
            text=lld.get('onclick')
            ld.append(text[text.find('\"content\\\":\\\"')+13:text.find('\\\",\\\"time\\\"')].replace('\\\\r','\r').replace('\\\\n','\n').replace('\\\\\\"','\"').replace('\\\\u0026','＆'))
                        
        if len(ld)==25:        
            #nctu+ page2 up
            for a in range(2):
                url = 'https://plus.nctu.edu.tw/discusses?custom_search='+name+'&page='+str(a+2)+'&utf8=%E2%9C%93'
                f = BeautifulSoup(ur.urlopen(url),'html.parser')    
                for lld in f.find_all('tr','clickable-hover'):
                    text=lld.get('onclick')
                    ld.append(text[text.find('\"content\\\":\\\"')+13:text.find('\\\",\\\"time\\\"')].replace('\\\\r','\r').replace('\\\\n','\n').replace('\\\\\\"','\"').replace('\\\\u0026','＆'))
    return ld

def getpText(ad,index):
    l=[]
    a=''
    #nctu+ page1
    url = 'https://www.ptt.cc'+ad[index]
    request=ur.Request(url,headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'})
    f = BeautifulSoup(ur.urlopen(request),'html.parser') 
    for ld in f.find_all('div'):
        if ld.get('id') == 'main-content':
            a=ld.get_text()
    return a
                        


#print(type(getTitle('心理學')[1]))
#print('\r'.join(getTitle('b')))

#https://plus.nctu.edu.tw/discusses/?utf8=%E2%9C%93&custom_search=%E5%BE%AE%E7%A9%8D%E5%88%86
#.replace('\x','%')
#\"content\":\"  \",\"time\"