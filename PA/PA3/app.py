import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置页面背景图片
st.markdown(
    """
    <style>
        body {
            background-image: url('https://raw.githubusercontent.com/CoopEdu2023-Python/George/Master/PA/PA3/Background/background.jpg?token=GHSAT0AAAAAACMHZK4L6JRZQRDC4USGJ2Y6ZM7H5FA');  
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('脏小豆的个人视频\n（本站全部信息截止于2024/1/4/14:30:54）')


