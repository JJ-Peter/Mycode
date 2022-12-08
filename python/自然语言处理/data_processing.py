import json
import re
#3、36修改
filename='E:\code\python\自然语言处理\data.json'#json文件的目录
url=[]
title=[]
text=[]

def remove_punctuation(line, strip_all=True):
    if strip_all:
        rule =re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
        line =rule.sub(' ',line)
    else:
        punctuation ="""！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""
        re_punctuation ="[{}]+".format(punctuation)
        line =re.sub(re_punctuation, ' ', line)
    return line.strip()

#打开json文件，并分离url、title、text
with open(filename,'r',encoding='UTF-8') as f:
    data=json.load(f)
    for news in data:
        url.append(news['url'])
        title.append(news['title'])
        text.append(news['text'])

#将标点符号替换成空格，同时去掉多余的空格
for i in range(len(url)):
    title[i]=remove_punctuation(title[i])
    text[i]=remove_punctuation(text[i])
    title[i]= ' '.join(title[i].split())
    text[i] = ' '.join(text[i].split())

#输出文件txt
for i in range(len(url)):
    f=open(r'E:\study\自然语言处理\news_'+str(i) +'.txt','w')#文件的保存地址
    f.write(url[i]+'\n')
    for j in range(10):
        f.write(title[i]+' ')
    f.write(text[i])
    f.close()