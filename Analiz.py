import sys,tweepy ,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt

class SentimentAnalysis:
    def __init__(self):
        self.tweets=[]
        self.tweetText=[]

        def DowloadData(self):
            consumerKey = "bBCzer7M2mtAKeaU8TACUIGsk"
            consumerSecret = "gSVk5nxIUCkoe4bb3BB5mtgNLpzG98QrbnyyRKAL8zOmcyzn7K"
            accessToken = "839835738099355649-wjmZn0p9Htkdsi52qRhCfZ2zQuZzZV4"
            accessTokenSecret = "q2kN1tOwDa2BdBYhbqsZlpzERLHO10IKlmOv7FveRAqgW"
            auth = tweepy.OAutHandler(consumerKey,consumerSecret)
            auth.set_access_token(accessToken,accessTokenSecret)
            api=tweepy.API(auth)

            searchKeyword= input("Aranacak kelimeyi yazınız: ")
            searchNumber=int(input("Analiz edilmesini istediğiniz tweet sayısı: "))

            self.tweets=tweepy.Cursor(api.search,q=searchKeyword,lang = "tr").items(searchNumber)

            fileWriter=open('result.csv', 'a') # twitleri bu dosyaya yazıyoruz
            fileWriter=csv.writer(fileWriter)

            polarity = 0
            positive = 0
            weakPositive = 0
            strongPositive = 0
            negative = 0
            weakNegative = 0
            strongNegative = 0
            neutral = 0

            sayac = 0

            for tweet in self.tweets:
                sayac+=1
                print(sayac,": ", tweet.text)

                self.tweetText.append(self.cleanText(tweet.text).encode('utf-8'))
                analysis = TextBlob(tweet.text).translate(from_lang="tr", to="en")

                polarity +=analysis.sentiment.polarity

                if(analysis.sentiment.polarity==0):
                    neutral += 1
                elif(analysis.sentiment.polarity>0 and analysis.sentiment.polarity <=0.3):
                    weakPositive+=1
                elif(analysis.sentiment.polarity>0.3 and analysis.sentiment.polarity <=0.6):
                    positive+=1
                elif(analysis.sentiment.polarity>0.6 and analysis.sentiment.polarity <=1):
                    strongPositive+=1
                elif(analysis.sentiment.polarity>-0.3 and analysis.sentiment.polarity <=0):
                    weakNegative+=1
                elif(analysis.sentiment.polarity>-0.6 and analysis.sentiment.polarity <=-0.3):
                    negative+=1
                elif(analysis.sentiment.polarity<-1 and analysis.sentiment.polarity <=-0.6):
                    strongNegative+=1







