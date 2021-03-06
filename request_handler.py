import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from users import get_single_user, get_all_users, create_user, delete_user, login_user
from posts import get_single_post, get_all_posts, delete_post, create_post, update_post, get_current_user_posts
from comments import get_all_comments, get_single_comment, create_comment, delete_comment, update_comment
from tags import get_all_tags, get_single_tag, create_tag, update_tag, delete_tag
from categories import get_all_categories, create_category, get_single_category, delete_category, update_category
from post_tags import get_post_tags

# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.


class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
            # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'email'
            value = pair[1]  # 'jenna@solis.com'

            return (resource, key, value)

        # No query string parameter
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)

    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, PATCH, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)
        response = {}  # Default response
        parsed = self.parse_url(self.path)
        # Parse the URL and capture the tuple that is returned

        if len(parsed) == 2:
            (resource, id) = self.parse_url(self.path)

            if resource == "users":
                if id is not None:
                    response = f"{get_single_user(id)}"
                else:
                    response = f"{get_all_users()}"
            elif resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"
            elif resource == "comments":
                if id is not None:
                    response = f"{get_single_comment(id)}"
                else:
                    response = f"{get_all_comments()}"
            elif resource == "tags":
                if id is not None:
                    response = f"{get_single_tag(id)}"
                else:
                    response = f"{get_all_tags()}"
            elif resource == "categories":
                if id is not None:
                    response = f"{get_single_category(id)}"
                else:
                    response = f"{get_all_categories()}"
            elif resource == "postTags":
                response = f"{get_post_tags(id)}"

        elif len(parsed) == 3:
            (resource, key, value) = parsed

            if key == 'user_id' and resource == 'posts':
                response = get_current_user_posts(value)

            # Is the resource `customers` and was there a
            # query parameter that specified the customer
            # email as a filtering value?

        self.wfile.write(f"{response}".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.

    def do_POST(self):
        """Handles POST requests to the server
        """
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_item = None
        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        # EXAMPLE BELOW
        if resource == "register":
            new_item = create_user(post_body)
        elif resource == "login":
            new_item = login_user(post_body)
        elif resource == "posts":
            new_item = create_post(post_body)
        elif resource == "tags":
            new_item = create_tag(post_body)
        elif resource == "categories":
            new_item = create_category(post_body)

        self.wfile.write(f"{new_item}".encode())
        # Encode the new animal and send in response

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)
        success = False
        # Delete a single animal from the list
        # EXAMPLE BELOW
        # if resource == "animals":
        #     success = update_animal(id, post_body)

        # Encode the new animal and send in response
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
        self.wfile.write("".encode())

    def do_PATCH(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)
        success = False
        # Delete a single animal from the list
        # EXAMPLE BELOW
        # if resource == "animals":
        #     success = update_animal(id, post_body)

        if resource == "tags":
            success = update_tag(id, post_body)
        if resource == "categories":
            success = update_category(id, post_body)
        if resource == "posts":
            success = update_post(id, post_body)

        # Encode the new animal and send in response
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
        self.wfile.write("".encode())

    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        # EXAMPLE BELOW
        # if resource == "animals":
        #     delete_animal(id)
        if resource == "users":
            delete_user(id)

        elif resource == "posts":
            delete_post(id)
        elif resource == "categories":
            delete_category(id)
        elif resource == "tags":
            delete_tag(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

# This function is not inside the class. It is the starting
# point of this application.


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
