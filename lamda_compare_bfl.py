# -*- coding = utf-8 -*-
# @Time : 2024/1/2 9:37
# @Author : Maxwell
# @File : lamda_compare_bfl.py
# @Software : PyCharm
# -*- coding = utf-8 -*-
# @Time : 2023/12/4 9:42
# @Author : Maxwell
# @File : lambda_with_m.py
# @Software : PyCharm

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# # 生成 x 值的范围
# x = np.linspace(0, 3, 100) # 在 -10 到 10 范围内生成 100 个点
#
# # 计算对应的 y 值
# m = 1
# y = (1+1/(m*x))*np.exp(m*x)
#
# # 绘制曲线
# plt.plot(x, y)
#
# # 添加标题和坐标轴标签
# plt.title('lamda rate delay')
# plt.xlabel('lamda')
# plt.ylabel('delay')
#
# # 显示图形
# plt.show()

# 生成 x 值的范围
x = np.linspace(0, 0.5, 100) # 在 0 到 3 范围内生成 100 个点


t_p = 0.5
# 计算对应的 y 值
m1 = 2
y1 = (30+1/(m1*x))*np.exp(m1*x*t_p)

m2 = 2
y2 = (10+1/(m2*x))*np.exp(m2*x*t_p)

# 绘制曲线
plt.plot(x, y1, label='BFL')
plt.plot(x, y2, label='BVIB')

# 添加标题和坐标轴标签
# plt.title(r'$\lambda$ rate delay')
plt.xlabel(r'$\lambda$')
plt.ylabel('E[T]')

# 添加图例
plt.legend()
plt.grid(True)
plt.savefig('figFile1/ComBfl.svg',dpi = 300)

# 显示图形
plt.show()




