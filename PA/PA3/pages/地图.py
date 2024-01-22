
import streamlit as st
import pandas as pd
import json

data = '''
{
  "河北": {
    "latitude": 38.568954,
    "longitude": 115.43978
  },
  "黑龙江": {
    "latitude": 47.108518,
    "longitude": 126.762714
  },
  "湖北": {
    "latitude": 30.932695,
    "longitude": 112.327646
  },
  "陕西": {
    "latitude": 33.404791,
    "longitude": 107.930091
  },
  "安徽": {
    "latitude": 32.448449,
    "longitude": 117.275731
  },
  "山东": {
    "latitude": 35.947973,
    "longitude": 118.09366
  },
  "上海": {
    "latitude": 31.273094,
    "longitude": 121.373237
  },
  "吉林": {
    "latitude": 43.835562,
    "longitude": 126.543727
  },
  "重庆": {
    "latitude": 29.540849,
    "longitude": 106.632809
  },
  "天津": {
    "latitude": 38.951618,
    "longitude": 117.236835
  },
  "四川": {
    "latitude": 31.166664,
    "longitude": 102.540196
  },
  "云南": {
    "latitude": 25.06511,
    "longitude": 100.568742
  },
  "内蒙古": {
    "latitude": 42.013154,
    "longitude": 111.230208
  },
  "山西": {
    "latitude": 37.399174,
    "longitude": 112.142715
  },
  "阿联酋": {
    "latitude": 23.43307661,
    "longitude": 53.9791945
  },
  "广东": {
    "latitude": 24.104169,
    "longitude": 113.487842
  },
  "辽宁": {
    "latitude": 41.222247,
    "longitude": 123.390106
  },
  "马来西亚": {
    "latitude": 5.452424408,
    "longitude": 116.834633
  },
  "福建": {
    "latitude": 25.803743,
    "longitude": 117.546963
  },
  "IP未知": {
    "latitude": null,
    "longitude": null
  },
  "湖南": {
    "latitude": 27.560188,
    "longitude": 111.709149
  },
  "河南": {
    "latitude": 33.764935,
    "longitude": 113.302086
  },
  "甘肃": {
    "latitude": 35.161803,
    "longitude": 103.771112
  },
  "广西": {
    "latitude": 23.929809,
    "longitude": 108.587878
  },
  "宁夏": {
    "latitude": 37.401799,
    "longitude": 106.042662
  },
  "中国香港": {
    "latitude": 22.27248321,
    "longitude": 114.1666082
  },
  "浙江": {
    "latitude": 29.284433,
    "longitude": 119.620259
  },
  "江苏": {
    "latitude": 33.60216,
    "longitude": 118.968969
  },
  "新疆": {
    "latitude": 40.84152,
    "longitude": 85.510272
  },
  "贵州": {
    "latitude": 26.134304,
    "longitude": 106.147532
  },
  "江西": {
    "latitude": 27.865172,
    "longitude": 115.587226
  },
  "北京": {
    "latitude": 39.903883,
    "longitude": 116.71847
  },
  "NaN": {
    "latitude": 18.85289827,
    "longitude": 100.8381905
  }
}
'''


# 加载JSON数据
json_data = json.loads(data)

# 从JSON数据创建DataFrame
df = pd.DataFrame.from_dict(json_data, orient='index').reset_index()
df.columns = ['location', 'latitude', 'longitude']

# 删除具有空值的行
df = df.dropna(subset=['latitude', 'longitude'])

# 显示地图
st.map(data=df)