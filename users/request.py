import sqlite3
import json
from models import User


def get_all_users():
    """fetches all users"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Users u
        """)

        users = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            user = User(row['id'], row['first_name'], row['last_name'],
                        row['email'], row['bio'], row['username'], row['password'],
                        row['profile_image_url'], row['created_on'], row['active'])

            users.append(user.__dict__)

    return json.dumps(users)


def create_user(new_user):
    """registers a new user"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Users
            ( first_name, last_name, email, bio, username, password, profile_image_url, created_on, active )
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?, ?, ? );
        """, (new_user['first_name'], new_user['last_name'],
            new_user['email'], new_user['bio'], new_user['username'],
            new_user['password'], new_user['profile_image_url'], new_user['created_on'],
            new_user['active'], ))

        id = db_cursor.lastrowid

        new_user['id'] = id
    return json.dumps(new_user)


def get_single_user(id):
    """fetches a single user"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Users u
        WHERE u.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        user = User(data['id'], data['first_name'], data['last_name'],
                    data['email'], data['bio'], data['username'], data['password'],
                    data['profile_image_url'], data['created_on'], data['active'])

        return json.dumps(user.__dict__)

def login_user(obj):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT email, id
        FROM Users
        WHERE email = ?
        """, (obj['username'], ))

        login = db_cursor.fetchone()

        if login:
            return json.dumps({"valid":True, "id": login["id"] })

        else:
            return json.dumps({"valid":False})

def delete_user(id):
    """deletes a user"""
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM User
        WHERE id = ?
        """, ( id, ))
