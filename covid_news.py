from newsapi import NewsApiClient
import pyttsx3
from datetime import datetime, timedelta
import pyttsx3


# Initiate the new reading engine
conversionEngine = pyttsx3.init()
voices = conversionEngine.getProperty('voices')  
conversionEngine.setProperty('rate', 160)
conversionEngine.setProperty('voice', voices[0].id) 
newsapi = NewsApiClient(api_key='Put your key here') #Register at newsapi.org

top_headlines = newsapi.get_top_headlines(q='COVID-19', 
                                          sources='bbc-news',
                                          language='en', 
                                          page=2)

for item in top_headlines['articles']:
    conversionEngine.say(item['description'])
    conversionEngine.runAndWait()
    conversionEngine.end()

# all_articles = newsapi.get_everything(q='COVID-19',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,CNN.com',
#                                       from_param=(datetime.now() - timedelta(1)).strftime('%Y-%m-%d'),
#                                       to=datetime.today().strftime('%Y-%m-%d'),
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# for item in all_articles['articles']:
#     conversionEngine.say(item['description'])
#     conversionEngine.runAndWait()
                                 