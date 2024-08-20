import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw

# 定义函数
def lambert(x):
    x = np.where(x < 0, np.nan, x)  # 将小于0的值替换为nan
    y = x.copy()
    x = np.log(x)
    while True:
        z = np.log(y) + y
        tmp = z - x
        mask = np.abs(tmp) >= 0.00001
        y = np.where(tmp < 0, y * 1.02, y * 0.98)
        if not mask.any():
            break
    y = np.round(y, 4)
    return y

def f(p):
    return 1 + 1/p + (p**2) / (1-p)

def g(p):
    b = -p * lambertw(-p ** (-1) * np.exp(-1 / p))
    return 1/(2*p) + 1/(1-b)

# 生成一组p值
p_values = np.linspace(0.2, 0.8, 100)

# 计算函数值
y_values_f = f(p_values)
y_values_g = g(p_values)

# 绘制图像
plt.plot(p_values, y_values_f, label='M/M/1', linestyle='-')
plt.plot(p_values, y_values_g, label='D/M/1', linestyle='--')
plt.xlabel(r'$\rho$')
plt.ylabel(r'$\Delta$')

plt.legend()
plt.grid(True)
plt.savefig('figFile1/rho.png')
plt.show()

