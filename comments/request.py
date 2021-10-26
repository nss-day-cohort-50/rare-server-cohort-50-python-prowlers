import sqlite3
import json
from models import Comment, Post, User


def get_all_comments():
    """fetches all comments"""
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            *,
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.created_on,
            p.content post_id,
            c.author_id user_id
        FROM Comments c
<<<<<<< HEAD
        JOIN Posts p
            ON p.id = c.post_id
        JOIN Users u
            ON u.id = c.author_id
=======
        JOIN Users u 
            ON u.id = c.author_id
        JOIN Posts p
            ON p.id = c.post_id
>>>>>>> main
        """)

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            comment = Comment(row['id'], row['post_id'],
                              row['author_id'], row['content'], row['created_on'])

            post = Post(row['id'], row['user_id'],
                        row['category_id'], row['title'],
                        row['publication_date'], row['image_url'], row['content'], row['approved'])

            user = User(row['id'], row['first_name'], row['last_name'],
                        row['email'], row['bio'], row['username'], row['password'],
                        row['profile_image_url'], row['created_on'], row['active'])

            comment.user = user.__dict__
            comment.post = post.__dict__
            comments.append(comment.__dict__)

        return json.dumps(comments)


def get_single_comment(id):
    """fetches individual comment"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.created_on
        FROM Comments c
        WHERE c.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        comment = Comment(data['id'], data['post_id'],
                          data['author_id'], data['content'], data['created_on'])

        return json.dumps(comment.__dict__)


def create_comment(new_comment):
    """creates a new comment"""
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( post_id, author_id, content, created_on )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_comment['post_id'], new_comment['author_id'],
            new_comment['content'], new_comment['created_on']))

        id = db_cursor.lastrowid

        new_comment['id'] = id

    return json.dumps(new_comment)

def delete_comment(id):
    """deletes individual comment"""
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))

def update_comment(id, new_post):
    """updates individual comment"""
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comments
            SET
                post_id = ?,
                author_id = ?,
                content = ?,
                created_on = ?
        WHERE id = ?
        """, (new_post['post_id'], new_post['author_id'],
            new_post['content'], new_post['created_on'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
        