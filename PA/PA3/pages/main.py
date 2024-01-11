import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
df = pd.read_excel('The data/video_list.xlsx')
df_ = pd.read_excel('The data/data3.xlsx')
# 根据点赞量排序数据框
df_sorted = df.sort_values(by='Create_time', ascending=False)
# 重置索引为整数
df_sorted.reset_index(drop=True, inplace=True)

# 添加新的整数索引列
df_sorted['index'] = range(1, len(df_sorted) + 1)
# 计算总获赞数
total_likes = df_sorted['Likes'].sum()
total_video_num = 425
st.write("视频列表：")
# 显示数据表
st.write(df_sorted)

st.write("评论：")
st.write(df_)