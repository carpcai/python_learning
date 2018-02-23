#coding:utf-8
import jieba
import jieba.analyse

str = "他当时只有3岁的儿子被诊断出患了白血病，就在一家人为儿子担心的时候，他的妻子又因为心脏问题突然离世。"

jieba.analyse.set_stop_words("./stopwords.txt")
sec_list =jieba.cut(str, HMM=False, cut_all=False)

tags = jieba.analyse.extract_tags(str);

result = [item for item in sec_list if item in tags]



# words =jieba.cut("他当时只有3岁的儿子被诊断出患了白血病，就在一家人为儿子担心的时候，他的妻子又因为心脏问题突然离世。", HMM=False)
# jieba.suggest_freq(('中','出'),True)
print('/'.join(sec_list))
print("\n")
print('/'.join(tags))