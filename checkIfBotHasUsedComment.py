import json

def writeCommentToUsedCommentsList(comment):
    with open('usedComments.txt') as json_file:
        usedComments = json.load(json_file)
    usedComments['comments'].append({
        'full_id': comment.fullname,
        'text': comment.body,
        'author': str(comment.author)
    })
    with open('usedComments.txt', 'w') as outfile:
        json.dump(usedComments, outfile)
        
        
def checkIfBotHasUsedComment(comment_fullname):
    with open('usedComments.txt') as json_file:
        usedComments = json.load(json_file)
    for comment in usedComments['comments']: 
        if comment_fullname == comment['full_id']:
            print("I've already replied to this comment", comment_fullname)
            return True
            
    # if it doesn't find the comment in the list
    # print("I have not yet replied to this comment", comment_fullname)
    return False

