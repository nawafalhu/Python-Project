<<<<<<< HEAD
import json
import time

start_time = time.time()

# Tweet 1
with open(r"D:\Python-Project\Uni\Lab07\Tweets\TweetsPart1.txt", "r") as f1:
    file_contents1 = f1.read()
tweets1 = []
for line in file_contents1.splitlines():
    tweet1 = json.loads(line)
    tweets1.append(tweet1)

# Tweet 2
with open(r"D:\Python-Project\Uni\Lab07\Tweets\TweetsPart2.txt", "r") as f2:
    file_contents2 = f2.read()
tweets2 = []
for line in file_contents2.splitlines():
    tweet2 = json.loads(line)
    tweets2.append(tweet2)

# Tweet 3
with open(r"D:\Python-Project\Uni\Lab07\Tweets\TweetsPart3.txt", "r") as f3:
    file_contents3 = f3.read()
tweets3 = []
for line in file_contents3.splitlines():
    tweet3 = json.loads(line)
    tweets3.append(tweet3)

# Tweet 1
created_at1 = []
user1 = []
text1 = []
for num in range(0,len(tweets1) - 1):
    if "created_at" in tweets1[num] :
        created_at1.append(tweets1[num]['created_at'])
    if "user" in tweets1[num] :
        user1.append(tweets1[num]["user"]['screen_name'])
    if "text" in tweets1[num] :
        text1.append(tweets1[num]['text'])

# Tweet 2
created_at1 = []
user1 = []
text1 = []
for num in range(0,len(tweets1) - 1):
    if "created_at" in tweets1[num] :
        created_at1.append(tweets1[num]['created_at'])
    if "user" in tweets1[num] :
        user1.append(tweets1[num]["user"]['screen_name'])
    if "text" in tweets1[num] :
        text1.append(tweets1[num]['text'])

# Tweet 3
created_at1 = []
user1 = []
text1 = []
for num in range(0,len(tweets1) - 1):
    if "created_at" in tweets1[num] :
        created_at1.append(tweets1[num]['created_at'])
    if "user" in tweets1[num] :
        user1.append(tweets1[num]["user"]['screen_name'])
    if "text" in tweets1[num] :
        text1.append(tweets1[num]['text'])

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("Total time is :", total_time)



