import re
from operator import itemgetter
import math
# from PyDictionary import PyDictionary
# import nltk
# nltk.download('averaged_perceptron_tagger')
# create function to parse each comment into array of words
# remove all nonalphabetical characters from ends of words
# get frequency of each word and put into json object
# return most used words
# filter out posts with kid related tags
# dictionary = PyDictionary()
# if "Noun" in dictionary.meaning("dog").keys():
#     print('dog')
# print(dictionary.meaning("the"))

def upperAndLowerBoundsWordLength(word_list):
    filtered_word_list = []
    for word in word_list:
        if len(word) <= 12 and len(word) > 1:
            filtered_word_list.append(word)
    return filtered_word_list
            

def commentToWordList(body):
    body = re.sub(r'[^\w\s]', '', body).lower()
    word_list = body.split(" ")
    word_list = upperAndLowerBoundsWordLength(word_list)
    # print(nltk.pos_tag(word_list))
    return word_list

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
    return word_freq_list

def filterOutCommonWords(word_freq_list):
    commonWords = [line.rstrip('\n') for line in open("commonWords.txt")]
    filtered_list = []
    for word, freq in word_freq_list:
        if not word in commonWords and word != "" and len(word) > 1:
            # if freq > 2:
            filtered_list.append([word, freq])
    return filtered_list

def filterOutInfrequentWords(word_freq_list):
    max_freq = word_freq_list[0][1]
    min_freq = math.sqrt(max_freq)
    
    filtered_list = []
    for word, freq in word_freq_list:
        if (freq > min_freq):
            filtered_list.append([word, freq])
    num_words = len(filtered_list)      
    # print("Returned Tags:  ", len(filtered_list))
    return filtered_list
    
        

if __name__ == '__main__':
    commentToWordList("rain: The sunniest, sir Trump: Looks like another sunny The sunniest, sir Trump Trump: Looks like another sunny The")