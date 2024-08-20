import numpy as np
import matplotlib.pyplot as plt

# 生成 x 值的范围
x = np.linspace(0, 1, 100) # 在 0 到 1 范围内生成 100 个点

# 计算对应的 y 值
m1 = 2
y1 = (1 + 1 / (m1 * x)) * np.exp(m1 * x)

m2 = 3
y2 = (1 + 1 / (m2 * x)) * np.exp(m2 * x)

# 添加两条新的曲线
m3 = 4
y3 = (1 + 1 / (m3 * x)) * np.exp(m3 * x)

# m4 = 5
# y4 = (1 + 1 / (m4 * x)) * np.exp(m4 * x)

# 绘制曲线
plt.plot(x, y1, label='m=2')
plt.plot(x, y2, label='m=3')
plt.plot(x, y3, label='m=4')  # 添加 m=4 的曲线
# plt.plot(x, y4, label='m=5')  # 添加 m=5 的曲线
plt.grid(axis='y')
# 添加标题和坐标轴标签
# plt.title(r'$\lambda$ rate delay')
plt.xlabel(r'$\lambda$')
plt.ylabel('delay')

# 添加图例
plt.legend()

plt.savefig('figFile1/lamdaRate2.png', dpi=300)

# 显示图形
plt.show()
