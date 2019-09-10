def topTagsToReply(word_freq_list):
    reply = ""
    topTag = word_freq_list[0][0]
    topTagFreq = word_freq_list[0][1]
    # print("Top Tag:\t", topTag)
    for i in range(0, 3):
        if (len(word_freq_list) > i):
            word = word_freq_list[i][0]
            reply += word + " "
    reply = reply.strip(" ")
    return reply

# def reduceTagRedundancy(reply):
#     tags = reply.split(" ")
#     # print(tags)
#     count = 0
#     for tag in tags:
#         for i in tags:
#             if tag in i:
#                 if tag != i:
#                     print(tag, i)
#                     count += 1
            