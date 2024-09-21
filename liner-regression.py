import matplotlib.pyplot as plt
import numpy as np

# 生成一次函数
k: float = 1.5
b: float = 2.0
# 数据浮动
noise: float = 2.0

# 生成数据
x = np.random.uniform(low=-10, high=10, size=100)
y = k * x + b + np.random.normal(scale=noise, size=100)

# 画图
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")

# 画原函数
plt.plot(x, k * x + b, color="blue")

# 回归
theta = np.zeros(2)
alpha: float = 0.01
iterations: int = 10


def hypothesis(x: np.ndarray, theta: np.ndarray) -> np.ndarray:
    return x * theta[0] + theta[1]


def cost(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> float:
    diff = hypothesis(x, theta) - y
    return np.sum(diff**2) / (2 * len(x))


for i in range(iterations):
    hypothesis_value = hypothesis(x, theta)
    theta[0] -= alpha * np.sum((hypothesis_value - y) * x) / len(x)  # TODO: WHY?
    theta[1] -= alpha * np.sum((hypothesis_value - y)) / len(x)

print("theta:", theta)

# 画回归线
plt.plot(x, hypothesis(x, theta), color="green")

plt.show()
