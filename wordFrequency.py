import re
from operator import itemgetter

# create function to parse each comment into array of words
# remove all nonalphabetical characters from ends of words
# get frequency of each word and put into json object
# return most used words
# filter out posts with kid related tags


def commentToWordList(body):
    body = re.sub(r'[^\w\s]', '', body).lower()
    word_list = body.split(" ")
    return word_list

def removeRareTags(word_dict):
    new_word_dict = {}
    for word in word_dict:
        # print(word_dict[word])
        if word_dict[word] > 1:
            print(word, word_dict[word])
            # new_word_dict.update(word)
            
    print(new_word_dict)
# combine word_list for each comment into one large word list, then get frequency
# filter out generic words(of, a , to, and, the, an)
def wordListToWordFreq(word_list):
    big_list = [["",0]]
    for word in word_list:
        word_pair = [word, word_list.count(word)]
        if not word_pair in big_list:
            big_list.append(word_pair)
    return big_list
    
def sortWordFreqList(word_freq_list):
    word_freq_list.sort(key=itemgetter(1), reverse=True)
    # print(word_freq_list)
    return word_freq_list

def filterOutCommonWords(word_freq_list):
    common_words = ["the", "i", "a", "of","to","is","in","like","and","this","that","on","do","it",""]
    avoid_words = ["child","kid","human"]
    good_words = ["dog","doggy"]
    for word_pair in word_freq_list:
        if word_pair[1] > 3:
            print(word_pair[0],"\t\t",word_pair[1])

# def removeCommonWords(word_list):
    
#     for word in word_list:
        

if __name__ == '__main__':
    commentToWordList("rain: The sunniest, sir Trump: Looks like another sunny The sunniest, sir Trump Trump: Looks like another sunny The")