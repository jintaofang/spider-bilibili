from lxml import etree
import  requests
import time
import io
import sys
import jieba
import numpy as np
# from PIL import Iage
from wordcloud import WordCloud as wcm


headers={
		'Host': 'api.bilibili.com',
		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Cookie': 'finger=edc6ecda; LIVE_BUVID=AUTO1415378023816310; stardustvideo=1; CURRENT_FNVAL=8; buvid3=0D8F3D74-987D-442D-99CF-42BC9A967709149017infoc; rpdid=olwimklsiidoskmqwipww; fts=1537803390'

		}


	# 获取信息
def get_page(url,headers):
	try:
		# 延时操作，防止太快爬取
		time.sleep(0.5)
		response=requests.get(url,headers=headers)
	except Exception as e:
		print('获取xml内容失败,%s' % e)
		return False
	else:
		if response.status_code == 200:
			# 下载xml文件
			with open('bilibili.xml','wb') as f:
				f.write(response.content)
			return True
		else:
			return False

# 解析网页
def param_page(barrage_result):
	time.sleep(1)
	if  barrage_result:
		# 文件路径，html解析器
		html=etree.parse('bilibili.xml',etree.HTMLParser())
		# xpath解析，获取当前所有的d标签下的所有文本内容
		results=html.xpath('//d//text()')
		return results

def save_text(results):
	with open('data.txt','w',encoding='utf-8') as f:
		for line in results:
			f.write(line+'\n')
	print("存储成功")

# def text_save(filename, data):
# #filename为写入CSV文件的路径，data为要写入数据列表.
#     file = open(filename,'a')
#     for i in range(len(data)):
#     s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
#     s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
#     file.write(s)
#     file.close()
#     print("保存文件成功")

oid = 95688383
# path = 'C:\Users\75488\Downloads'
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
url='https://api.bilibili.com/x/v1/dm/list.so?oid='+str(oid)
barrage_result = get_page(url,headers)
results = param_page(barrage_result)
# for i in range(10):
# 	print(results[i])
save_text(results)
