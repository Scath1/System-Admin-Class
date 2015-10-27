import feedparser


feeddata = feedparser.parse("http://www.reddit.com/r/python/.rss")


for post in feeddata.entries:
	print post.title + ": "+ post.link + "\n"


print feeddata["entries"][0]["title"]