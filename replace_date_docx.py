#!/usr/bin/python

import datetime
import random
import os.path
import re
import sys
from docx import Document


def replace_date_docx(filename, search):
    """
    Replaces dates in .docx files with randomized date.
    """
    if check_extension(filename):
        document = Document(filename)
        for paragraph in document.paragraphs:
            if any(word in paragraph.text for word in search):
                print "Replacing " + paragraph.text + "..."
                paragraph.text = randomize_datetime(2015, 2)
                print "with " + paragraph.text + "\n"
        document.save(filename)
    else:
        print "File does not have a .docx extension."


def check_extension(filename):
    if filename.endswith(".docx"):
        return True


def randomize_datetime(year, month):
    """
    Randomizes date within a given month and year.
    Outputs to "February 15, 2015" format.
    """
    day = random.choice(range(1, 20))
    date = datetime.datetime(year, month, day)
    return date.strftime("%B %d, %Y")


def rename_file(filename, pattern, replace):

    if pattern in filename.split(".")[0].split(" "):
        new_filename = re.sub(pattern, replace, filename)
        print "Renaming file to... " + new_filename + "\n"
        os.rename(filename, new_filename)


def get_filenames(dir_name):
    """
    Get filenames from current directory.
    """
    return os.listdir(dir_name)


def get_current_dir():
    """
    Get filepath of current directory.
    """
    return os.getcwd()


def main():
    dir_name = get_current_dir()
    if len(sys.argv) > 1:
        dir_name = sys.argv[1]
    filenames = get_filenames(dir_name)
    search = ["2014", "2015"]
    for filename in filenames:
        print "Processing " + filename + "..."
        replace_date_docx(filename, search=search)
        rename_file(filename, pattern="2014", replace="2015")


if __name__ == "__main__":
    main()
