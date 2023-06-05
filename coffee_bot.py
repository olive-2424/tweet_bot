import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')
import tweepy
import schedule
import time
import datetime

api_key = "666lskWV0Ih3VfAcuQ93wtoSj"
api_secret_key = "7biuddIS65YenyPpqmFpTF1OQXYgBOqFD3idnUWILU5iRhA39Q"
access_token = "1665008289590165506-fdK5tEcLC3AzMzchoEbDgCwPXuHJq6"
access_token_secret = "N1aC79Wh7KNWwK7f0jBbe49IeeFbx1amQr1VRBbyD7bIe"

client = tweepy.Client(
    consumer_key = api_key,
    consumer_secret= api_secret_key,
    access_token = access_token,
    access_token_secret = access_token_secret
)

coffee_knowledges = [
    "コーヒーに含まれるクロロゲン酸は、抗酸化作用がある",
    "カフェインの持続時間はおよそ4時間ほど(個人差はある)",
    "コーヒーの樹はアカネ科の植物",
    "コーヒーには脱臭効果があるので、かすを乾かして容器に入れて消臭剤として利用することができる！！",
    "コーヒーの香りを嗅ぐとα波が出るのでリラックスできる効果がある",
    "コーヒーは1日3~4杯までが適量！！",
    "コーヒーの旨み成分はドリップの前半に、後半は雑味成分が抽出されやすくなる",
    "最初にお湯を注ぐと、粉がもこもこ膨らむのは炭酸ガスが揮発するためで、新鮮な豆の証拠!!",
    "スペシャリティコーヒーの定義によって生産者と消費者の双方に利益をもたらされている",
    "ドリッパーにも色々な形がある"
]
n = 0
date = datetime.datetime.now()
def tweet():
  global n
  global date
  client.create_tweet(text = coffee_knowledges[n] + '::' + str(date.date()))
  n +=1
  if n == len(coffee_knowledges):
    n = 1

schedule.every(2).minutes.do(tweet)

while True:
  schedule.run_pending()
  time.sleep(1)
