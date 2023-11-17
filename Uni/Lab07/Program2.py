import threading
import json
import time

def Read_file(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()
    tweets = []
    for line in file_contents.splitlines():
        tweet = json.loads(line)
        tweets.append(tweet)

files = [r"D:\Python-Project\Uni\Lab07\Tweets\TweetsPart1.txt", r"D:\Python-Project\Uni\Lab07\Tweets\TweetsPart2.txt", r"D:\Python-Project\Uni\Lab07\Tweets\TweetsPart3.txt"]

start_time = time.time()

threads = []
for file in files :
    thread = threading.Thread(target=Read_file, args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
total_time = end_time - start_time
print("Total time is :", total_time)