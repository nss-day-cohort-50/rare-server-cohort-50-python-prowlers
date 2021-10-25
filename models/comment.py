class Comment():
    """defines what properties will be on an object representation of a Comment.
    """

    def __init__(self, post_id, author_id, content, created_on):
        self.post_id = post_id
        self.author_id = author_id
        self.content = content
        self.created_on = created_on
        self.post = None
        self.author = None
