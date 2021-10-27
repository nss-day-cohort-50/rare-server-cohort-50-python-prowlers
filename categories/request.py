import sqlite3
import json
from models import Category


def get_all_categories():
    """fetches all users"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.label
        FROM Categories u
        """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    return json.dumps(categories)

# Function to create category
def create_category(new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            (  label )
        VALUES
            (  ?)
        """, (new_category['label'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the category dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_category['id'] = id


    return json.dumps(new_category)

# Function with a single parameter
def get_single_category(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.label
        FROM categories a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an category instance from the current row
        category = Category(data['id'], data['label'])

        return json.dumps(category.__dict__)

def delete_category(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM categories
        WHERE id = ?
        """, (id, ))