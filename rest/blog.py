import os
import tempfile
import time
from datetime import datetime
from threading import Thread

from flask import Blueprint, request, send_file

blog_blueprint = Blueprint('blog', __name__)


@blog_blueprint.route('/create', methods=['POST'])
def create_post_with_request_params():
    """
    Create a blog post from JSON request data and return it as a downloadable text file.

    The function reads 'title' and 'content' from the JSON body of a POST request,
    creates a temporary text file with the blog post details including the current date and time,
    and sends this file as a download to the client.

    Returns:
        A Flask response object that triggers the download of the created text file.
    """
    data = request.json  # Get JSON data from the request body
    title = data.get('title', 'Unknown')  # Default to 'Unknown' if 'title' is not provided
    content = data.get('content', 'Unknown')  # Default to 'Unknown' if 'content' is not provided

    return create_and_send_temp_file(content, title)


@blog_blueprint.route('/create/', methods=['GET'])
def create_get_with_query_params():
    """
    Create a blog post from URL query parameters and return it as a downloadable text file.

    The function reads 'title' and 'content' from the query parameters of a GET request,
    creates a temporary text file with the blog post details including the current date and time,
    and sends this file as a download to the client.

    Returns:
        A Flask response object that triggers the download of the created text file.
    """
    title = request.args.get('title', 'Unknown')
    content = request.args.get('content', 'Unknown')

    return create_and_send_temp_file(content, title)


def delete_file_later(file_path, delay=10):
    """
    Delete the specified file after a delay. If the folder containing the file is empty after
    deleting the file, delete the folder as well.

    Args:
        file_path (str): The path of the file to be deleted.
        delay (int): The time in seconds to wait before deleting the file.
    """
    time.sleep(delay)
    try:
        os.remove(file_path)
        folder_path = os.path.dirname(file_path)

        # Check if the folder is empty
        if not os.listdir(folder_path):
            os.rmdir(folder_path)
    except OSError as e:
        print(f"Error: {e}")


def create_temp_file(content, title):
    """
       Create a temporary text file with the specified content and title, including the current date and time.

       Args:
           content (str): The content to be written to the file.
           title (str): The title to be used in the file.

       Returns:
           str: The path to the created temporary file.
       """
    # Create 'temp' directory if it doesn't exist
    temp_dir = 'temp'
    os.makedirs(temp_dir, exist_ok=True)

    # Create a temporary text file in the 'temp' directory
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt', dir=temp_dir, encoding='utf-8')

    try:
        temp_file.write("Blog entry\n")
        add_date_and_time(temp_file)
        temp_file.write(f"{title}\n")
        temp_file.write(f"{content}\n")
        temp_file_path = temp_file.name  # Save the path to access the file later
    finally:
        temp_file.close()  # Ensure the file is closed properly

    return temp_file_path


def add_date_and_time(temp_file):
    """
    Add the current date and time to the passed temporary file.

    Args:
        temp_file (TemporaryFile): The temporary file to which the date and time should be written.
    """
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    temp_file.write(f"Date and Time: {now}\n\n")


def create_and_send_temp_file(content, title):
    """
    Create a temporary text file with the specified content and title, and send it as a downloadable file.
    The file is scheduled to be deleted after a short delay.

    Args:
        content (str): The content to be written to the file.
        title (str): The title to be used in the file.

    Returns:
        A Flask response object that triggers the download of the created text file.
    """
    temp_file_path = create_temp_file(content, title)

    # Schedule the file to be deleted later
    Thread(target=delete_file_later, args=(temp_file_path,)).start()

    return send_file(temp_file_path, as_attachment=True, download_name=f"{title}.txt", mimetype='text/plain')
