import os

def path_walker(path):
    return os.walk(path)

def add_name_to_path(path, name):
    return os.path.join(path, name)

def remove_file(path):
    if os.path.exists(path):
        os.remove(path)
        return True
    else:
        return False

def get_dir():
    return os.getcwd()