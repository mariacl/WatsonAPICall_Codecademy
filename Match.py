#Comparing tweets from 2 different users to produce a Personality Insights report with IBM Watson API. Code from Codecademy online course.
import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

def analyze(handle):
#Retrieving 200 tweets from a public Twitter account.
	twitter_consumer_key = 'wIaufOevg1dIIx1MikKejJ8d6'
	twitter_consumer_secret = 'J1gxhHnBOgpOHsVbdC6hBcSiVE1q9EmrDARlffzI9NLU7AmWOR'
	twitter_access_token = '910975459713847297-PzTKZIDLOtCiEPu6x9GaQXXma7iXHAU'
	twitter_access_secret = '2PZTyvmPXzfCLbkM4fTGuuImXwWICgrCiaBXWOaC5E91i'

#instances the twitter API with my API keys
	twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)



#retrieves 200 tweets from the handle account avoiding rts (retweets)
	statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

	text = ""

#filters for English tweets, and encodes Unicode Twitter format into UTF-8. Then concatenates all tweets into one long string.
	for status in statuses:
    if (status.lang =='en'): #English tweets
        	text += status.text.encode('utf-8')

	pi_username = "f1e67009-45f7-4646-8cae-a5fb773346ff"
	pi_password = "0t2mEQ703FLc"

	personality_insights = PersonalityInsights(username = pi_username, password =pi_password)

	pi_result = personality_insights.profile(text)

	return pi_result

def flatten(orig):
  data ={}
  for c in orig['tree']['children']:
    if 'children' in c:
      for c2 in c['children']:
        if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data
  
  def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
                compared_data[keys]=abs(dict1[keys] - dict2[keys])
    return compared_data
  
  user_handle = "@Codecademy"
  celebrity_handle = "@IBM"
  
  user_result=analyze(user_handle)
  celebrity_result=analyze(celebrity_handle)
  
  user =flatten(user_result)
  celebrity=flatten(celebrity_result)
  
  compared_results = compare(user,celebrity)
  
  #sort results and display top 5 traits shared between Twitter accounts selected
  
  sorted_result = sorted(compared_results.items(),key=operator.itemgetter(1))
  
  for keys, value in sorted_result[:5]:
    print keys,
    print(user[keys]).
    print ('->'),
    print (celebrity[keys]),
    print ('->'),
    print (compared_results[keys])
    
  
