__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'
import os
import shutil

# 1. clean_cache: takes no arguments and creates an empty folder named cache in the current directory. If it already exists, it deletes everything in the cache folder.

def clean_cache():
    dir_path = './cache'
    if os.path.isdir('./cache') == True:
        shutil.rmtree(dir_path)  # delete folder /cache
        os.mkdir(dir_path)  # create folder /cache
        print(f"successfully cleared folder {dir_path[1:]}")
    else:
        os.mkdir(dir_path)  # create folder /cache
        print(f"successfully created folder {dir_path[1:]}")
    return


# 2. cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, in that order. The function then unpacks the indicated zip file into a clean cache folder.

import time


def cache_zip(zip_file_path, cache_dir_path):
    clean_cache()
    wait(3)
    from zipfile import ZipFile
    ZipFile(zip_file_path).extractall(cache_dir_path)
    print("files unzipped - ready. Files include:")
    return


def wait(seconds):
    print(f"waiting {seconds} seconds for Windows to realize internal operations....")
    time.sleep(seconds)
    return


zip_file_path = os.path.abspath("data.zip")
cache_dir_path = os.path.join("cache")
cache_zip(zip_file_path, cache_dir_path)


# 3. cached_files: takes no arguments and returns a list of all the files in the cache. The file paths should be specified in absolute terms. Search the web for what this means! No folders should be included in the list. You do not have to account for files within folders within the cache directory.
def cached_files():
    file_list = ""
    os.chdir('cache')
    for file in os.listdir():
        file_list = file_list + os.path.abspath(file) + " "
    return file_list


cached_files = cached_files()


# 4. find_password: takes the list of file paths from cached_files as an argument. This function should read the text in each one to see if the password is in there. Surely there should be a word in there to incidicate the presence of the password? Once found, find_password should return this password string.

def Convert(string):
    li = list(string.split(" "))
    return li


def find_password(cached_files):
    for i in cached_files:
        with open(i) as fp:
            line = fp.readline()
            while line:
                if "password" in line:
                    signal = line
                    file_number = i
                else:
                    pass
                line = fp.readline()
    return signal, file_number


cached_files = Convert(cached_files)  # Conversion from string tot list of cached files
print(cached_files.pop())
print(find_password(cached_files))