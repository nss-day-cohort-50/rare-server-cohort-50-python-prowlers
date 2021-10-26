import sqlite3
import json
from models import Post


def get_all_posts():
    """fetches all posts"""
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM posts p
        """)

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            post = Post(row['id'], row['user_id'],
                        row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])

            posts.append(post.__dict__)

        return json.dumps(posts)


def get_current_user_posts(current_user):
    """fetches current users posts"""
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM posts p
        WHERE p.user_id = ?
        """, (current_user, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            post = Post(row['id'], row['user_id'],
                        row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])

            posts.append(post.__dict__)

        return json.dumps(posts)


def get_single_post(id):
    """fetches single post by id"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM posts p
        WHERE p.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        post = Post(data['id'], data['user_id'],
                    data['category_id'], data['title'],
                    data['publication_date'], data['image_url'], data['content'], data['approved'])

        return json.dumps(post.__dict__)


def delete_post(id):
    """deletes a post from the server"""
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, ))


def create_post(new_post):
    """creates a new post"""
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, category_id. title, publication_date, image_url, content, approved );
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?, ? );
        """, (new_post['user_id'], new_post['category_id'], new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved']))

        id = db_cursor.lastrowid

        new_post['id'] = id

    return json.dumps(new_post)
