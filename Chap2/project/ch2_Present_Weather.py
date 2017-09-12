# coding:utf-8
import requests

print (
"""
====我是您的贴心天气小助手====
程序持续更新中，欢迎关注
使用建议请发送至邮箱：sailinchengo@gmail.com
"""
)

# 获取实时天气
def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params = {
    'key': 'sl28on5pq79bxilu',
    'location': location,
    'language': 'zh-Hans',
    'unit': 'c'
    }, timeout= 60)
    return result.json()

#天气数据展示
def weatherPresent(target):
    city = target['results'][0]['location']['name']
    weather = target['results'][0]['now']['text']
    temp = target['results'][0]['now']['temperature']
    time = target['results'][0]['last_update'][:-6].replace('T', ' ')
    weather = "%s 的天气为 %s, 温度为 %s 摄氏度.\n更新时间: %s\n" % (city,weather,temp,time)
    return weather

def play():
    history_weather = []
    while True:
        try:
            user_input = input("请输入要查询的城市：")
            result = fetchWeather(user_input)
            user_weather = weatherPresent(result)
            print(user_weather)
            history_weather.append(user_weather)

        except:
            if user_input in ['h', 'help', 'H']:
                print(
                '''
                输入城市，查询实时天气；
                输入 help，查看帮助文档；
                输入 history, 查看历史查询；
                输入 quit, 退出查询。
                '''
                )
            elif user_input == 'history':
                for history in history_weather:
                    print(history)
            elif user_input == 'quit':
                print('您已退出查询，感谢使用')
                exit()
            else:
                print('无法识别该城市名或命令，请重新输入')



play()
