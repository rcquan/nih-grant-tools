#!/usr/bin/python

import docx
import pandas as pd
import os


def extract_references(doc, author, refnumbers):
    references_by_author = []
    for paragraph in doc.paragraphs:
        if paragraph.style == "ListNumber" and "PMC" not in paragraph.text:
            article = paragraph.text.lstrip()
            reference = {
                "author": author.encode("utf-8"),
                "refnumber": "",
                "article": article.encode("utf-8")
            }
            references_by_author.append(reference)
        for refnumber in refnumbers:
            if paragraph.text.startswith(refnumber) and "PMC" not in paragraph.text:
                article = strip_characters(paragraph.text, refnumber)
                # store result in dictionary
                reference = {
                    "author": author.encode("utf-8"),
                    "refnumber": refnumber.encode("utf-8"),
                    "article": article.encode("utf-8")
                }
                references_by_author.append(reference)
    return references_by_author


def check_extension(filename):
    if filename.endswith(".docx"):
        return True


def strip_characters(text, pattern):
    return text.lstrip(pattern).lstrip()


def main():
    dir_name = os.getcwd()
    filenames = os.listdir(dir_name)
    reference_list = []
    # get a list of reference numbers
    refnumbers = [str(x) + "." for x in range(1, 30)]
    for filename in filenames:
        print "Processing " + filename
        if check_extension(filename):
            # get the author name
            author = filename.split(" ")[0]
            print "Author name is " + author + "."
            # parse the DOCX
            doc = docx.Document(filename)
            # extract numbered references within DOCX file
            references_by_author = extract_references(doc, author, refnumbers)
            if not references_by_author:
                print "Unable to parse references."
            reference_list += references_by_author
    # convert to data frame
    data = pd.DataFrame(reference_list)
    data.to_csv("biosketch_references.csv")

if __name__ == '__main__':
    main()
