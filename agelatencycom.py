# -*- coding = utf-8 -*-
# @Time : 2024/3/21 20:10
# @Author : Maxwell
# @File : agelatencycom.py
# @Software : PyCharm
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei', 'Times New Roman']  # 设置字体族，中文为SimSun，英文为Times New Roman
plt.rcParams['mathtext.fontset'] = 'stix'  # 设置数学公式字体为stix
def f(p):
    return 1 + 1/p + (p**2) / (1-p)

# 生成一组p值
p_values = np.linspace(0.15, 0.8, 100)


m1 = 2
y1 = (1 + 1 / (m1 * p_values)) * np.exp(m1 * p_values)

# 计算函数值
y_values_f = f(p_values)

plt.plot(p_values, y1, label='非信息年龄', linestyle='--')
plt.plot(p_values, y_values_f, label='信息年龄', linestyle='-')
plt.xlabel(r'$\rho$')
plt.ylabel('延时')

plt.legend()
plt.grid(True)
plt.savefig('figFile1/agelatency.png')
plt.show()