sample = {'created_at': 'Sun Jan 01 01:00:51 +0000 2017', 'id': 815362116110651392, 'id_str': '815362116110651392', 
          'text': 'Can my neighbors stop their party and go to sleep pls', 'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', 
          'truncated': False, 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 
          'user': {'id': 1154969916, 'id_str': '1154969916', 'name': 'karen', 'screen_name': 'KarenMneimneh', 'location': 'Lebanon', 'url': None, 'description': None, 'protected': False, 
                   'verified': False, 'followers_count': 49, 'friends_count': 71, 'listed_count': 0, 'favourites_count': 217, 'statuses_count': 636, 'created_at': 'Wed Feb 06 20:17:07 +0000 2013', 
                   'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'lang': 'en', 'contributors_enabled': False, 'is_translator': False, 'profile_background_color': 'C0DEED', 
                   'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 
                   'profile_background_tile': False, 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 
                   'profile_use_background_image': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/783735232474251265/sHh1LFch_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/783735232474251265/sHh1LFch_normal.jpg', 
                   'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1154969916/1475692155', 'default_profile': True, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None}, 
          'geo': None, 'coordinates': None, 'place': {'id': '583bd538eb3129d1', 'url': 'https://api.twitter.com/1.1/geo/id/583bd538eb3129d1.json', 'place_type': 'country', 'name': 'Lebanon', 'full_name': 'Lebanon', 'country_code': 'LB', 'country': 'Lebanon', 
                                                      'bounding_box': {'type': 'Polygon', 'coordinates': [[[35.075771, 33.054742], [35.075771, 34.691989], [36.623258, 34.691989], [36.623258, 33.054742]]]}, 'attributes': {}}, 'contributors': None, 'is_quote_status': False, 
=======
import json
import time

start_time = time.time()

# Tweet 1
with open(r"D:\Python-Project\Uni\Lab07\Tweets\TweetsPart1.txt", "r") as f1:
    file_contents1 = f1.read()
tweets1 = []
for line in file_contents1.splitlines():
    tweet1 = json.loads(line)
    tweets1.append(tweet1)

# Tweet 2
with open(r"D:\Python-Project\Uni\Lab07\Tweets\TweetsPart2.txt", "r") as f2:
    file_contents2 = f2.read()
tweets2 = []
for line in file_contents2.splitlines():
    tweet2 = json.loads(line)
    tweets2.append(tweet2)

# Tweet 3
with open(r"D:\Python-Project\Uni\Lab07\Tweets\TweetsPart3.txt", "r") as f3:
    file_contents3 = f3.read()
tweets3 = []
for line in file_contents3.splitlines():
    tweet3 = json.loads(line)
    tweets3.append(tweet3)

# Tweet 1
created_at1 = []
user1 = []
text1 = []
for num in range(0,len(tweets1) - 1):
    if "created_at" in tweets1[num] :
        created_at1.append(tweets1[num]['created_at'])
    if "user" in tweets1[num] :
        user1.append(tweets1[num]["user"]['screen_name'])
    if "text" in tweets1[num] :
        text1.append(tweets1[num]['text'])

# Tweet 2
created_at1 = []
user1 = []
text1 = []
for num in range(0,len(tweets1) - 1):
    if "created_at" in tweets1[num] :
        created_at1.append(tweets1[num]['created_at'])
    if "user" in tweets1[num] :
        user1.append(tweets1[num]["user"]['screen_name'])
    if "text" in tweets1[num] :
        text1.append(tweets1[num]['text'])

# Tweet 3
created_at1 = []
user1 = []
text1 = []
for num in range(0,len(tweets1) - 1):
    if "created_at" in tweets1[num] :
        created_at1.append(tweets1[num]['created_at'])
    if "user" in tweets1[num] :
        user1.append(tweets1[num]["user"]['screen_name'])
    if "text" in tweets1[num] :
        text1.append(tweets1[num]['text'])

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("Total time is :", total_time)



sample = {'created_at': 'Sun Jan 01 01:00:51 +0000 2017', 'id': 815362116110651392, 'id_str': '815362116110651392', 
          'text': 'Can my neighbors stop their party and go to sleep pls', 'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', 
          'truncated': False, 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 
          'user': {'id': 1154969916, 'id_str': '1154969916', 'name': 'karen', 'screen_name': 'KarenMneimneh', 'location': 'Lebanon', 'url': None, 'description': None, 'protected': False, 
                   'verified': False, 'followers_count': 49, 'friends_count': 71, 'listed_count': 0, 'favourites_count': 217, 'statuses_count': 636, 'created_at': 'Wed Feb 06 20:17:07 +0000 2013', 
                   'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'lang': 'en', 'contributors_enabled': False, 'is_translator': False, 'profile_background_color': 'C0DEED', 
                   'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 
                   'profile_background_tile': False, 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 
                   'profile_use_background_image': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/783735232474251265/sHh1LFch_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/783735232474251265/sHh1LFch_normal.jpg', 
                   'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1154969916/1475692155', 'default_profile': True, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None}, 
          'geo': None, 'coordinates': None, 'place': {'id': '583bd538eb3129d1', 'url': 'https://api.twitter.com/1.1/geo/id/583bd538eb3129d1.json', 'place_type': 'country', 'name': 'Lebanon', 'full_name': 'Lebanon', 'country_code': 'LB', 'country': 'Lebanon', 
                                                      'bounding_box': {'type': 'Polygon', 'coordinates': [[[35.075771, 33.054742], [35.075771, 34.691989], [36.623258, 34.691989], [36.623258, 33.054742]]]}, 'attributes': {}}, 'contributors': None, 'is_quote_status': False, 
>>>>>>> 40b695b7b8c1e383f5e04d5a00bb5c0d7e5c5353
                                                      'retweet_count': 0, 'favorite_count': 0, 'entities': {'hashtags': [], 'urls': [], 'user_mentions': [], 'symbols': []}, 'favorited': False, 'retweeted': False, 'filter_level': 'low', 'lang': 'en', 'timestamp_ms': '1483232451833'}