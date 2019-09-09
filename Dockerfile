FROM python:3

ADD praw.ini /
ADD redditidea.py /

RUN pip install praw

CMD [ "python", "redditidea.py" ]