import streamlit as st

# 设置页面背景图片和样式
st.markdown(
    """
    <style>
        body {
            background-image: url('Background/background.jpg');  
            background-size: cover;
            color: white; /* 设置文字颜色为白色 */
            padding: 20px; /* 设置页面边距 */
        }
        h1 {
            color: #FFD700; /* 设置标题颜色为金色 */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('脏小豆的个人视频\n（本站全部信息截止于2024/1/4/14:30:54）')
