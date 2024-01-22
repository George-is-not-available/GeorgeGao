import streamlit as st
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
df = pd.read_excel('The data/video_list.xlsx')
df_ = pd.read_excel('The data/data3.xlsx')

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 清理文本的函数（去除 '@' 提及和表情符号）
def clean_text(text):
    # 处理浮点数情况
    if isinstance(text, float):
        return str(text)

    # 去除 '@' 提及
    # text = re.sub(r'@\w+', '', text)
    # 去除表情符号
    emoji_pattern = re.compile("[w+]", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    return text


# 从本地 Excel 文件中的一列导入评论文本
comments_column_name = 'Text'  # 请替换为实际的评论列名

if comments_column_name in df_.columns:
    # 应用文本清理到评论列
    df_['clean_comments'] = df_[comments_column_name].apply(clean_text)

    # 使用正则表达式去除非中文字符
    df_['clean_comments'] = df_['clean_comments'].apply(lambda x: re.sub(r'[^\u4e00-\u9fa5]', '', x))

    # 检查是否有剩余的中文字符
    if not df_['clean_comments'].empty and any(df_['clean_comments']):
        # 生成并显示基于清理后评论的词云
        clean_comments_text = ' '.join(df_['clean_comments'].astype(str))

        # 导入自定义字体
        custom_font_path = 'C:\\Windows\\STZHONGS.TTF'  # 请替换为实际字体文件路径
        print("Custom Font Path:", custom_font_path)  # 添加调试输出

        # 创建图形
        plt.figure(figsize=(25, 15))

        # 生成并显示基于清理后评论的词云
        wordcloud = WordCloud(width=3760, height=2640, background_color='white', font_path=custom_font_path).generate(
            clean_comments_text)

        # 使用 streamlit 绘制词云图
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.write("词云：")
        st.pyplot(plt)
