#1

import requests
import pandas as pd
import json
import bs4

key = "a8e597633acca03091ad5fba598b58a7"
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=" + key
parameter = {"directorNm": "봉준호"}

response = requests.get(url, parameter)
content_text = response.text
content_text2 = BeautifulSoup(content_text, 'html.parser')
content_json = response.json()

movie = pd.DataFrame(content_json['movieListResult']['movieList'])
movie = movie.sort_values('prdtYear')
movie['directors'] = movie['directors'][0][0]['peopleNm']

for i in range(0, len(movie), 1):
    if movie['companys'][i] == []:
        movie['companys'][i] = []
    else:
        movie['companys'][i] = movie['companys'][i][0]['companyNm']

#2

date = pd.date_range('20180101', '20181231')
date

Time = []
for time in date:    
    Time.append(date.strftime("%Y%m%d").tolist())
    
time_list=Time[0]

data = []

key = 'a8e597633acca03091ad5fba598b58a7'
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=" + key + "&targetDt="
df_default = pd.DataFrame()

for k in range(len(time_list)):
    requestData2 = requests.get(url+str(time_list[k])+'')
    data_2 = requestData2.json()
    data = data_2['boxOfficeResult']['dailyBoxOfficeList']
    df = pd.DataFrame.from_dict(data)
    df_default = df_default.append(df)

df_default.to_csv('data_result.csv',encoding='utf-8', index = False)

pd.read_csv('data_result.csv')