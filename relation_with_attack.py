# -*- coding = utf-8 -*-
# @Time : 2023/12/4 16:37
# @Author : Maxwell
# @File : relation_with_attack.py
# @Software : PyCharm


import numpy as np
import matplotlib.pyplot as plt



# 定义方程
def func(a, t_ec, m, x, t_ele, T_term, n):
    return ((t_ec + 1/(m*x))*np.exp(m*x))/(1-t_ele/(T_term*(n-a)/n))

# 创建数据
a = np.linspace(0, 8, 9) # a的取值范围
t_ec = 10
m = 3
x1 = 0.2
x2 = 0.3
x3 = 0.4
t_ele = 150
T_term = 2000
n = 10
Y1 = func(a, t_ec, m, x1, t_ele, T_term, n) # 计算x为0.2时的Y轴的值
Y2 = func(a, t_ec, m, x2, t_ele, T_term, n) # 计算x为0.3时的Y轴的值
Y3 = func(a, t_ec, m, x3, t_ele, T_term, n) # 计算x为0.4时的Y轴的值

# 绘制图形
plt.plot(a, Y1, label=r'$\lambda$=0.2') # 绘制x为0.2的曲线
plt.plot(a, Y2, label=r'$\lambda$=0.3') # 绘制x为0.3的曲线
plt.plot(a, Y3, label=r'$\lambda$=0.4') # 绘制x为0.4的曲线
plt.xlabel('a') # 设置X轴标签
plt.ylabel('E[T]') # 设置Y轴标签
# plt.title('Comparison of the function for different x') # 设置标题
plt.legend() # 显示图例
plt.grid(True) # 显示网格
plt.savefig('figFile1/attack2.svg',dpi = 300)
plt.show()
