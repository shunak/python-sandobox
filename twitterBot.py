import os
import twitter

auth = twitter.OAuth(consumer_key=os.environ['CONSUMER_KEY'],
consumer_secret=os.environ['CONSUMER_SECRET'],
token=os.environ['ACCESS_TOKEN'],
token_secret=os.environ['ACCESS_TOKEN_SECRET'])

# auth = twitter.OAuth(consumer_key="",
# consumer_secret="",
# token="",
# token_secret="")

t = twitter.Twitter(auth=auth)

#ツイートのみ
status="Hello,World" #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿

#画像付きツイート
pic=""　#画像を投稿するなら画像のパス
with open(pic,"rb") as image_file:
 image_data=image_file.read()
pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
t.statuses.update(status=status,media_ids=",".join([id=img1]))











