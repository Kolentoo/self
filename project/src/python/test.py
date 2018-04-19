
from urllib import request
from bs4 import BeautifulSoup
import time
import re


# 目标地址
url = "https://www.bilibili.com/"
# 头文件反爬虫
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mob'}
# 模拟浏览器打开页面
page_info = request.urlopen(url).read()
page_info = page_info.decode('utf-8')

# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser') 
# print(soup.prettify())
titles = soup.find_all('a')
for title in titles: 
    print(title.string) 

#open()是读写文件的函数,with语句会自动close()已打开文件  
#在磁盘以只写的方式打开/创建一个名为 articles 的txt文件  
with open(r"F:\python\data.txt","w") as file:       
    for title in titles:  
        file.write(title.text)  
        file.write("https://www.bilibili.com/" + title.get('href')+'\n\n') 

links = soup.find_all('img')
path=r'F:\python'
for link in links:  
    print(link.attrs['src'])  
    #保存链接并命名，time.time()返回当前时间戳防止命名冲突  
    request.urlretrieve(link.attrs['src'],{}{}.jpg)

