import praw

if __name__ == "__main__":
    reddit = praw.Reddit(
        client_id="hriuWbbrwdeEXABkTLbXfw",
        client_secret="bPFIO-dqgtgYwcxuljg5nJdTDz-ksQ",
        user_agent='',
        username="Odd-Fudge-8518",
        redirect_uri='http://localhost:65010/reddit_callback'
    )
    # print(reddit.auth.scopes())
    print(reddit.user.me())
    # PWU5yRtbcD!.L?
    """
    https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
    Odd-Fudge-8518
    #PWU5yRtbcD!.L?
    """