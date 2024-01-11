import requests
from time import sleep
import json
import pandas as pd

file_location = 'The data/data2.xlsx'


def write_comments(file_location, final_data):
    df = pd.DataFrame(final_data)
    df.to_excel(file_location, index=False)


def fetch_comments(parameters, headers, file_location):
    url = 'https://www.douyin.com/aweme/v1/web/comment/list/?'

    video_id = []
    comment_id = []
    comment_text = []
    comment_likes = []
    comment_sender_id = []
    comment_sender_name = []
    comment_sender_region = []
    comment_like_author = []

    has_more = True

    while has_more:
        try:
            response = requests.get(url, headers=headers, params=parameters)
            data = response.json()
        except requests.exceptions.JSONDecodeError as e:
            sleep(15)
            continue

        with open(file_location, 'a', encoding='utf-8') as f:
            json.dump(data, f)

        for info in data.get('comments', []):
            video_id.append(info.get('aweme_id', ''))
            comment_id.append(info.get('cid', ''))
            comment_text.append(info.get('text', '').encode().decode('utf-8'))
            comment_likes.append(info.get('digg_count', 0))
            comment_sender_id.append(info.get('user', {}).get('uid', ''))
            comment_sender_name.append(info.get('user', {}).get('nickname', ''))
            comment_sender_region.append(info.get('ip_label', '').encode().decode('utf-8'))
            comment_like_author.append(info.get('is_author_digged', False))
            print(comment_text[-1])

        parameters['cursor'] = data.get('cursor', 0)
        has_more = data.get('has_more', False)

        sleep(10)

    final_data = {
        'video ID': video_id,
        'comment ID': comment_id,
        'Text': comment_text,
        'likes': comment_likes,
        'sender ID': comment_sender_id,
        'sender': comment_sender_name,
        'sender region': comment_sender_region,
        'comment liked by author?': comment_like_author
    }

    write_comments(file_location, final_data)


