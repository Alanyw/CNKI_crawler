# -*- coding: cp936 -*-
#author:ѩ֮��
#---------------------

import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re
import time
import httplib
import Cookie
def readtxt(path):
    url=[]
    with open(path,'r') as txt:
        url=txt.readlines()
    return url
'''��½��ҳ����ȡ��ҳ'''
hosturl='http://www.cnki.net/'
#����cookie
httplib.HTTPConnection.debuglevel = 1
cookie = cookielib.CookieJar()

#����һ���µ�opener��ʹ��cookiejar
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie),urllib2.HTTPHandler)
#post��ַ
posturl='http://epub.cnki.net/kns/brief/result.aspx?dbprefix=scdb&action=scdbsearch&db_opt=SCDB'
#����ͷ�ṹ��ģ�������
headers={'Connection':'Keep-Alive',
         'Accept':'text/html,*/*',
         'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36',
         'Referer':posturl}
#ͨ��chormeץ����ȡpostdata

#֪���Ĳ���������UTF8���룬����������Ҫ��gbk�����ٽ���utf-8����
DbCatalog='�й�ѧ��������������ܿ�'.decode('gbk').encode('utf8')
magazine='����ѧ��'.decode('gbk').encode('utf8')
txt='����'.decode('gbk').encode('utf8')
times=time.strftime('%a %b %d %Y %H:%M:%S')+' GMT+0800 (�й���׼ʱ��)'
parameters={'ua':'1.21',
            'PageName':'ASP.brief_result_aspx',
            'DbPrefix':'SCDB',
            'DbCatalog':DbCatalog,
            'ConfigFile':'SCDB.xml',
            'db_opt':'CJFQ,CJFN,CDFD,CMFD,CPFD,IPFD,CCND,CCJD,HBRD',
            'base_special1':'%',
            'magazine_value1':magazine,
            'magazine_special1':'%',
            'txt_1_sel':'SU',
            'txt_1_value1':txt,
            'txt_1_relation':'#CNKI_AND',
            'txt_1_special1':'=',
            'his':'0',
            '__':times}
postdata=urllib.urlencode(parameters)

query_string=urllib.urlencode({'pagename':'ASP.brief_result_aspx','DbCatalog':'�й�ѧ��������������ܿ�',
                               'ConfigFile':'SCDB.xml','research':'off','t':int(time.time()),
                               'keyValue':'����','dbPrefix':'SCDB',
                               'S':'1','spfield':'SU','spvalue':'����',
                               })
#��������


url='http://epub.cnki.net/KNS/request/SearchHandler.ashx?action=&NaviCode=*&'
url2='http://epub.cnki.net/kns/brief/brief.aspx?'
#��Ҫ�����ύ����һ���ύ���󣬵ڶ������ؿ��
req=urllib2.Request(url+postdata,headers=headers)
html=opener.open(req).read()


req2=urllib2.Request(url2+query_string,headers=headers)

#print req.get_header(),req.header_items()
#����ҳ����½�ɹ�
result2 = opener.open(req2)

html2=result2.read()

##with open('web2.html','w') as e:
##    e.write(html2)

def Regular(html):
    reg='<a href="(.*?)"\ttarget'
    comlists=re.findall(re.compile(reg),html)
    return comlists

t=Regular(html2)
print t  
