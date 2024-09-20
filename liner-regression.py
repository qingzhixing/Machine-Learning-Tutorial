import matplotlib.pyplot as plt
import numpy as np

# 生成一次函数
k : float = 1.5
b : float = 2.0
# 数据浮动
noise : float = 2.0

# 生成数据
x = np.random.uniform(low=-10, high=10, size=100)
y = k * x + b + np.random.normal(scale=noise, size=100)

# 画图
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()

# TODO:计算线性回归参数