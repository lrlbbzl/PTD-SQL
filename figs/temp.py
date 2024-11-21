import matplotlib.pyplot as plt
import numpy as np

# 设置步长
steps = np.linspace(0, 20, 100)

# 理想效率
ideal_efficiency = np.ones_like(steps)
ideal_efficiency[steps > 8] = 1
ideal_efficiency[steps <= 8] = steps[steps <= 8] / 8

# 实际效率
actual_efficiency = 1 - np.exp(-steps / 10)

# 绘制理想效率
plt.plot(steps, ideal_efficiency, label='Ideal Curve', color=(223/255, 122/255, 94/255))

# 绘制实际效率
plt.plot(steps, actual_efficiency, label='Actual Curve', color=(130/255, 178/255, 154/255))

# 设置横轴和纵轴标签
plt.xlabel('Steps')
plt.ylabel('Completion Rate')

# 添加图例
plt.legend()

# 设置横纵轴范围从0开始
plt.xlim(0, 20)
plt.ylim(0, 1)

# 在两个曲线下方分别绘制有颜色的区域
plt.fill_between(steps, ideal_efficiency, color=(223/255, 122/255, 94/255), label='S1')
plt.fill_between(steps, actual_efficiency, color=(130/255, 178/255, 154/255), label='S2')

# 隐藏横轴上的ticks
plt.xticks([])

# 修改区域标签颜色为黑色
plt.text(12, 0.4, 'S1', fontsize=12, color='black')
plt.text(8, 0.75, 'S2', fontsize=12, color='black')

# 设置图片尺寸
plt.gcf().set_size_inches(6, 4)

# 显示图形
plt.savefig('temp.pdf')