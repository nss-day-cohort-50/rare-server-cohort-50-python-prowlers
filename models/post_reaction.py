class PostReaction():
    """defines what properties will be on an object representation of a PostReaction.
    """

    def __init__(self, user_id, post_id, reaction_id):
        self.user_id = user_id
        self.post_id = post_id
        self.reaction_id = reaction_id
        self.user = None
        self.post = None
        self.reaction = None
