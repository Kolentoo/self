
from urllib import request
from bs4 import BeautifulSoup


# 目标地址
url = "https://bangumi.bilibili.com/22/?spm_id_from=333.334.primary_menu.7"
# 头文件反爬虫
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mob'}
# 模拟浏览器打开页面
page_info = request.urlopen(url).read()
page_info = page_info.decode('utf-8')

# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser') 
# print(soup.prettify())
titles = soup.find_all('div','more-link')

for title in titles: 
    print(title.string) 
# with open(r'F:\python\data.txt', 'w') as file:
#     for title in titles:
#         file.write(title.string + '\n')

#open()是读写文件的函数,with语句会自动close()已打开文件  
with open(r"F:\python\data.txt","w") as file:       #在磁盘以只写的方式打开/创建一个名为 articles 的txt文件  
    for title in titles:  
        file.write(title.string+'\n')  
