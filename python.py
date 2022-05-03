from bs4 import BeautifulSoup
import requests
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

# span - item_title
results = soup.findAll('span','item_title')

print(response.text)

search_rank_file = open("rankresult.txt","a")
print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1


#chapter 3
import requests
import json

city = "Seoul"
apikey = "################################"
lang = "kr"

# units - metric
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

result = requests.get(api)
# print(result.text)

data = json.loads(result.text)

# 지역: name
print(data["name"],"의 날씨입니다.")
# 자세한 날씨: weather-description
print("날씨는 ",data["weather"][0]["description"],"입니다.")
# 현재온도: main-temp
print("현재 온도는 ",data["main"]["temp"],"입니다.")
# 체감온도: main-feels_like
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
# 최저기온: main-temp_min
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
# 최고기온 : main-temp_max
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
# 습도 : main-humidity
print("습도는 ",data["main"]["humidity"],"입니다.")
# 기압 : main-pressure
print("기압은 ",data["main"]["pressure"],"입니다.")
# 풍향 : wind - deg
print("풍향은 ",data["wind"]["deg"],"입니다.")
# 풍속 : wind - speed
print("풍속은 ",data["wind"]["speed"],"입니다.")