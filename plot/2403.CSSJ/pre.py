import matplotlib.pyplot as plt
import pandas as pd
from plottable import Table, ColumnDefinition
from plottable.plots import bar, progress_donut
from matplotlib.colors import LinearSegmentedColormap

# 设置字体为微软雅黑，防止绘制表格时由于存在中文而报错
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'

df = pd.read_excel('2022和2023年杭州市人口主要数据公报.xlsx')

# 由于原始数据“城镇化率（%）”和“常住人口（万人）”列名重复，所以pandas在读取数据后自动将第二个重名列的名称后面加了“.1”的后缀。
df['城镇化率（%）'] = df['城镇化率（%）'] / 100  #将百分数转换为小数，方便后续绘图
df['城镇化率（%）.1'] = df['城镇化率（%）.1'] / 100
df['人口增长率'] = (df['常住人口（万人）.1'] - df['常住人口（万人）']) / df['常住人口（万人）'] #计算人口增长率

print(df)

# 创造一个颜色映射带
cmap = LinearSegmentedColormap.from_list(
    name="bugw", colors=["#ffffff", "#f2fbd2", "#c9ecb4", "#93d3ab", "#35b0ab"], N=256
)

# 设置绘图背景的长宽
fig, ax = plt.subplots(figsize=(9, 12))

# 绘制表格
tab = Table(df,ax=ax,
            odd_row_color='#a5d8ff',  #设置奇偶列的表格背景颜色
            even_row_color='white',
            footer_divider=True,  #显示表格尾端边界线
            textprops={'ha': 'center'}, # 设置表格中文字居中对齐
            column_definitions=[
                # 设置“index”列，将其名称设为空，宽度改为0，文本居右对齐，颜色设置为白色从而将其隐藏
                ColumnDefinition(name='index',
                                 title="",
                                 width=0,
                                 textprops={"ha": "right",'color':'w'}),

                ColumnDefinition(name='地区',
                                 textprops={"ha": "center",
                                            'fontsize': 12}),

                # 设置“常住人口（万人）”列的组别为2022年，绘制表格会在表头显示分组信息，字体设置为加粗。
                ColumnDefinition(name='常住人口（万人）',
                                 group='2022年',
                                 textprops={'weight': 'bold'}),

                # 设置“城镇化率（%）”列的组别为2022年，修改列名为’城镇化率‘。
                ColumnDefinition(name='城镇化率（%）',
                                 title='城镇化率',
                                 group='2022年',
                                 plot_fn=progress_donut, # 将数据转换为圆环图形
                                 plot_kw={"is_pct": True,   # True代表数据为比率数，不需要再除以100
                                          "formatter": "{:.2f}", # 数据保留两位小数
                                          'radius': 0.48, # 圆环的显示半0径
                                          'textprops':{'fontsize':8}}), # 数据的文本显示大小

                ColumnDefinition(name='常住人口（万人）.1',
                                 title='常住人口（万人）',
                                 group='2023年', textprops={'weight': 'bold'}),


                ColumnDefinition(name='城镇化率（%）.1',
                                 title='城镇化率',
                                 group='2023年',
                                 plot_fn=bar,
                                 plot_kw={"cmap": cmap, # 给图形传入映射颜色带，从而根据数据大小，显示颜色的深浅。
                                          "plot_bg_bar": True,
                                          "annotate": True,
                                          "height": 0.8,
                                          "lw": 0.5,
                                          "formatter": "{:.1%}"}),

                ColumnDefinition(name='人口增长率',
                                 formatter="{:.1%}",
                                 textprops={'color': 'g', # 修改该列中文本颜色为绿色
                                            'weight': 'bold'})
            ]
            )

# 保存图片，裁掉其周围空白的区域。
plt.savefig('杭州市2022年和2023年人口主要数据公报.png', dpi=600, bbox_inches='tight')

plt.show()