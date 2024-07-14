import plotly.graph_objects as go
import plotly.io as pio

# 设置Kaleido的MathJax为None
pio.kaleido.scope.mathjax = None

# 数据
x = ['Easy', 'Medium', 'Hard', 'Extra', 'All']
overlap = [91.1, 81.5, 76.0, 54.8, 78.6]
similarity = [92.3, 81.3, 75.9, 56.0, 79.0]
overlap_similarity = [90.7, 83.1, 80.6, 56.6, 80.3]

# 创建柱状图
trace1 = go.Bar(x=x, y=overlap, name='Syntactic matching',marker=dict(color='rgba(50, 171, 96, 0.6)'))
trace2 = go.Bar(x=x, y=similarity, name='Semantic matching',marker=dict(color='rgba(255, 127, 14, 0.6)'))
trace3 = go.Bar(x=x, y=overlap_similarity, name='Mix-of-matching',marker=dict(color='rgba(148, 103, 189, 0.6)'))

data = [trace1, trace2, trace3]

# 设置布局
layout = go.Layout(
    barmode='group',
    xaxis=dict(title='Difficulty Level', linecolor='black', linewidth=1, mirror='allticks'),
    yaxis=dict(title='Execution Accuracy (%)', range=[45, 100], linecolor='black', linewidth=1, mirror='allticks'),
    legend=dict(x=0.97, y=0.97, xanchor='right', yanchor='top', bgcolor='rgba(255, 255, 255, 0.8)'),
    font=dict(
        family='"Open Sans", verdana, arial, sans-serif',
        size=12,
        color='#333'
    ),  # 使用Arial字体
    paper_bgcolor='rgba(255, 255, 255, 0.5)',  # 设置半透明的背景颜色
    plot_bgcolor='rgba(255, 255, 255, 1)',  # 设置不透明的图形背景颜色
    margin=dict(r=100, t=100)  # 在右侧和顶部添加边框
)

# 创建图形
fig = go.Figure(data=data, layout=layout)

# 显示图形
fig.write_image('select_ablation.pdf')