from lib2to3.pgen2 import driver
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#自動で検索するためのメソッド
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
import sys, os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MAX_PAGE = 2


#ブラウザ操作を自動化するドライバ
def Driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver"), options=options)
    #driver.get("https://www.google.co.jp")
    return driver

#検索結果ページ(1ページ目、２ページ目、...、MAX_PAGE目のURLをリストに格納)
def getPageURL(search_query, MAX_PAGE=MAX_PAGE):
    
    driver = Driver()
    driver.get("https://www.google.co.jp")
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys(search_query)
    search_bar.send_keys(Keys.ENTER)

    pageLIST = []
    pageLIST.append(driver.current_url)
    pagelinks = driver.find_elements(By.XPATH, '//div/table/tbody/tr/td/a')
    for page in range(MAX_PAGE-1):
        
        #print(pagelink.get_attribute("href"))
        pageLIST.append(pagelinks[page].get_attribute("href"))
    return pageLIST


    

def index(request):
    # qu = request.POST['qu']
    # MyURL = request.POST['MyURL']
    # print(qu, MyURL)
    # #headline, rank = search_ranking(search_query=query, MyURL=MyURL)
    # # dict = {
    # #     "headline": headline,
    # #     "rank": rank
    # # }
    return render(request, "index.html")

#入力された検索クエリ、対象URLをもとにGoogleの掲載順位を調査
def searchRank(request):

    dict = {}
    if request.method=="POST":
        qu = request.POST.get('qu')
        MyURL = request.POST.get('MyURL')
        #print(type(qu), MyURL)

        pageList = getPageURL(qu)
        #print(len(pageList))
        rank = 0
        find_flg = False
        for i in range(len(pageList)):
            driver = Driver()
            driver.get(pageList[i])
            headlines = driver.find_elements(By.XPATH, "//a/h3") #検索ページ内の見出しをすべて取得
            for headline in headlines:
                rank += 1
                a_element = headline.find_element(By.XPATH, "..") #見出しの上の階層にあるaタグを取得し、
                url = a_element.get_attribute("href")             #見出しに付随するURLを取得 k近傍法　回帰
                
                #MyURLが含まれているか確認
                if MyURL in url:
                    find_flg = True
                    dict["headline"] = f"記事タイトル: {headline.text}"
                    dict["rank"] = f"{rank}位"
                    break
            
            if find_flg:
                break
        if find_flg==False:
            dict["headline"] = f"1~{MAX_PAGE}ページ中にはありませんでした"
            dict["rank"]= "なし"
    
    return render(request, "result.html", dict)