class Subscription():
    """defines what properties will be on an object representation of a subscription.
    """

    def __init__(self, created_on, follower_id, author_id):
        self.created_on = created_on
        self.follower_id = follower_id
        self.author_id = author_id
        self.follower = None
        self.author = None
