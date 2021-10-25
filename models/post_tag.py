from models import tag


class PostTag():
    """defines what properties will be on an object representation of a PostTag.
    """

    def __init__(self, tag_id, post_id):
        self.tag_id = tag_id
        self.post_id = post_id
        self.tag = None
        self.post = None
