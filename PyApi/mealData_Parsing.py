# mealData_Parsing API

import requests
from bs4 import BeautifulSoup
import re

def mealSearch(mealType): # 음식의 타입을 받아들임 ex) lunch , Dinner
    ## 검색어: 남주고등학교 급식 < 네이버
    req = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=남주고등학교 급식')

    date = '10월 27일'

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')

    Nj_MealData = soup.find_all('li', attrs={'class':'menu_info'})
    Nj_MealData = re.sub('<[^>]+>', '', str(Nj_MealData), 0)
    Nj_MealData = re.sub('[a-z]+', '', str(Nj_MealData), 0)
    Nj_MealData = Nj_MealData.replace('  ', '')

    if(mealType == 'Lunch'):
        return Nj_MealData.split(date + ' [점심]')[1].split(',')[0]
    if(mealType == 'Dinner'):
        return Nj_MealData.split(date + ' [저녁]')[1].split(',')[0]
    else:
        return '입력된 값에 오류가 있습니다.'