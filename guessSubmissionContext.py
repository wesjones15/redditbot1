import praw
import time
import random
from checkIfBotHasUsedComment import *
from wordFrequency import *
from topTagsToReply import *

reddit = praw.Reddit('bot1')

def returnPopularTagsFromSubreddit(subreddit, limit):
    masterTagList = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        if submission.num_comments > 0:
            # print("\n")
            # print("FROM /r/"+str(submission.subreddit)+":\t", submission.score,"pts")
            # print("u/"+str(submission.author),"\t", submission.num_comments, "comments")

            word_list_submission = []
            submission.comments.replace_more(limit=10)
            comment_queue = submission.comments[:]
            while comment_queue:
                comment = comment_queue.pop(0)
                word_list = commentToWordList(comment.body)
                word_list_submission += word_list

            word_freq_list = wordListToWordFreq(word_list_submission)
            word_freq_list = sortWordFreqList(word_freq_list)
            word_freq_list = filterOutCommonWords(word_freq_list)
            if len(word_freq_list) > 0:
                filtered_list = filterOutInfrequentWords(word_freq_list)
                if (len(filtered_list) > 0):
                    reply = topTagsToReply(filtered_list)
                    # print(reply)
                    # reduceTagRedundancy(reply)
                    masterTagList.append([submission, reply])
    return masterTagList
        
        
if __name__ == '__main__':
    postTagList = returnPopularTagsFromSubreddit("aww", 100)
    # print(postTagList)
    # tagsToCheck = ["dog", "cat", "kid"]
    for submission, tags in postTagList:
        print(submission.permalink)
        print("Comments:",submission.num_comments)
        print("   Score:",submission.score)
        print("    Tags:",tags)
        if not submission.is_self:
            print("   Image:",submission.url)
        print("\n")
        # print("\t", submission.id,"\n")
        # for tag in tagsToCheck:
        #     if tag in tags:
        #         print("It's a "+tag+"!")
