import sqlite3
import json
from models import Tag, Post, PostTag


def get_post_tags(post_id):
    '''Fetches all tags for a post'''
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id,
            t.label
        FROM posttags pt
        JOIN tags t
            ON pt.tag_id = t.id
        WHERE pt.post_id = ?
        """, (post_id, ))

        post_tags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = PostTag(row['id'], row['post_id'], row['tag_id'])
            tag = Tag(row['tag_id'], row['label'])

            post_tag.tag = tag.__dict__
            post_tags.append(post_tag.__dict__)

        return json.dumps(post_tags)
