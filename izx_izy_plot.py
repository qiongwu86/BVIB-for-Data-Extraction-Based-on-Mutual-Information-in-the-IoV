# -*- coding = utf-8 -*-
# @Time : 2023/12/4 9:44
# @Author : Maxwell
# @File : izx_izy_plot.py
# @Software : PyCharm
# -*- coding = utf-8 -*-
# @Time : 2023/8/14 16:01
# @Author : Maxwell
# @File : figplot.py
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# 读取CSV文件
data = pd.read_csv('csv_file\paper_data_03.csv')

# 取出的数据
subset1 = data.iloc[:, [0,1]] #izx compare
subset2 = data.iloc[:, [2,3]] #izy compare

# 创建一个包含线形选项的列表
linestyles = [':', '-.']

# 绘制折线图，并设置不同的线形
for i in range(subset1.shape[1]):
    plt.plot(subset1.iloc[:, i], linestyle=linestyles[i])

# 添加横向网格线
plt.grid(axis='y')
plt.xlabel('epoch')
plt.ylim(0, 35) #izx
plt.ylabel(r'$I(Z,X)_{max}$')
plt.legend(subset1.columns, loc='upper right') #izx
plt.savefig('figFile1/izxwithlambda.pdf',dpi = 300)
plt.show()



for i in range(subset2.shape[1]):
    plt.plot(subset2.iloc[:, i], linestyle=linestyles[i])
plt.grid(axis='y')
plt.xlabel('epoch')
plt.ylim(2, 3.5) #izy
plt.ylabel(r'$I(Z,Y)_{min}$')
plt.legend(subset2.columns, loc='lower right') #izy
plt.savefig('figFile1/izywithlambda.pdf',dpi = 300)

# 显示图形
plt.show()
