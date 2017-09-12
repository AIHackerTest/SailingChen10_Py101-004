# coding:utf-8

from flask import Flask, request, render_template
from weather import fetchWeather, weatherPresent

app=Flask(__name__)
history_weather = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request')
def process_request():
    city = request.args.get('city')
    try:
        result = fetchWeather(city)
        weather_str = weatherPresent(result)
        history_weather.append(weather_str)
        return render_template('weather.html', weather_str=weather_str)
    except KeyError:
        if request.args.get('history') == '历史':
            return render_template('history.html', history_weather=history_weather)

        elif request.args.get('help') == '帮助':
            return render_template('help.html')

        else:
            return render_template('404.html')


if __name__ == '__main__':
    app.run()
