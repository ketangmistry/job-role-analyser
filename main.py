from io import FileIO
from os import environ
import sys

def get_first_line(file: FileIO):
    return file.read().splitlines()[0]

def get_keywords_and_skills_from_line(line: str, keywords: list, skills: list) -> dict:
    w = line.lower().replace('/', ' ').replace('(', ' ').replace(')', ' ').split(' ')
    m = dict()

    if keywords is not None or skills is not None:
        for k in keywords:
            if k in w:
                w = [skill in w for skill in skills]
                m[k] = [x for x, y in zip(skills, w) if y]

    return m
            
def main():
    with open(sys.argv[1], 'r') as arg1, open(sys.argv[2], 'r') as arg2, open(sys.argv[3], 'r') as arg3:
        requirements = arg1.read().splitlines()
        keywords = arg2.read().splitlines()
        skills= arg3.read().splitlines()
        for line in requirements:
            matches = get_keywords_and_skills_from_line(line, keywords, skills)

            # TODO: you can do a lot more than just printing it out!
            print(matches)

if __name__ == '__main__':
    main()
