import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

# 定义函数
def calculate_y(x, m, n, t_ec):
    return ((t_ec + 1 / (m * x)) * np.exp(m * x)) + (150 / 10) * np.log2(n)

# 定义变量范围
x_values = [0.2, 0.3]
m_values = np.linspace(1, 10, 100)
n_values = np.linspace(1, 10, 100)

# 创建网格数据
M, N = np.meshgrid(m_values, n_values)
t_ec = 10

# 计算Z轴的值
Z1 = calculate_y(x_values[0], M, N, t_ec)
Z2 = calculate_y(x_values[1], M, N, t_ec)

# 绘制曲面图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制第一个曲面
surf1 = ax.plot_surface(M, N, Z1, cmap='viridis')

# 绘制第二个曲面
surf2 = ax.plot_surface(M, N, Z2, cmap='plasma')

# 手动创建图例
legend_elements = [
    Patch(facecolor=surf1.get_facecolor()[0], label=fr'$\lambda$={x_values[0]}'),
    Patch(facecolor=surf2.get_facecolor()[0], label=fr'$\lambda$={x_values[1]}')
]
ax.legend(handles=legend_elements)

# 计算并绘制第三个曲面
x_values.append(0.4)
Z3 = calculate_y(x_values[2], M, N, t_ec)
surf3 = ax.plot_surface(M, N, Z3, cmap='magma')

# 更新图例
# legend_elements.append(Patch(facecolor=surf3.get_facecolor()[0], label=fr'$\lambda$={x_values[2]}'))

legend_elements.append(Patch(facecolor=surf3.get_facecolor()[0], label=fr'$\rho$={x_values[2]}'))

ax.legend(handles=legend_elements)

# 设置坐标轴标签和标题
ax.set_xlabel('m')
ax.set_ylabel('n')
# ax.set_zlabel('E[T]')

ax.set_zlabel('AoI')

plt.savefig('figFile1/delayWithMN2.png',dpi = 300)
# 显示图形
plt.show()
