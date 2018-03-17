import jieba
import jieba.analyse
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer,TfidfVectorizer
from sklearn.preprocessing import Normalizer
# 1、据说程序员是一个很有前途的工作，我要好好学习，将来做程序员。前两天我在网上买了一本开发方面的书，
# 卖家发的顺丰快递，快递小哥2天就给送到，这几天我正式开始写代码学习了。
# 2、现在我工作了十几年，每天过着同样的生活，送快递、收快递，太无聊了。
# 3、圣诞节要到了。不要工作了，大家嗨起来了。

# jieba.analyse.set_stop_words('./files/stopwords.txt')
#
# str="据说程序员是一个很有前途的工作，我要好好学习，将来做程序员。前两天我在网上买了一本开发方面的书，"\
#                      "卖家发的顺丰快递，快递小哥2天就给送到，这几天我正式开始写代码学习了"
# seg_list = jieba.cut(str,cut_all=False)
# tags=jieba.analyse.extract_tags(str)
# result=[item for item in seg_list if item  in tags ]
# print("/".join(result))

# words_list=['程序员 前途 程序员 快递 工作 快递','工作 快递 无聊 快递 ','圣诞节 工作']
# cv=CountVectorizer()
# cv_result=cv.fit_transform(words_list)
# # print(cv.get_feature_names())
# # print(cv_result.toarray())
# # print(Normalizer().fit_transform(cv_result.toarray()))
# # #手动方法
# # tfidf_trans=TfidfTransformer(norm=None).fit_transform(Normalizer().fit_transform(cv_result.toarray()))
# # print(Normalizer().fit_transform(tfidf_trans.toarray()))
#
# #直接方法
# tfidf_v=TfidfVectorizer()
# tfidf_result=tfidf_v.fit_transform(words_list)
# print(tfidf_result)
# print(tfidf_v.get_feature_names())
# print(tfidf_result.toarray())

import re
import os
from sklearn.naive_bayes import MultinomialNB
def getTestKeyWords(fileName): #测试文件的 关键词
    with open(doc_root+"/"+fileName,"rb") as f:
        content=f.read().decode("utf-8");
        f.close()
    return [getKeyWords(content)]
#
# jieba.analyse.set_stop_words('./files/stopwords.txt')
def getKeyWords(str):
    str=re.sub(r'[0-9]', '', str)
    seg_list = jieba.cut(str, cut_all=False)
    tags=jieba.analyse.extract_tags(str)
    result=[item for item in seg_list if item  in tags ]
    return " ".join(result)   #返回一个字符串用  空格 分割 ，方便 给 数组append

doc_root="docs"
words_list=[] #保存所有关键字列表
label_list=[] #保存分类

for label in os.listdir("docs"):
    labelpath=doc_root+"/"+label
    if not os.path.isdir(labelpath):
        continue
    files=os.listdir(labelpath) #获取文件夹  label就是分类名
    for file in files:
        with open(doc_root+'/'+label+"/"+file,'rb') as f:
            file_content=f.read().decode("utf-8")
            f.close()
        words_list.append(getKeyWords(file_content))
        label_list.append(label)
# print(words_list)
# print(label_list)

tfidf_v=TfidfVectorizer()
training_data=tfidf_v.fit_transform(words_list)

# print(training_data)

test_data=tfidf_v.transform(getTestKeyWords("test2.txt"))

print(test_data)


clf=MultinomialNB()
clf.fit(training_data,label_list)

print(clf.predict(test_data))

