import praw
import time
reddit = praw.Reddit('bot1')
# for submission in reddit.subreddit("AwakeSeeker887").hot():
#     print("\tTitle:\t",submission.title)
#     if submission.title == "test post please ignore":
print("\n")
for submission in reddit.subreddit("Seltz").hot(limit=5):
    if not submission.stickied:
        title = submission.title
        author = submission.author
        self_text = submission.selftext
        score = submission.score
        num_comments = submission.num_comments
        # print(title, author, score)
        if (author == "OopsNotAgain"):
            # submission.crosspost(subreddit="AwakeSeeker887", send_replies=False)
            for comment in submission.comments:
                text = comment.body
                # if text
                # print(comment.author,"\t", comment.body)
                
            
        print("\n")
        time.sleep(.5)

# reddit.redditor('AwakeSeeker887').message('TEST', 'test message from PRAW')

