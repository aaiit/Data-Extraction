import tweepy
import webbrowser
import time
import json
import os
import zipfile
import wget

consumer_key ="UFkzPnRg6teYYVpopicJlHu2L"
consumer_secret = "CNuHKlXlI4nY2YtX1RFFwthZQ0ziebfkLfrxd6T6xZp9FX7w7P"

callback_url = 'oob'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret,callback_url)
redirect_url = auth.get_authorization_url()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api=tweepy.API(auth,timeout=11)



def downloadImages(fields):
	media_files = set()
	k=0
	for status in tweepy.Cursor(api.search,q=fields["q"],count=fields["len"],
							   lang=fields["lang"],
							   since="2020-08-14").items():
		media = status.entities.get('media', [])
		if(len(media) > 0):
			media_files.add(media[0]['media_url'])
		# print (status.created_at, status.text)
	for media_file in media_files:
		wget.download(media_file,out="Imagesdownl")
		k+=1
		print(k)

	def zipdir(path, ziph):
		for root, dirs, files in os.walk(path):
			for file in files:
				ziph.write(os.path.join(root, file))

	zipf = zipfile.ZipFile('hello/static/Imagesdownl.zip', 'w', zipfile.ZIP_DEFLATED)
	zipdir('Imagesdownl/', zipf)
	zipf.close()