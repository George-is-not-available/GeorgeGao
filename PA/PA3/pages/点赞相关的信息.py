import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
df = pd.read_excel('The data/video_list.xlsx')
df_ = pd.read_excel('The data/data3.xlsx')
df_sorted = df.sort_values(by='Create_time', ascending=False)

# 重置索引为整数
df_sorted.reset_index(drop=True, inplace=True)
# 添加新的整数索引列
df_sorted['index'] = range(1, len(df_sorted) + 1)
# 计算总获赞数
total_likes = df_sorted['Likes'].sum()
total_video_num = 425

# 显示总获赞数
st.write(f"总获赞数: {total_likes}")
# 绘制折线统计图
st.line_chart(df_sorted.set_index('index')[['Likes']])
# 平均每个视频的点赞数
df_num = total_likes / total_video_num
st.write("平均视频点赞数：")
st.write(df_num)
