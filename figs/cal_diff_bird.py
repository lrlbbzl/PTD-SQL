import plotly.graph_objects as go
import plotly.io as pio

# 设置Kaleido的MathJax为None
pio.kaleido.scope.mathjax = None

# 数据
din_1 = [47.01,32.62,27.12]
ptd_1 = [51.49,37.97,31.36]
din_2 = [46.60,33.42,29.66]
ptd_2 = [51.22,35.03,29.66]
din_3 = [56.93,41.44,36.44]
ptd_3 = [63.17,48.66,44.92]

data1 = [(ptd_1[i] - din_1[i]) * 100 / din_1[i] for i in range(3)]
data2 = [(ptd_2[i] - din_2[i]) * 100/ din_2[i] for i in range(3)]
data3 = [(ptd_3[i] - din_3[i]) * 100/ din_3[i] for i in range(3)]

print(data1)
print(data2)
print(data3)

# 四舍五入保留一位小数
data1 = [round(x, 1) for x in data1]
data2 = [round(x, 1) for x in data2]
data3 = [round(x, 1) for x in data3]

x_labels = ['Simple', 'Moderate', 'Challenging']

# 创建折线图
fig = go.Figure()

# 添加折线
fig.add_trace(go.Scatter(x=x_labels, y=data1, mode='lines+markers', name='Deepseek-coder-6.7b-instruct', line=dict(color='rgb(223,122,94)'), showlegend=True))
fig.add_trace(go.Scatter(x=x_labels, y=data2, mode='lines+markers', name='ChatGPT', line=dict(color='rgb(60,64,91)'), showlegend=True))
fig.add_trace(go.Scatter(x=x_labels, y=data3, mode='lines+markers', name='GPT-4', line=dict(color='rgb(130,178,154)'), showlegend=True))

# 设置横轴标签
fig.update_xaxes(title_text='Difficulty')

# 设置纵轴标签为"Gain (%)"
fig.update_yaxes(range=[-10, 40])

# 设置标题为空字符串，以关闭标题
fig.update_layout(title_text='')

# 设置图例位置
fig.update_layout(legend=dict(x=0, y=1, traceorder='normal', font=dict(family='sans-serif', size=18, color='black'), bgcolor='rgba(0,0,0,0)'))

# 着重显示三个曲线的最高点
fig.add_trace(go.Scatter(x=['Moderate'], y=[max(data1)], mode='markers', marker=dict(color='rgb(223,122,94)', size=10), showlegend=False))
fig.add_trace(go.Scatter(x=['Simple'], y=[max(data2)], mode='markers', marker=dict(color='rgb(60,64,91)', size=10), showlegend=False))
fig.add_trace(go.Scatter(x=['Challenging'], y=[max(data3)], mode='markers', marker=dict(color='rgb(130,178,154)', size=10), showlegend=False))

# 设置字体为Abadi
fig.update_layout(font=dict(family='Abadi', size=16))

# 调整y轴的图例离图形的距离
fig.update_layout(margin=dict(l=100, r=100, t=100, b=100))

# 调整y轴标签的位置，使其离y轴更近
fig.update_yaxes(tickvals=[-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40])

# 设置背景色为透明
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')

# 为图形画出上下左右四个黑色边框
fig.update_layout(
    shapes=[
        dict(type="rect", x0=-0.5, x1=2.5, y0=-10, y1=40, line=dict(color="black", width=2)),
        dict(type="rect", x0=-0.5, x1=2.5, y0=-10, y1=40, line=dict(color="black", width=2)),
        dict(type="rect", x0=-0.5, x1=2.5, y0=-10, y1=40, line=dict(color="black", width=2)),
        dict(type="rect", x0=-0.5, x1=2.5, y0=-10, y1=40, line=dict(color="black", width=2)),
    ]
)

# 添加虚线grid背景
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
fig.update_xaxes(title_text='Difficulty', range=[-0.5, 2.5])
# 添加实线y=0
fig.add_shape(type="line", x0=-0.5, x1=3.5, y0=0, y1=0, line=dict(color="rgba(0,0,0,0.1)", width=1))
# 保存图形为PDF文件
fig.write_image('_bird_fig.pdf')
