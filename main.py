from io import FileIO
from operator import contains
import sys

def get_first_line(file: FileIO):
    return file.read().splitlines()[0]

def get_keywords_and_skills_from_line(line: str, skills: list, keywords: list):
    words = line.lower().split(' ')

    matches = dict()

    for k in keywords:
        if k in words:
            w = [skill in words for skill in skills]
            matches[k] = [x for x, y in zip(skills, w) if y]

    return matches
            
def main():
    pass

if __name__ == '__main__':
    main()
