import praw
reddit = praw.Reddit('bot1')

# while (True):
for submission in reddit.subreddit("AwakeSeeker887").new():
    if submission.num_comments > 0:
        for comment in submission.comments:
            comment_body = comment.body
            print(comment_body)
            if "!PGK" in comment_body:
                comment.reply("i am a bot") 
            