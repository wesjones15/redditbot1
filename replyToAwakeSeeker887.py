import praw
import time
import random
from checkIfBotHasUsedComment import *
from wordFrequency import *

reddit = praw.Reddit('bot1')

def generateReplyToComment(body, author):
    # print(body)
    split_body = body.split("!PGK")
    
    text_after_tag = split_body[-1].strip(" ")
    
    # print(text_after_tag)
    # print(author)
    # reply = "Hello, u/"+str(author)+". You said: "+text_after_tag
    reply_soup = text_after_tag.split(" ")
    if len(reply_soup) <= 4:
        reply = text_after_tag+"?"
    else:
        reply = ""
        phrase_size = random.randint(3,7)
        for i in range(0,phrase_size):
            rN = random.randint(0,len(reply_soup)-1)
            reply+= reply_soup[rN]+" "
        reply += "?"
        # print("reply", reply)
    # print(reply)
    return reply

if __name__ == '__main__':
    word_list_main = []
    for submission in reddit.subreddit("aww").hot(limit=1):
        for comment in submission.comments:
            word_list = commentToWordList(comment.body)
            word_list_main += word_list
        word_list_main.sort()
        word_freq_list = wordListToWordFreq(word_list_main)
        word_freq_list = sortWordFreqList(word_freq_list)
        filterOutCommonWords(word_freq_list)
        # for i in range(0, 3):
        #     print(word_freq_list[i][0], word_freq_list[i][1])
        # print(sorted(word_freq_list))
        # removeRareTags(word_freq_dict)
        # print(freq_dict)
    # keyword = "trump"   # "!PGK"
    # while (True):
    #     for submission in reddit.subreddit("politics").new():
    #         if submission.num_comments > 0:
    #             for comment in submission.comments:
    #                 if keyword in comment.body.lower():
    #                     # print("!PGK tag located")
    #                     # print("\n\tComment:\t",comment.body)
    #                     if not checkIfBotHasUsedComment(comment.fullname):
    #                         reply = generateReplyToComment(comment.body, comment.author)
    #                         # print("\n\treply: 'i am a bot'")
    #                         # comment.reply(reply)
    #                         print("\n\t/u/PaperGalaxyKey commented: ", reply,"\n")
    #                         writeCommentToUsedCommentsList(comment)
    #                         time.sleep(.5)
    #                     else:
    #                         print("\t\ti already replied to this comment")
                        
                