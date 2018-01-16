import praw

client_id = 'AViZAd_JlI4BQA'
client_secret = 'Rfln6LWhj2McideE6oxOGXx7ZBg'
password = 'iamstarlord'
user_agent = '/u/PaperGalaxyKey reddit bot test'
username = 'PaperGalaxyKey'

reddit = praw.Reddit(client_id, client_secret, password, user_agent, username)