# 设置请求参数和头部信息
params = {
    'aid': '6383',
    'aweme_id': 7045446211884649765,
    'cursor': 0,
    'count': 20
}
headers = {
    'cookie': '_waftokenid=eyJ2Ijp7ImEiOiIrcWNqVHBCOWd5ejl5M2YyM1BVV29NVlM2WHZDTG5MMDJZZDZDRUtYQ1NJPSIsImIiOjE3MDQzNDQ2MjEsImMiOiJWWHFjc3VSdGJ5TTZSS2kxcHpKT1NuRktGZ09WWUZIWUQzWkhvamtlVXA4PSJ9LCJzIjoiK1VxaVVVOTdCMzU5TGhrNVM2WFRzL01mTjIrazQ0M1hmdkE2c21iR0ZDUT0ifQ; douyin.com; ttwid=1%7CWrIXV0WAMD6CESqs5vR9j1q-ii8ZkdjH3R0kjfjwe1U%7C1703228680%7C5ece741f46129a2c471031ba6a12c4426de37c8e78198a9971fc11d3a92131e4; dy_swidth=1862; dy_sheight=1048; s_v_web_id=verify_lqgadpxo_ns6Cd8WC_MOho_4WSz_ApKA_l3fmQF23JKWG; passport_csrf_token=d1a935e5d7b856c481b0600cb026a4f9; passport_csrf_token_default=d1a935e5d7b856c481b0600cb026a4f9; bd_ticket_guard_client_web_domain=2; n_mh=q0Kq98z6Kg7MjAbFoEEKlPfXnGVYeI_ZNqF6tQu0wGI; sso_uid_tt=2a5853123b7fdd201028141d1e5ab434; sso_uid_tt_ss=2a5853123b7fdd201028141d1e5ab434; toutiao_sso_user=397246632dcfca334116dc934ac481fe; toutiao_sso_user_ss=397246632dcfca334116dc934ac481fe; passport_assist_user=CjvcffXvlggOKlLC1FKYwwnI1XyaIoq8W-Z_cBKVwoNX8LSO_Vge3A8tTd-AQcL7TQ6QaESpCv38HUdG4hpKCjw-_C1dIGKFVP6X3dUerePTTg5nnTu43FNaWTjv5nyMqnkq78L4qXEOfInkTHRSoDAINCgM6Lfqidvj08cQyczEDRiJr9ZUIAEiAQMqOTmK; sid_ucp_sso_v1=1.0.0-KGI3NTUwYzQwYjk0MWQ5ODM2NzhmZmE2MmE1MGE5M2RmY2QyMjUyYTgKHAiv-ve2EBCvhZWsBhjvMSAOMPS7pKwFOAZA9AcaAmhsIiAzOTcyNDY2MzJkY2ZjYTMzNDExNmRjOTM0YWM0ODFmZQ; ssid_ucp_sso_v1=1.0.0-KGI3NTUwYzQwYjk0MWQ5ODM2NzhmZmE2MmE1MGE5M2RmY2QyMjUyYTgKHAiv-ve2EBCvhZWsBhjvMSAOMPS7pKwFOAZA9AcaAmhsIiAzOTcyNDY2MzJkY2ZjYTMzNDExNmRjOTM0YWM0ODFmZQ; passport_auth_status=59bee56589fd99ece9dd34383d843515%2C; passport_auth_status_ss=59bee56589fd99ece9dd34383d843515%2C; uid_tt=3d2709d8a0f6684bf7fdf066dfee3821; uid_tt_ss=3d2709d8a0f6684bf7fdf066dfee3821; sid_tt=7a87a7e91c8e3de2e28d827ffbf0842b; sessionid=7a87a7e91c8e3de2e28d827ffbf0842b; sessionid_ss=7a87a7e91c8e3de2e28d827ffbf0842b; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=15667a89c5b492d416d7eefb93fa1f3d; __security_server_data_status=1; sid_guard=7a87a7e91c8e3de2e28d827ffbf0842b%7C1703232179%7C5183998%7CTue%2C+20-Feb-2024+08%3A02%3A57+GMT; sid_ucp_v1=1.0.0-KDM4ODc2YTNlZjNiMjVlNjc2YzIwY2Q1ZDYwNWNjNWQ2MzUyNWJlNmUKGAiv-ve2EBCzhZWsBhjvMSAOOAZA9AdIBBoCaGwiIDdhODdhN2U5MWM4ZTNkZTJlMjhkODI3ZmZiZjA4NDJi; ssid_ucp_v1=1.0.0-KDM4ODc2YTNlZjNiMjVlNjc2YzIwY2Q1ZDYwNWNjNWQ2MzUyNWJlNmUKGAiv-ve2EBCzhZWsBhjvMSAOOAZA9AdIBBoCaGwiIDdhODdhN2U5MWM4ZTNkZTJlMjhkODI3ZmZiZjA4NDJi; LOGIN_STATUS=1; store-region=cn-bj; store-region-src=uid; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; publish_badge_show_info=%221%2C0%2C0%2C1704003947636%22; download_guide=%223%2F20231231%2F1%22; SEARCH_RESULT_LIST_TYPE=%22single%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAMhY_KGOfzEO6H0RWAzx6NT_rohz-VFsXDToLCZNSp74%2F1704211200000%2F0%2F0%2F1704168696880%22; __ac_nonce=065963c06007e1c0f3a45; __ac_signature=_02B4Z6wo00f01j04AgwAAIDDNx7ZpLkXP6Y9GE6AAOrmcfmwVrg7mWjMg9sMbhdnJBja0v5hTR6BfN033MtSqmO.xIvjKxSPGHgKL4Rsj5hN9qULJafjAfEVgJWU1oSNNe5W1oMSxQSjrpjxe8; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; csrf_session_id=d0fc63af2e58d83bf06e8c8e864f6623; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAMhY_KGOfzEO6H0RWAzx6NT_rohz-VFsXDToLCZNSp74%2F1704384000000%2F0%2F1704344583222%2F0%22; passport_fe_beating_status=true; strategyABtestKey=%221704344596.081%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; xg_device_score=7.524182179909139; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1862%2C%5C%22screen_height%5C%22%3A1048%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUEgrSFoyS3lKS043b1JFYThBc2Fyemdqa1RoZkwzcWkxMWIwbnhzR3hrR2NBMlQraWRmQVcvSktYNVdsNWxXQXRxQmRSaWtYVjR1K3NzUDNSN3BPRUU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=eb0H8VhuByy_CuyIHg6WI7dKgnddN46XYkxOgEzrS0QQj3FOQnh-MzXfuN9zLJmF-I2xAz69AF-XT19KKyveca2BtJtfTCJ1vZp4FZPWBHoYiiv0QDxxf2HbHyA=; odin_tt=cc63af7c3acd10cd0bd0f59499f2b548d6b4eb6802eea93b3f520c80ab2b865437bfdd78aa64dc5dda4877834e03320580a28ee22635e20c913c21470b46c358; tt_scid=utNxcSZdeqGRB9TcgMQVSVJnhAwDProJdcnV3eRAaX4NPa7wL3NaZl.V85foG4Stb2f4; msToken=7STI3uErNa--QJVHVhp51GWRHDMxn0tZPgA8baGgvKUa7z89rY9CiPauLteDp279RursTpOCheTg5v-fKr_LEFdOe2Dtx22HSRq7Sl112GCLW2zIe2ZufQdWIWg=; IsDouyinActive=false',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.3   6'
}

# 请将'your_file_location_here'替换为实际的文件路径
file_location = 'The data/data2.json'

# 运行脚本
fetch_comments(params, headers, file_location)
