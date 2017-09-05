# coding:utf-8
import urllib, urllib2, sys
import json
# import urllib
from matplotlib import pyplot as plt
from collections import Counter

host = 'http://saweather.market.alicloudapi.com'
path = '/day15'
method = 'GET'
appcode = '57ea4457f10549a2980bcc3c2e2514f2'
querys = 'areaid=101210113'
bodys = {}
url = host + path + '?' + querys


request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib2.urlopen(request)
# response = urllib.urlopen(url, headers=)
content = response.read()
if (content):
    # print(content)
    # contentJson = json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    # print(contentJson)
    contentjson = eval(content)
    if (not contentjson['showapi_res_error']):
        information = contentjson['showapi_res_body']['dayList']
        # print(information)
        air_temperature = [{} for count in range(len(information))]
        for i, _ in enumerate(information):
            air_temperature[i]['daytime'] = information[i]['daytime']
            air_temperature[i]['night'] = information[i]['night_air_temperature']
            air_temperature[i]['day'] = information[i]['day_air_temperature']
        # print air_temperature
        for i, _ in enumerate(air_temperature):
            print air_temperature[i]

        # 折线图
        daytime = [air['daytime'] for i, air in enumerate(air_temperature)]
        daytimetemp = [i for i, _ in enumerate(air_temperature)]
        air_day = [int(air['day']) for i, air in enumerate(air_temperature)]
        air_night = [int(air['night']) for i, air in enumerate(air_temperature)]
        air_minus = [int(air['day'])-int(air['night']) for i, air in enumerate(air_temperature)]
        # print air_day
        # print daytime
        plt.plot(daytimetemp, air_day, color='green', marker='o', linestyle='solid')
        plt.plot(daytimetemp, air_night, color='blue', marker='o', linestyle='solid')
        plt.plot(daytimetemp, air_minus, color='red', marker='o')
        plt.show()

        # 柱状图
        day_counts = Counter(air_day)
        night_counts = Counter(air_night)
        xs = range(41)
        # days = [day_counts[str(x)] for x in xs]
        # nights = [night_counts[str(x)] for x in xs]
        days = [day_counts[x] for x in xs]
        nights = [night_counts[x] for x in xs]
        # print days
        plt.bar(xs, days)
        # plt.show()
        plt.bar(xs, nights)
        plt.show()

        # 散点图
        plt.scatter(air_day, air_night)
        plt.xlabel("day")
        plt.ylabel("night")
        plt.axis("equal")
        plt.show()
