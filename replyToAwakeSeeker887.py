import praw
reddit = praw.Reddit('bot1')

already_replied = []
while (True):
    for submission in reddit.subreddit("AwakeSeeker887").new():
        if submission.num_comments > 0:
            for comment in submission.comments:
                print(comment.id)
                print("\t",comment.body)
                if "!PGK" in comment.body and (comment.id not in already_replied):
                    # comment.reply("i am a bot") 
                    print('I would post a comment')
                    already_replied.append(comment.id)
                    print(already_replied)
                else:
                    print("i already replied to this comment")
            