import requests
import os
from bs4 import BeautifulSoup
res=requests.get('http://www.xxbiquge.com/11_11104/')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
for mm in soup.select('.box_con'):
   i=0
   while i<len(mm.select('dd')):
      title = mm.select('dd')[i].text
      a=mm.select('a')[i]['href']
      url = 'http://www.xxbiquge.com' + a
      res1=requests.get(url)
      # print(url)
      res1.encoding='utf-8'
      soup1 = BeautifulSoup(res1.text, 'html.parser')
      # 获取当前网页书名
      dirname=mm.select('dt')[0].text
      print(dirname)
      try:
          # 创建书名文件夹
          package=os.mkdir(dirname)
      except OSError as why:
          pass
      # 获取当前目录的位置 \\转义字符
      path = os.getcwd()
      f = open(path+'\\'+dirname+'\\'+title + '.txt', 'a', encoding='utf-8')
      for nn in soup1.select('.content_read'):
         if len(nn.select('h1')) > 0:
            title1 = nn.select('h1')[0].text
            content = nn.select('#content')[0].text
            # print(content)
            f.writelines(content)
            f.close()
      # print(title,a)
      i=i+1