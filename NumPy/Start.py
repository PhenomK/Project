from sklearn import datasets
import matplotlib.pyplot as plt
#加载数字数据集
digits = datasets.load_digits()
#展示第一个数字
plt.figure(5, figsize=(10, 10))
plt.imshow(digits.images[1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
