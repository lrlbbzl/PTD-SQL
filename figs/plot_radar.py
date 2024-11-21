import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

# 数据
methods = ['DIN-SQL', 'DAIL-SQL', 'PTD-SQL']
models = ['Deepseek-coder-6.7b-instruct', 'ChatGPT', 'GPT-4']
categories = ['Multi-set problems', 'Combination problems', 'Filtering problems', 'Other simple problems']

# 第一张图数据
model1_scores = [[49.5, 71.7, 75.6, 81.3], [54.4, 72.8, 76.1, 84.6], [62.4, 74.0, 76.1, 85.3]]

# 第二张图数据
model2_scores = [[63.4, 70.5, 79.8, 83.2], [67.3, 71.7, 79.3, 89.7], [73.3, 74.4, 79.8, 89.0]]

# 第三张图数据
model3_scores = [[71.3, 78.0, 82.0, 83.5], [71.3, 77.2, 84.2, 91.2], [77.2, 80.7, 87.2, 91.2]]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 更改为更协调的颜色

# 绘制雷达图的函数
def plot_radar_chart(ax, model_scores, model_name, ylim):
    N = len(categories)
    x_as = [n / float(N) * 2 * np.pi for n in range(N)]
    x_as += x_as[:1]

    for i, method in enumerate(methods):
        values = model_scores[i]
        values += values[:1]
        ax.plot(x_as, values, color=colors[i], linewidth=2, linestyle='solid', label=method)
        ax.fill(x_as, values, color=colors[i], alpha=0.2)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(0)
    ax.set_yticklabels([])
    ax.set_xticks(x_as[:-1])
    ax.set_xticklabels([])  # 移除默认的xticklabels
    ax.set_title(model_name, size=20, color=colors[i], y=1.1)
    ax.set_ylim(ylim)

    for i, (angle, label) in enumerate(zip(x_as[:-1], categories)):
        if angle < np.pi:
            ha, distance = "left", 1.05
        else:
            ha, distance = "right", 1.1
        ax.text(angle, ylim[1] * distance, label, size=10, horizontalalignment=ha, rotation=angle * 180 / np.pi)

# 创建一个1x3的子图
fig, axs = plt.subplots(1, 3, figsize=(18, 6), subplot_kw=dict(polar=True))

# 将三个雷达图添加到子图中
plot_radar_chart(axs[0], model1_scores, models[0], [45, 90])
plot_radar_chart(axs[1], model2_scores, models[1], [60, 95])
plot_radar_chart(axs[2], model3_scores, models[2], [70, 95])

# 添加图例
fig.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# 显示图像
plt.savefig('radar.pdf')