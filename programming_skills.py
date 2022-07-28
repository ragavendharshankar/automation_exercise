import os

'''using os.clone function returns file starts with T and ends with S irrespective of the file extension'''
def search_files():
    number_of_files =[]
    for directory, sub_directory, files in os.walk(".",topdown=True):
        for file in files:
            if file.startswith("T") or os.path.splitext(file)[0].endswith('S'):
                number_of_files.append(file)
    return number_of_files


print(len(search_files()))
