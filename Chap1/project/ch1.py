# coding=utf-8

print("天气查询小工具")

# 把 weather_info 保存为 dict 类型
city_weather = {}
history = {}

f = open('weather_info.txt', 'r',encoding='utf-8')
for line in f:
    (city, weather) = line.strip().split(',')
    city_weather[city] = weather

while True:
    user_input = input('请输入命令或要查询的城市名:')
    if user_input in city_weather.keys():
        weather = city_weather[user_input]
        history[user_input] = weather
        print ('%s的天气状况为:%s' %(user_input, weather))

    elif user_input == "help":
        print(
        """
         输入城市名，查询天气；
         输入 help, 获取帮助说明；
         输入 history, 获取查询历史；
         输入 quit, 退出查询程序。
        """
        )
    elif user_input == "history":
        for user_input in history:
            print (user_input, history[user_input])
        else:
            print ('尚未查询')
    elif user_input == "quit":
        break
    else:
        print ("输入的指令不存在，重新输入")
    f.close()
