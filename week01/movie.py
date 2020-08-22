# 使用requests获取豆瓣电影前10信息(名称、类型、上映时间)
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
url = 'https://movie.douban.com/top250'
header = {'user-agent':user_agent}
response = requests.get(url,headers=header)

# 通过status_code 查看是否成功
# print(response.status_code)
# print(response.text)
response.encoding = 'utf-8'
bs_info = bs(response.text,'html.parser')

movie_list = []
movie=[]
for tags in bs_info.find_all('div',attrs={'class':'info'},limit=10):
    #获取电影名称
    atag = tags.find_all('span',attrs={'class':'title'})
    if len(atag) > 1:
        # print('电影名称：',atag[0].text,atag[1].text)
        movie_name = atag[0].text+atag[1].text
    else:
        # print('电影名称：',atag[0].text)
        movie_name = atag[0].text

    atag1=tags.find_all('p',{'class':''})[0].text.split('...')[1].split('/')
    # print('电影类型：',atag1[2].strip())
    # print('上映时间：',atag1[0].strip(),'\n')
    movie_type = atag1[2].strip()
    movie_time = atag1[0].strip()
    
    movie =[movie_name,movie_type,movie_time]
    movie_list.append(movie)

#print(movie_name)
#print(movie_type)
#print(movie_time)

# 写入.csv文件
movies = pd.DataFrame(data = movie_list)
movies.to_csv('movies.csv',encoding='utf_8_sig',index=False,header=False)

print('success')


