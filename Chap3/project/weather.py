# coding:utf-8

import requests

def fetchWeather(location):
    result= requests.get('https://api.seniverse.com/v3/weather/now.json', params = {
    'key': 'sl28on5pq79bxilu',
    'location': location,
    'language': 'zh-Hans',
    'unite': 'c'
    }, timeout=60)
    return result.json()

def weatherPresent(target):
    city = target['results'][0]['location']['name']
    weather = target['results'][0]['now']['text']
    temp = target['results'][0]['now']['temperature']
    time = target['results'][0]['last_update'][:-6].replace('T', ' ')
    weather_str = "%s 的天气为 %s, 温度为 %s 摄氏度.\n更新时间: %s\n" % (city,weather,temp,time)
    return weather_str