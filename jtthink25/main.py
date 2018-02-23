# 用户口味计算、修正的余弦相似性、利用sklearn实现相关功能
from sklearn.metrics.pairwise import cosine_similarity

users = np.array([3, 2, 1, 2, 3], [6, 4, 3, 5, 6], [2,3,4,5,6])

print(cosine_similarity(users));