import praw, prawcore, argparse, pprint

def authenticate():
    reddit = praw.Reddit('commdel', user_agent="deletes my comments")
    return reddit

def delete(reddit):
    user = reddit.user.me()
    while len(list(user.comments.new())) > 0:
        for comment in user.comments.new(limit=None):
            comment.delete()

if __name__ == "__main__":
    reddit = authenticate()
    delete(reddit)