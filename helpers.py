

import os

UPLOAD_FOLDER = "uploads"

def save_file(upload_file):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(UPLOAD_FOLDER, upload_file.filename)
    with open(file_path, "wb") as f:
        f.write(upload_file.file.read())

    return file_path
