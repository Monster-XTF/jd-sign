import os
import requests
import json
from datetime import datetime

# 获取环境变量中的 Cookie
jd_cookie = os.getenv('JD_COOKIE')
if not jd_cookie:
    print("未配置京东 Cookie！")
    exit(1)

# 请求头配置
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie': jd_cookie,
    'Referer': 'https://home.jd.com/'
}

def jd_sign():
    """京东首页签到"""
    try:
        url = 'https://api.m.jd.com/client.action?functionId=signBeanAct'
        params = {
            'functionId': 'signBeanAct',
            'body': '{"fp":"-1","shshshfp":"-1","shshshfpa":"-1","referUrl":"-1","userAgent":"-1","jda":"-1","rnVersion":"3.9"}',
            'appid': 'ld',
            'clientVersion': '10.0.4',
            'client': 'apple',
            'uuid': '123456789012345',
            'openudid': '123456789012345'
        }
        
        response = requests.get(url, headers=headers, params=params, timeout=10)
        result = response.json()
        
        if result.get('code') == 0:
            print(f"{datetime.now()} - 签到成功！{result.get('data', {}).get('signAwardMessage', '获得京豆')}")
        else:
            print(f"{datetime.now()} - 签到失败：{result.get('errMsg', '未知错误')}")
            
    except Exception as e:
        print(f"{datetime.now()} - 签到异常：{str(e)}")

def jd_daily_task():
    """执行其他每日任务（示例）"""
    try:
        # 这里可以添加其他任务的API调用
        print(f"{datetime.now()} - 执行每日任务...")
        # 示例：东东农场、萌宠、工厂等任务
    except Exception as e:
        print(f"{datetime.now()} - 每日任务异常：{str(e)}")

if __name__ == "__main__":
    print("开始执行京东签到任务...")
    jd_sign()
    jd_daily_task()
    print("京东签到任务执行完成！")
