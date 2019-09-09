import praw

# user_agent = "/u/PaperGalaxyKey reddit bot test"

# subreddit("AwakeSeeker887")

reddit = praw.Reddit('bot1')
for submission in reddit.subreddit("AwakeSeeker887").hot():
    print("\tTitle:\t",submission.title)
    if submission.title == "test post please ignore":
        
# for submission in reddit.front.hot(limit=5):
#     print("\tTitle:\t",submission.title)
#     # print(submission.body)
#     if submission.is_self:
#         print("selfpost")

