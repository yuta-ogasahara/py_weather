import requests
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

CHANNEL_ACCESS_TOKEN = 'aPybBNGVq6NDHacJYQwsQ85HmF4mkLWkttNR8fIqEeAFybruRZ1XTgu/yB7plWZKAGynGoM0QSJjVZ3xHNAibCzued9ooRHyXqzfCQD9whxj0TmLw4YQ3raMfNQbGWaUaLXrsAe2kSS5s+/OiFLxSAdB04t89/1O/w1cDnyilFU='
USER_ID='Ua127f42c01f3dd05f84fe1f680082d78'
def GetWheater():
    url="https://tenki.jp/forecast/6/31/6310/28201/"
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    Weather = soup.find_all("p",class_='weather-telop')
    City_name=soup.select('#main-column > section > h2')
    print("今日の"+City_name[0].contents[0]+"は"+Weather[0].contents[0]+"です。\n明日の"+City_name[0].contents[0]+"は"+Weather[1].contents[0]+"です。")
    return Weather ,City_name
   
def send_message(text):
  
  line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
  
  try:
      line_bot_api.push_message(USER_ID,TextSendMessage(text=text))
  except LineBotApiError as e:
    print(e.message)

if __name__ == "__main__":
  Weather=GetWheater()[0]
  City=GetWheater()[1]
  text ="今日の"+City[0].contents[0]+"は"+Weather[0].contents[0]+"です。\n明日の"+City[0].contents[0]+"は"+Weather[1].contents[0]+"です。"
  send_message(text)



