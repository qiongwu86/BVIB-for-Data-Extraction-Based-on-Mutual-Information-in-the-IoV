import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义方程
def func(m, tec):
    return (-2*m+np.sqrt(m**2+4*m**2*tec))/(2*m**2*tec)

# 创建数据
m = tec = np.linspace(1, 10, 100)
M, Tec = np.meshgrid(m, tec)
Z1 = func(M, Tec) # 第一张曲面
Z2 = func(M, Tec) + 0.3 # 修改第二张曲面的函数值，使之与第一张曲面有明显差异

# 绘制图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(M, Tec, Z1, alpha=0.7, cmap='coolwarm') # 绘制第一张曲面
ax.plot_surface(M, Tec, Z2, alpha=0.7, cmap='viridis') # 绘制第二张曲面，修改了颜色映射以区分两者
ax.set_xlabel('m') # 设置X轴标签
ax.set_ylabel(r'$t_{ec}$') # 设置Y轴标签
ax.set_zlabel('λ') # 设置Z轴标签
# 添加曲面名称
ax.text(10, 0, np.max(Z1), "BVIB", color='red', fontsize=12)
ax.text(10, 0, np.max(Z2), "BFL", color='blue', fontsize=12)

plt.savefig('figFile1/delayWithmtec.png',dpi = 300)

plt.show()
